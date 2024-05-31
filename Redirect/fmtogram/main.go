package fmtogram

import (
	"Redirect/app"
	"Redirect/fmtogram/executer"
	"Redirect/fmtogram/formatter"
	"Redirect/fmtogram/helper"
	"Redirect/fmtogram/types"
	"log"
	"time"
)

func pollResponse(output chan *formatter.Formatter, reg *executer.RegTable) {
	var (
		offset           int
		err              error
		telegramResponse *types.TelegramResponse
		index            int
		chatID           int
	)

	err = executer.RequestOffset(types.TelebotToken, &offset)
	for err != nil {
		err = executer.RequestOffset(types.TelebotToken, &offset)
	}
	for {
		log.Print("The cycle started")
		telegramResponse = new(types.TelegramResponse)
		err = executer.Updates(&offset, telegramResponse)
		log.Print(telegramResponse)
		if len(telegramResponse.Result) != 0 && err == nil {
			chatID = helper.ReturnChatId(telegramResponse)
			index = reg.Seeker(chatID)
			log.Print(chatID, index)
			if index != executer.None {
				reg.Reg[index].Chu <- telegramResponse
			} else {
				index = reg.NewIndex()
				reg.Reg[index].UserId = chatID
				reg.Reg[index].Chu = make(chan *types.TelegramResponse, 1)
				reg.Reg[index].Chu <- telegramResponse
			}
			log.Print(reg.Reg)
			go Worker(reg.Reg[index].Chu, reg.Reg[index].Chb, output)
			offset = offset + 1
			log.Print("The cycle ended")
		} else if err != nil {
			panic(err)
		}
		time.Sleep(time.Second / 20)
	}
}

func Worker(input chan *types.TelegramResponse, mesoutput chan *types.MessageResponse, output chan *formatter.Formatter) {
	var (
		fm *formatter.Formatter
	)
	for len(input) > 0 {
		fm = app.Receiving(<-input)
		if err := fm.Complete(); err == nil {
			output <- fm
		}
	}
}

func pushRequest(requests <-chan *formatter.Formatter, reg *executer.RegTable) {
	for r := range requests {
		mes, err := r.Make()
		if err != nil {
			panic(err)
		}
		if mes.Ok {
			index := reg.Seeker(mes.Result.Chat.Id)
			reg.Reg[index].Chb = make(chan *types.MessageResponse, 1)
			reg.Reg[index].Chb <- mes
		}
	}
}

func Start() {
	var (
		requests chan *formatter.Formatter
		reg      *executer.RegTable
	)
	requests = make(chan *formatter.Formatter)
	reg = new(executer.RegTable)
	go pollResponse(requests, reg)
	go pushRequest(requests, reg)

	for {
		time.Sleep(time.Second)
	}
}
