package helper

import (
	"Redirect/fmtogram/types"
	"fmt"
	"log"
)

func ReturnText(telegramResponse *types.TelegramResponse) (text string) {
	if telegramResponse.Result[0].Message.Text != "" {
		text = telegramResponse.Result[0].Message.Text
	} else if telegramResponse.Result[0].Query.Data != "" {
		text = telegramResponse.Result[0].Query.Data
	}
	return text
}

func ReturnChatId(telegramResponse *types.TelegramResponse) (chatID int) {
	if telegramResponse.Result[0].Message.TypeFrom.UserID != 0 {
		chatID = telegramResponse.Result[0].Message.TypeFrom.UserID
	} else if telegramResponse.Result[0].Query.TypeFrom.UserID != 0 {
		chatID = telegramResponse.Result[0].Query.TypeFrom.UserID
	}
	return chatID
}

func ReturnName(telegramResponse *types.TelegramResponse) (name string) {
	if telegramResponse.Result[0].Message.TypeFrom.Name != "" {
		name = telegramResponse.Result[0].Message.TypeFrom.Name
	} else if telegramResponse.Result[0].Query.TypeFrom.Name != "" {
		name = telegramResponse.Result[0].Query.TypeFrom.Name
	}
	return name
}

func ReturnLastName(telegramResponse *types.TelegramResponse) (lastname string) {
	if telegramResponse.Result[0].Message.TypeFrom.LastName != "" {
		lastname = telegramResponse.Result[0].Message.TypeFrom.LastName
	} else if telegramResponse.Result[0].Query.TypeFrom.LastName != "" {
		lastname = telegramResponse.Result[0].Query.TypeFrom.LastName
	}
	return lastname
}

func ReturnUsername(telegramResponse *types.TelegramResponse) (username string) {
	if telegramResponse.Result[0].Message.TypeFrom.Username != "" {
		username = telegramResponse.Result[0].Message.TypeFrom.Username
	} else if telegramResponse.Result[0].Query.TypeFrom.Username != "" {
		username = telegramResponse.Result[0].Query.TypeFrom.Username
	}
	return username
}

func ReturnLanguage(telegramResponse *types.TelegramResponse) (language string) {
	if telegramResponse.Result[0].Message.TypeFrom.Language != "" {
		language = telegramResponse.Result[0].Message.TypeFrom.Language
	} else if telegramResponse.Result[0].Query.TypeFrom.Language != "" {
		language = telegramResponse.Result[0].Query.TypeFrom.Language
	}
	return language
}

func ReturnBotStatus(telegramResponse *types.TelegramResponse) (botstatus bool) {

	m_isbot := telegramResponse.Result[0].Message.TypeFrom.IsBot
	cl_isbot := telegramResponse.Result[0].Query.TypeFrom.IsBot

	if !m_isbot && !cl_isbot {
		botstatus = false
	} else if m_isbot && !cl_isbot || !m_isbot && cl_isbot {
		botstatus = true
	}
	return botstatus
}

func ReturnMessageId(message *types.MessageResponse) (messageId int, err error) {
	if message.Ok {
		messageId = message.Result.MessageId
	} else {
		err = fmt.Errorf("we don't have a message id")
	}
	return messageId, err
}

func ReturnPhotosFileIdout(message *types.MessageResponse) ([]string, error) {
	var (
		err     error
		fileIds []string
	)
	fileIds = make([]string, len(message.Result.Photo))
	if len(message.Result.Photo) > 0 {
		for i := 0; i < len(message.Result.Photo); i++ {
			fileIds[i] = message.Result.Photo[i].FileId
		}
	} else {
		err = fmt.Errorf("we don't have a Photo fileId")
	}
	return fileIds, err
}

func ReturnVideosFileIdout(message *types.MessageResponse) ([]string, error) {
	var (
		err     error
		fileIds []string
	)
	fileIds = make([]string, len(message.Result.Video))
	if len(message.Result.Video) > 0 {
		for i := 0; i < len(message.Result.Video); i++ {
			fileIds[i] = message.Result.Video[i].FileId
		}
	} else {
		err = fmt.Errorf("we don't have a Video fileId")
	}
	return fileIds, err
}

func ReturnPhotosFileIdfrom(tr *types.TelegramResponse) ([]string, error) {
	var (
		err     error
		fileIds []string
	)
	j := 0
	if len(tr.Result[0].Message.Photo) > 0 {
		l := len(tr.Result[0].Message.Photo) / 4
		fileIds = make([]string, l)
		for i := 0; i < l; i++ {
			fileIds[i] = tr.Result[0].Message.Photo[j].FileId
			j = j + 4
		}
	} else {
		err = fmt.Errorf("we don't have a Photo fileId")
	}
	return fileIds, err
}

func ReturnVideosFileIdfrom(tr *types.TelegramResponse) ([]string, error) {
	var (
		err     error
		fileIds []string
	)
	fileIds = make([]string, len(tr.Result[0].Message.Video))
	if len(tr.Result[0].Message.Video) > 0 {
		for i := 0; i < len(tr.Result[0].Message.Video); i++ {
			fileIds[i] = tr.Result[0].Message.Video[i].FileId
		}
	} else {
		err = fmt.Errorf("we don't have a Video fileId")
	}
	return fileIds, err
}

func ReturnPhotoResp(resp *types.MessageResponse) (fileid string, err error) {
	if len(resp.Result.Photo) > 0 {
		log.Print(len(resp.Result.Photo))
		if len(resp.Result.Photo) < 5 {
			fileid = resp.Result.Photo[0].FileId
		} else {
			err = fmt.Errorf("there is not a one Photo. There are a few. You should use [ReturnMediaResp]")
		}
	} else {
		err = fmt.Errorf("we don't have a Photo fileId")
	}
	return fileid, err
}

func ReturnVideoResp(resp *types.MessageResponse) (fileid string, err error) {
	if len(resp.Result.Video) > 0 {
		if len(resp.Result.Video) < 5 {
			fileid = resp.Result.Video[0].FileId
		} else {
			err = fmt.Errorf("there is not a one Video. There are a few. You should use [ReturnMediaResp]")
		}
	} else {
		err = fmt.Errorf("we don't have a Video fileId")
	}
	return fileid, err
}

func ReturnMediaResp(resp *types.MessageResponse) ([]types.Media, error) {
	var err error
	media := make([]types.Media, (len(resp.Result.Photo) + len(resp.Result.Video)))
	count := 0
	if len(resp.Result.Photo) > 0 || len(resp.Result.Video) > 0 {
		if len(resp.Result.Photo) < 4 && len(resp.Result.Video) < 4 {
			if len(resp.Result.Photo) > 1 {
				for i := range resp.Result.Photo {
					media[count].Media = resp.Result.Photo[i].FileId
					media[count].Type = "photo"
					count++
				}
			}
			if len(resp.Result.Video) > 1 {
				for i := range resp.Result.Video {
					media[count].Media = resp.Result.Video[i].FileId
					media[count].Type = "video"
					count++
				}
			}
		} else {
			err = fmt.Errorf("there are not a few Video or Photo. There is only one (maybe bouth of them photo+video). You should use [ReturnPhotoResp] or [ReturnVideoResp]")
		}
	} else {
		err = fmt.Errorf("we don't have any Videos or Photos")
	}
	return media, err
}

func ReturnPhotoReq(req *types.TelegramResponse) (fileId string, err error) {
	if len(req.Result[0].Message.Photo) > 0 {
		l := len(req.Result[0].Message.Photo) / 4
		if l == 1 {
			fileId = req.Result[0].Message.Photo[0].FileId
		} else {
			err = fmt.Errorf("there is not a one Photo. There are a few. You should use [ReturnMediaReq]")
		}
	} else {
		err = fmt.Errorf("we don't have a Photo fileId")
	}
	return fileId, err
}

func ReturnVideoReq(req *types.TelegramResponse) (fileId string, err error) {
	if len(req.Result[0].Message.Video) > 0 {
		l := len(req.Result[0].Message.Video) / 4
		if l == 1 {
			fileId = req.Result[0].Message.Video[0].FileId
		} else {
			err = fmt.Errorf("there is not a one Video. There are a few. You should use [ReturnMediaReq]")
		}
	} else {
		err = fmt.Errorf("we don't have a Video fileId")
	}
	return fileId, err
}

func ReturnMediaReq(req *types.TelegramResponse) ([]types.Media, error) {
	var err error
	media := make([]types.Media, (len(req.Result[0].Message.Photo) + len(req.Result[0].Message.Video)))
	count := 0
	if len(req.Result[0].Message.Photo) > 0 || len(req.Result[0].Message.Video) > 0 {
		if len(req.Result[0].Message.Photo) < 2 && len(req.Result[0].Message.Video) < 2 {
			if len(req.Result[0].Message.Photo) > 1 {
				for i := range req.Result[0].Message.Photo {
					media[count].Media = req.Result[0].Message.Photo[i].FileId
					media[count].Type = "photo"
					count++
				}
			}
			if len(req.Result[0].Message.Video) > 1 {
				for i := range req.Result[0].Message.Video {
					media[count].Media = req.Result[0].Message.Video[i].FileId
					media[count].Type = "video"
					count++
				}
			}
		} else {
			err = fmt.Errorf("there are not a few Video or Photo. There is only one (maybe bouth of them photo+video). You should use [ReturnPhotoResp] or [ReturnVideoResp]")
		}
	} else {
		err = fmt.Errorf("we don't have any Videos or Photos")
	}
	return media, err
}
