package dict

var Dictionary map[string]map[string]string

func ru(dict map[string]string) {
	dict["Hello"] = "Здравствуйте! Я очень рад, что вы решили опробовать мой продукт. Нажмите на ссылку ниже, чтобы перейти к редакторскому или клиентскому боту.\nClient - t.me/reg_to_games_cl_bot\nAdmin - t.me/reg_to_games_ad_bot"
}

func en(dict map[string]string) {
	dict["Hello"] = "Hello! I am very glad that you decided to try my product. Click the link below to go to the editor bot or the customer bot.\nClient - t.me/reg_to_games_cl_bot\nAdmin - t.me/reg_to_games_ad_bot"
}

func tur(dict map[string]string) {
	dict["Hello"] = "Merhaba! Ürünümü denemeye karar verdiğiniz için çok mutluyum. Editör botuna veya müşteri botuna geçmek için aşağıdaki bağlantıya tıklayın.\nClient - t.me/reg_to_games_cl_bot\nAdmin - t.me/reg_to_games_ad_bot"
}

func init() {
	Dictionary = make(map[string]map[string]string)
	Dictionary["ru"] = make(map[string]string)
	Dictionary["en"] = make(map[string]string)
	Dictionary["tur"] = make(map[string]string)
	ru(Dictionary["ru"])
	en(Dictionary["en"])
	tur(Dictionary["tur"])
}
