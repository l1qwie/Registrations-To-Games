package formatter

import (
	"Redirect/fmtogram/errors"
	"Redirect/fmtogram/executer"
	"Redirect/fmtogram/types"
	"bytes"
	"encoding/json"
	"log"
)

func (fm *Formatter) WriteString(lineoftext string) {
	fm.Message.Text = lineoftext
}

func (fm *Formatter) WriteChatId(chatID int) {
	fm.Message.ChatID = chatID
}

func (fm *Formatter) WriteParseMode(mode string) {
	fm.Message.ParseMode = mode
}

func (fm *Formatter) WriteDeleteMesId(mesId int) {
	fm.DeleteMessage.MessageId = mesId
}

func (fm *Formatter) WriteEditMesId(mesId int) {
	fm.Message.MessageId = mesId
}

func (fm *Formatter) Error(err error) {
	fm.Err = err
}

func (fm *Formatter) Complete() error {
	if fm.Err != nil {
		errors.MadeMisstake(fm.Err)
	}
	return fm.Err
}

func (fm *Formatter) CheckDelete() (err error) {
	var (
		function    string
		jsonMessage []byte
		finalBuffer *bytes.Buffer
	)
	if fm.DeleteMessage.MessageId != 0 {
		function = "deleteMessage"
		fm.DeleteMessage.ChatId = fm.Message.ChatID
		jsonMessage, err = json.Marshal(fm.DeleteMessage)
		if err == nil {
			fm.contenttype = "application/json"
			finalBuffer = bytes.NewBuffer(jsonMessage)
		}
		if err == nil {
			_ = executer.Send(finalBuffer, function, fm.contenttype, false)
		}
	}
	return err
}

func (fm *Formatter) ReadyKB() {
	if fm.Keyboard.Keyboard != nil {
		jsonKeyboard, err := json.Marshal(fm.Keyboard)
		if err == nil {
			fm.Message.ReplyMarkup = string(jsonKeyboard)
		}
	}
}

func (fm *Formatter) makebuf() (*bytes.Buffer, error) {
	var buf *bytes.Buffer
	jsonMessage, err := json.Marshal(fm.Message)
	if err == nil {
		fm.contenttype = "application/json"
		buf = bytes.NewBuffer(jsonMessage)
	}
	return buf, err
}

func (fm *Formatter) sendMessage() (*bytes.Buffer, string, error) {
	buf, err := fm.makebuf()
	return buf, "sendMessage", err
}

func (fm *Formatter) editMessage() (*bytes.Buffer, string, error) {
	buf, err := fm.makebuf()
	return buf, "editMessageText", err
}

func (fm *Formatter) mediaGroup() error {
	buf, err := fm.makebuf()
	_ = executer.Send(buf, "sendMediaGroup", "application/json", true)
	return err
}

func (fm *Formatter) media() (*bytes.Buffer, string, error) {
	var (
		buf *bytes.Buffer
		err error
		f   string
	)
	if fm.kindofmedia[0] == fromStorage {
		buf = bytes.NewBuffer(nil)
		fm.contenttype, err = fm.prepareMedia(buf)
	} else {
		if fm.mediatype[0] == "photo" {
			f = "sendPhoto"
		} else {
			f = "sendVideo"
		}
		buf, err = fm.makebuf()
	}
	return buf, f, err
}

func (fm *Formatter) Make() (*types.MessageResponse, error) {
	var (
		buf     *bytes.Buffer
		f       string
		res     *types.MessageResponse
		mshstat bool
	)
	err := fm.CheckDelete()
	if err == nil {
		fm.ReadyKB()
	}
	if err == nil {
		if len(fm.Message.InputMedia) == 0 && fm.Message.Photo == "" && fm.Message.Video == "" {
			mshstat = true
			if fm.Message.MessageId == 0 {
				buf, f, err = fm.sendMessage()
			} else {
				buf, f, err = fm.editMessage()
			}
		} else if len(fm.Message.InputMedia) != 0 || fm.Message.Photo != "" || fm.Message.Video != "" {
			if len(fm.Message.InputMedia) > 1 {
				err = fm.mediaGroup()
				if err == nil {
					mshstat = true
					buf, f, err = fm.sendMessage()
				}
			} else {
				buf, f, err = fm.media()
			}
		}
	}
	if err == nil {
		log.Print("THE MESSAGE ID DELETE OR EDIT AND MARSHAL STATUS: ", fm.DeleteMessage.MessageId, fm.Message.MessageId, mshstat)
		res = executer.Send(buf, f, fm.contenttype, mshstat)
	}

	return res, err
}

func (fm *Formatter) Send() (mes *types.MessageResponse, err error) {
	var (
		jsonMessage   []byte
		finalBuffer   *bytes.Buffer
		function      string
		marshalstatus bool
	)

	err = fm.CheckDelete()
	if err == nil {
		fm.ReadyKB()
	}
	if err == nil {
		if len(fm.Message.InputMedia) == 0 && fm.Message.Photo == "" && fm.Message.Video == "" {
			if fm.Message.MessageId == 0 {
				marshalstatus = true
				function = "sendMessage"
			} else {
				function = "editMessageText"
			}
			jsonMessage, err = json.Marshal(fm.Message)
			if err == nil {
				fm.contenttype = "application/json"
				finalBuffer = bytes.NewBuffer(jsonMessage)
			}
		} else if len(fm.Message.InputMedia) != 0 || fm.Message.Photo != "" || fm.Message.Video != "" {
			marshalstatus = true
			if len(fm.Message.InputMedia) > 1 {
				function = "sendMediaGroup"
				m := fm.Message.Text
				fm.Message.Text = ""
				//finalBuffer = bytes.NewBuffer(nil)
				jsonMessage, err = json.Marshal(fm.Message)
				if err == nil {
					fm.contenttype = "application/json"
					finalBuffer = bytes.NewBuffer(jsonMessage)
				}
				//fm.contenttype, err = fm.createMediaGroup(finalBuffer)
				_ = executer.Send(finalBuffer, function, fm.contenttype, marshalstatus)
				fm.Message.InputMedia = []types.Media{{}}
				fm.Message.Text = m
				function = "sendMessage"
			} else {
				if fm.mediatype[0] == "photo" {
					function = "sendPhoto"
				} else if fm.mediatype[0] == "video" {
					function = "sendVideo"
				}
				if fm.kindofmedia[0] == fromStorage {
					finalBuffer = bytes.NewBuffer(nil)
					fm.contenttype, err = fm.prepareMedia(finalBuffer)
				} else {
					jsonMessage, err = json.Marshal(fm.Message)
					if err == nil {
						fm.contenttype = "application/json"
						finalBuffer = bytes.NewBuffer(jsonMessage)
					}
				}
			}
		}

	}
	if err == nil {
		mes = executer.Send(finalBuffer, function, fm.contenttype, marshalstatus)
	}

	return mes, err
}
