package executer

import (
	"Redirect/fmtogram/errors"
	"Redirect/fmtogram/types"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"net/url"
)

const None int = -1

type Entry struct {
	UserId int
	Chu    chan *types.TelegramResponse
	Chb    chan *types.MessageResponse
}

type RegTable struct {
	Reg []Entry
}

func GetpostRequest(url string, Buffer *bytes.Buffer, contenttype string) (body []byte, err error) {
	var (
		request  *http.Request
		response *http.Response
		client   *http.Client
	)
	request, err = http.NewRequest("POST", url, Buffer)
	if err != nil {
		panic(err)
	}

	request.Header.Set("Content-Type", contenttype)
	client = &http.Client{}
	response, err = client.Do(request)
	if err != nil {
		panic(err)
	}
	defer response.Body.Close()
	return io.ReadAll(response.Body)
}

func heandlerMessage(response []byte, mes *types.MessageResponse) (err error) {
	log.Print("string(response): ", string(response))
	err = json.Unmarshal(response, &mes)
	if err != nil {
		err = nil
		tr := new(types.TelegramResponse)
		err = json.Unmarshal(response, &tr)
		mes.Result.Photo = []types.Photo{{FileId: "TRASHID"}}
	}
	return err
}

func Send(buf *bytes.Buffer, function, contenttype string, unmarshal bool) (mes *types.MessageResponse) {
	var (
		err  error
		url  string
		body []byte
	)
	log.Print("THE REQUEST TO TELEGRAM: ", buf.String())
	url = fmt.Sprintf("%sbot%s/%s", types.HttpsRequest, types.TelebotToken, function)
	body, err = GetpostRequest(url, buf, contenttype)
	log.Print("THE RESPONSE FROM TELEGRAM: ", string(body))
	if err == nil && unmarshal {
		mes = new(types.MessageResponse)
		err = heandlerMessage(body, mes)
		log.Print("mes.Result.MessageId: ", mes.Result.MessageId)
	} else if !unmarshal {
		mes = &types.MessageResponse{
			Ok: false,
			Result: types.Message{
				MessageId: 0,
				Chat: types.Chat{
					Id: 0,
				},
			},
		}
	}
	if err != nil {
		panic(err)
	}
	return mes
}

func Updates(offset *int, telegramResponse *types.TelegramResponse) (err error) {
	var (
		response *http.Response
		body     []byte
	)
	log.Print(*offset, telegramResponse)
	url := fmt.Sprintf(types.HttpsRequest+"bot%s/getUpdates?limit=1&offset=%d", types.TelebotToken, *offset)
	response, err = http.Get(url)
	if err == nil {
		log.Print(*response)
		body, err = io.ReadAll(response.Body)
	}
	if err == nil {
		log.Print(string(body))
		err = handlerTelegramResponse(body, telegramResponse)
	}
	log.Print(string(body), telegramResponse)
	response.Body.Close()
	return err
}

func handlerTelegramResponse(response []byte, telegramResponse *types.TelegramResponse) (err error) {
	err = json.Unmarshal(response, &telegramResponse)
	if err == nil {
		if !telegramResponse.Ok {
			err = fmt.Errorf(fmt.Sprintf("Telegram API вернул ошибку: %s", telegramResponse.Error.Message))
		}
	}
	return err
}

func (reg *RegTable) Seeker(chatID int) (index int) {
	var i int
	index = None
	if len(reg.Reg) != 0 {
		for i < len(reg.Reg) && reg.Reg[i].UserId != chatID {
			i++
		}
		if reg.Reg[i].UserId == chatID {
			index = i
		}
	}
	return index
}

func (reg *RegTable) NewIndex() (newIndex int) {
	newIndex = len(reg.Reg)
	reg.Reg = append(reg.Reg, Entry{})
	return newIndex
}

func handlerOffsetResponse(response []byte, offset *int) (err error) {
	var telegramResponse types.JustForUpdate

	err = json.Unmarshal(response, &telegramResponse)
	if err == nil {
		if len(telegramResponse.Result) > 0 {
			for _, storage := range telegramResponse.Result {
				*offset = storage.ID
			}
		} else {
			err = errors.UpdatesMisstakes("Telegram returned an empty data of telegramResponse")
		}
	}

	return err
}

func RequestOffset(TelebotToken string, offset *int) (err error) {
	var (
		response *http.Response
		body     []byte
	)

	Url := fmt.Sprintf("https://api.telegram.org/bot%s/getUpdates?limit=1", url.PathEscape(TelebotToken))
	response, err = http.Get(Url)
	if err == nil {
		body, err = io.ReadAll(response.Body)
	}
	if err == nil {
		err = handlerOffsetResponse(body, offset)
	}
	response.Body.Close()

	return err
}
