package types

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

const HttpsRequest = "https://api.telegram.org/"

var (
	//ConnectTot func() *sql.DB = connect
	Db *sql.DB
)

const (
	Markdown string = "Markdown"
	HTML     string = "HTML"
)

func ConnectToDatabase(doc bool) *sql.DB {
	var (
		db  *sql.DB
		err error
	)
	if doc {
		db, err = sql.Open("postgres", docConnect())
	} else {
		db, err = sql.Open("postgres", connectData())
	}
	if err != nil {
		panic(err)
	}
	err = db.Ping()
	if err != nil {
		panic(err)
	}
	return db
}

type InfMessage struct {
	TypeFrom User    `json:"from"`
	Text     string  `json:"text"`
	Photo    []Photo `json:"photo"`
	Video    []Video `json:"video"`
}

type User struct {
	UserID   int    `json:"id"`
	IsBot    bool   `json:"is_bot"`
	Name     string `json:"first_name"`
	LastName string `json:"last_name"`
	Username string `json:"username"`
	Language string `json:"language_code"`
}

type TelegramUpdate struct {
	UpdateID  int        `json:"update_id"`
	MessageId int        `json:"message_id"`
	Message   InfMessage `json:"message"`
	Query     Callback   `json:"callback_query"`
}

type Callback struct {
	TypeFrom User   `json:"from"`
	Data     string `json:"data"`
}

type TelegramError struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
}

type TelegramResponse struct {
	Ok     bool             `json:"ok"`
	Result []TelegramUpdate `json:"result"`
	Error  *TelegramError   `json:"error,omitempty"`
	AppErr *chan error
}

type JustForUpdate struct {
	Ok     bool            `json:"ok"`
	Result []StorageOfJson `json:"result"`
}

type StorageOfJson struct {
	ID int `json:"update_id"`
}

type Media struct {
	Type  string `json:"type"`
	Media string `json:"media"`
}

type SendMessagePayload struct {
	ChatID      int     `json:"chat_id"`
	Text        string  `json:"text"`
	ReplyMarkup string  `json:"reply_markup"`
	Photo       string  `json:"photo"`
	Video       string  `json:"video"`
	ParseMode   string  `json:"parse_mode"`
	MessageId   int     `json:"message_id"`
	InputMedia  []Media `json:"media"`
}

type DelMessage struct {
	ChatId    int `json:"chat_id"`
	MessageId int `json:"message_id"`
}

type Chat struct {
	Id int `json:"id"`
}

type Photo struct {
	FileId string `json:"file_id"`
}

type Video struct {
	FileId string `json:"file_id"`
}

type Message struct {
	MessageId int     `json:"message_id"`
	Chat      Chat    `json:"chat"`
	Photo     []Photo `json:"photo"`
	Video     []Video `json:"video"`
}

type MessageResponse struct {
	Ok     bool    `json:"ok"`
	Result Message `json:"result"`
}

type FMTRS interface {
	WriteString(string)
	WriteChatId(int)
	WriteDeleteMesId(int)
	WriteEditMesId(int)
	AddPhotoFromStorage(string)
	AddPhotoFromTG(string)
	AddPhotoFromInternet(string)
	AddVideoFromStorage(string)
	AddVideoFromTG(string)
	AddVideoFromInternet(string)
	SetIkbdDim([]int)
	WriteInlineButtonCmd(string, string)
	WriteInlineButtonUrl(string, string)
	Send() error
}

type Responser interface {
	RequestOffset(string, *int) error
	Updates(string, *int, *TelegramResponse) error
}

func connectData() string {
	return fmt.Sprintf("user=%s password=%s dbname=%s sslmode=%s", username, password, dbname, sslmode)
}
func docConnect() string {
	return fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=%s",
		docHost,
		docPort,
		docUsername,
		docPass,
		docDbname,
		docSslmode)
}
