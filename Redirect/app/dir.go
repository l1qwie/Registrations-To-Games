package app

import (
	"Redirect/app/handler"
	"Redirect/apptype"
	"Redirect/fmtogram/formatter"
	"Redirect/fmtogram/helper"
	"Redirect/fmtogram/types"
)

func Receiving(tr *types.TelegramResponse) *formatter.Formatter {
	comm := new(apptype.User)
	fm := new(formatter.Formatter)
	comm.Id = helper.ReturnChatId(tr)
	comm.Language = helper.ReturnLanguage(tr)
	handler.Send(comm, fm)
	return fm
}
