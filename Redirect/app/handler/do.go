package handler

import (
	"Redirect/app/dict"
	"Redirect/apptype"
	"Redirect/fmtogram/formatter"
)

func Send(user *apptype.User, fm *formatter.Formatter) {
	fm.WriteString(dict.Dictionary[user.Language]["Hello"])
	fm.WriteChatId(user.Id)
}
