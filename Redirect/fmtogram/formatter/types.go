package formatter

import "Redirect/fmtogram/types"

type InlineKeyboard struct {
	Keyboard [][]btn `json:"inline_keyboard"`
	x        int
	y        int
}

type InputMediaPhoto struct {
	Type      string `json:"type"`
	Media     string `json:"media"`
	Caption   string `json:"caption"`
	ParseMode string `json:"parse_mode"`
}

type InputMedia struct {
	InputMediaPhoto InputMediaPhoto `json:"InputMediaPhoto"`
}

type Formatter struct {
	Message       types.SendMessagePayload
	Keyboard      InlineKeyboard
	DeleteMessage types.DelMessage
	Err           error
	contenttype   string
	kindofmedia   []int
	mediatype     []string
}

type btnKind int

const (
	bCmd btnKind = 1
	bUrl btnKind = 2

	fromStorage  int = 0
	fromTelegram int = 1
	fromInternet int = 2
)

type btn struct {
	Label string `json:"text"`
	what  btnKind
	Cmd   string `json:"callback_data"`
	Url   string `json:"url"`
}
