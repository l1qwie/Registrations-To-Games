from Admin_bot.Clients.clients_keyboard import ClientsDirections, FromWhere, SaveOrChange, OptionChange
from Admin_bot.Clients.clients_database import SelectClient, SelectCountClient, SaveNewClient, SelectAllOfUserId, SelectAllInf, ChangeColumnUserInt, ChangeColumnUserStr, RemoveClient, FreeSeats, SelectPriceAndCurrency, RegClient
from Admin_bot.Game.game_database import ScheduleOfGamesWithSeats, LengthOfGames, SelectGameId
import language_dictionary_for_all
import used_by_everyone as forall

class CreateClient:
    name: str
    last_name: str
    phonenum: int




def ChooseClientDirection(S: dict[str, str], language: str) -> tuple[int, str, object]:
    return 1, S["choose_cl_dir"], ClientsDirections(S["create_client"], S["change_client"], S["delete_client"], S["reg_client"], language_dictionary_for_all.String[language]["main_menu_kb"])

def ShowClientsByDirection(S: dict[str, str], phrase: str, language: str, client_direction: str, level: int, act: str, launch_point: int) -> tuple[int, str, str, str, object, bool]:
    halt = False

    if phrase in ("create client", "change client", "delete client", "reg client to game", "next page", "previous page"):
        client_direction = phrase
        halt = True
        level = 2
        if phrase != "create client":
            limit = 7
            names:list[tuple[int, str, str]] = SelectClient(limit, launch_point)
            length:int = SelectCountClient()
            if names != []:
                text = S["chose_your_client"]
                kbd = forall.KeyboardWithClientsNames(names, limit, launch_point, length, language)
            else:
                level = 3
                act = "divarication"
                text = S["no_clients"]
                kbd = forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"])
        else:
            text = S["choose_fromwhere"]
            kbd = FromWhere(S["teledirectionary"], language_dictionary_for_all.String[language]["main_menu_kb"])
    else:
        (level, text, kbd) = ChooseClientDirection(S, language)

    return (level, act, client_direction, text, kbd, halt)


def InputFromWhere(phrase: str, halt: bool) -> bool:

    if phrase in ("tg", "wapp", "vb", "calling"):
        halt = True

    return (halt)

def CreateFromWhere(S: dict[str, str], phrase: str, fromwhere: str, language: str, client_direction: str, level: int, halt: bool) -> tuple[int, str, str, object, bool, str]:
    _client_direction_:str = ''
    _act_:str = ''

    if InputFromWhere(phrase, halt):
        halt = True
        prmode = "HTML"
        level = 3
        fromwhere = phrase
        text = (S["fromwhere"] % (fromwhere)) + S["writename"]
        kbd = forall.GoToAdmin(language_dictionary_for_all.String[language]["main_menu_kb"])
    else:
        prmode = ''
        (level, _act_, _client_direction_, text, kbd, _halt_) = ShowClientsByDirection(S, client_direction, language, _client_direction_, level, _act_, 0)
    
    return (level, fromwhere, text, kbd, halt, prmode)

def CreateName(S: dict[str, str], phrase: str, fromwhere:str, language: str) -> tuple[int, str, str, object, str]:
    return 4, phrase, ((S["fromwhere+name"] % (fromwhere, phrase)) + S["writelastname"]), forall.GoToAdmin(language_dictionary_for_all.String[language]["main_menu_kb"]), "HTML"

def CreateLastName(S: dict[str, str], phrase: str, language: str, name: str, fromwhere: str) -> tuple[int, str, str, object, str]:
    return 5, phrase, ((S["fromwhere+name+last_name"] % (fromwhere, name, phrase)) + S["writephonenum"]), forall.GoToAdmin(language_dictionary_for_all.String[language]["main_menu_kb"]), "HTML"

def CreatePhoneNum(S: dict[str, str], phrase: str, language: str, halt: bool, level: int, name: str, last_name: str, phonenum: int, fromwhere: str) -> tuple[int, int, str, object, bool, str]:
    text:str = ''
    kbd:object = None

    if forall.IntCheck(phrase):
        halt = True
        level = 6
        phonenum = int(phrase)
        prmode = "HTML"
        text = (S["fromwhere+name+last_name+phonenum"] % (fromwhere, name, last_name, phonenum)) + S["saveorchange"]
        kbd = SaveOrChange(S["savegame"], S["changegame"], language_dictionary_for_all.String[language]["main_menu_kb"])
    else:
        (level, _lastname_, text, kbd, prmode) = CreateLastName(S, last_name, language, name, fromwhere)

    return (level, phonenum, text, kbd, halt, prmode)

def CreateSaveOrChange(S: dict[str, str], phrase: str, level: int, language: str, aid: int, act: str, phonenum: int, name: str, last_name: str, fromwhere: str) -> tuple[int, str, str, object, bool, str]:
    halt:bool = False
    text:str = ''
    kbd:object = None
    _halt_:bool = False
    _phonenum_:int = -1

    if phrase in ("save", "change"):
        halt = True
        prmode = ''
        if phrase == "save":
            SaveNewClient(aid)
            text = S["data_save"]
            kbd = forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"])
            act = "divarication"
            level = 3
        else:
            pass
    else:
        (level, _phonenum_, text, kbd, _halt_, prmode) = CreatePhoneNum(S, str(phonenum), language, _halt_, level, name, last_name, _phonenum_, fromwhere)

    return (level, act, text, kbd, halt, prmode)

def InputUserId(S: dict[str, str], phrase: str, level: int, halt: bool, language: str, user_id: int, client_direction: str, launch_point: int) -> tuple[int, int, int, str, str, object, bool]:
    text:str = ''
    kbd:object = None
    prmode = ''
    _client_direction_:str = ''
    _act_:str = ''

    if forall.IntCheck(phrase):
        if SelectAllOfUserId(int(phrase)):
            halt = True
            prmode = "HTML"
            level = 3
            user_id = int(phrase)
            text = S["user_inf"] % (SelectAllInf(user_id)) + S["choose_dir_for_change"]
            kbd = OptionChange(S["fromwhere_kb"], S["name_kb"], S["last_name_kb"], S["phonenum_kb"], language_dictionary_for_all.String[language]["main_menu_kb"])
        else:
            (level, _act_, _client_direction_, text, kbd, _halt_) = ShowClientsByDirection(S, client_direction, language, _client_direction_, level, _act_, launch_point)
    else:
        if phrase == "next page":
            launch_point += 7
        elif phrase == "previous page":
            launch_point += -7
        (level, _act_, _client_direction_, text, kbd, _halt_) = ShowClientsByDirection(S, client_direction, language, _client_direction_, level, _act_, launch_point)

    return (level, launch_point, user_id, prmode, text, kbd, halt)

def InputChangeOption(S: dict[str, str], phrase: str, user_id: int, changeoption: str, language: str, level: int, halt: bool) -> tuple[int, str, str, str, object, bool]:
    text:str = ''
    kbd:object = None
    prmode:str = ''
    _client_direction_:str = ''
    _launch_point_:int = -1

    if phrase in ("from_where", "name", "last_name", "phone_number"):
        halt = True
        level = 4
        changeoption = phrase
        if phrase == "from_where":
            text = S["choose_fromwhere"]
            kbd = FromWhere(S["teledirectionary"], language_dictionary_for_all.String[language]["main_menu_kb"])
        elif phrase == "name":
            text = S["writename"]
        elif phrase == "last_name":
            text = S["writelastname"]
        elif phrase == "phone_number":
            text = S["writephonenum"]
    else:
        (level, _launch_point_, _user_id_, prmode, text, kbd, _halt_) = InputUserId(S, str(user_id), level, halt, language, user_id, _client_direction_, _launch_point_)

    return (level, changeoption, prmode, text, kbd, halt)

def InputNewData(S: dict[str, str], phrase: str, user_id: int, changeoption: str, language: str, halt: bool, level: int) -> tuple[int, str, int, str, str, object, bool]:
    prmode:str = ''
    _user_id_:int = -1
    _halt_:bool = False
    changeddata_int:int = -1
    changeddata_str:str = ''

    if changeoption == "phone_number":
        if forall.IntCheck(phrase):
            halt = True
            changeddata_int = int(phrase)
            ChangeColumnUserInt(user_id, changeddata_int)
            text = S["user_inf"] % (SelectAllInf(user_id)) + S["inf_saved"] + S["data_changed"]
            kbd = forall.AnotherChange(S["yes"], S["no"])
            prmode = "HTML"
            level = 5
        else:
            (level, _changeoption_, prmode, text, kbd, _halt_) = InputChangeOption(S, changeoption, _user_id_, changeoption, language, level, _halt_)
    elif changeoption == "from_where":
        if InputFromWhere(phrase, halt):
            halt = True
            changeddata_str = phrase
            ChangeColumnUserStr(user_id, changeoption, changeddata_str)
            text = S["user_inf"] % (SelectAllInf(user_id)) + S["inf_saved"] + S["data_changed"]
            kbd = forall.AnotherChange(S["yes"], S["no"])
            prmode = "HTML"
            level = 5
        else:
            (level, _changeoption_, prmode, text, kbd, _halt_) = InputChangeOption(S, changeoption, _user_id_, changeoption, language, level, _halt_)
    elif changeoption in ("name", "last_name"):
        changeddata_str = phrase
        ChangeColumnUserStr(user_id, changeoption, changeddata_str)
        text = S["user_inf"] % (SelectAllInf(user_id)) + S["inf_saved"] + S["data_changed"]
        kbd = forall.AnotherChange(S["yes"], S["no"])
        prmode = "HTML"
        level = 5
    else:
        assert(False)
    
    return (level, changeddata_str, changeddata_int, prmode, text, kbd, halt)

def InputRepeat(S: dict[str, str], phrase: str, level: int, user_id: int, language: str, changeoption: str, changeddata_int: int, changeddata_str: str, halt: bool):

    _client_direction_:str = ''

    if phrase == "another data change":
        halt = True
        (level,_launch_point_, _user_id_, prmode, text, kbd, _halt_) = InputUserId(S, str(user_id), level, halt, language, user_id, _client_direction_, 0)
    else:
        if changeoption == "phone_number":
            (level, changeddata_str, changeddata_int, prmode, text, kbd, _halt_) = InputNewData(S, str(changeddata_int), user_id, changeoption, language, halt, level)
        else:
            (level, changeddata_str, changeddata_int, prmode, text, kbd, _halt_) = InputNewData(S, changeddata_str, user_id, changeoption, language, halt, level)
    
    return (level, prmode, text, kbd, halt)

def DeleteClient(S: dict[str, str], phrase: str, client_direction: str, language: str, launch_point: int, level: int, act: str, halt: bool) -> tuple[int, int, str, str, object, bool]:
    _client_direction_:str = ''
    _act_: str = ''
    text:str = ''
    kbd:object = None

    if forall.IntCheck(phrase):
        if SelectAllOfUserId(int(phrase)):
            RemoveClient(int(phrase))
            halt = True
            text = S["client_delete"] + language_dictionary_for_all.String[language]["main_menu_text"]
            kbd = forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"])
            level = 3
            act = "divarication"
        else:
            (level,  _act_, _client_direction_, text, kbd, _halt_) = ShowClientsByDirection(S, client_direction, language, _client_direction_, level, _act_, launch_point)
    else:
        if phrase == "next page":
            launch_point += 7
        elif phrase == "previous page":
            launch_point += -7
        (level, _act_, _client_direction_, text, kbd, _halt_) = ShowClientsByDirection(S, client_direction, language, _client_direction_, level, _act_, launch_point)
    
    return (level, launch_point, act, text, kbd, halt)

def InputClientId(S: dict[str, str], phrase: str, language: str, game_launch_point: int, client_launch_point: int, client_direction: str, level: int, user_id: int, halt: bool) -> tuple[int, int, int, str, object, bool]:
    text:str = ''
    kbd:object = None
    _client_direction_:str = ''
    _act_:str = ''

    if forall.IntCheck(phrase):
        if SelectAllOfUserId(int(phrase)):
            halt = True
            level = 3
            user_id = int(phrase)
            schedule_input:list[tuple[int, str, int, int, int]] = ScheduleOfGamesWithSeats(game_launch_point, 7)
            length:int = LengthOfGames()
            schedule_output, _schedule_, = forall.SheduleStr(schedule_input, [], language)
            text = S["choose_game"]
            kbd = forall.Schedule(schedule_output, 7, game_launch_point, S["seats"], length)
        else:
            (level, _act_, _client_direction_, text, kbd, _halt_) = ShowClientsByDirection(S, client_direction, language, _client_direction_, level, _act_, client_launch_point)
    else:
        if phrase == "next page":
            client_launch_point += 7
        elif phrase == "previous page":
            client_launch_point += -7
        (level, _act_, _client_direction_, text, kbd, _halt_) = ShowClientsByDirection(S, client_direction, language, _client_direction_, level, _act_, client_launch_point)
    return (level, client_launch_point, user_id, text, kbd, halt)

def InputGameId(S: dict[str, str], phrase: str, level: int, language: str, game_launch_point: int, game_id: int, user_id: int, halt: bool) -> tuple[int, int, int, str, object, bool]:
    text:str = ''
    kbd:object = None
    _client_launch_point_:int = -1
    _client_direction_:str = ''

    if forall.IntCheck(phrase):
        if SelectGameId(int(phrase)):
            halt = True
            level = 4
            game_id = int(phrase)
            text = S["type_seats"]
            kbd = forall.GoToAdmin(language_dictionary_for_all.String[language]["main_menu_kb"])
        else:
            (level, _game_launch_point_, _user_id_, text, kbd, _halt_) = InputClientId(S, str(user_id), language, game_launch_point, _client_launch_point_, _client_direction_, level, user_id, halt)
    else:
        if phrase == "next page":
            game_launch_point += 7
        elif phrase == "previous page":
            game_launch_point += -7
        print("!!!!!!!!!!!!!!", game_launch_point)
        (level, _client_launch_point_, _user_id_, text, kbd, _halt_) = InputClientId(S, str(user_id), language, game_launch_point, _client_launch_point_, _client_direction_, level, user_id, halt)
    
    return (level, game_launch_point, game_id, text, kbd, halt)

def InputSeats(S: dict[str, str], phrase: str, level: int, language: str, game_id: int, seats: int, halt: bool) -> tuple[int, int, str, object, bool]:
    text:str = ''
    kbd:object = None
    _game_launch_point_:int = -1
    _user_id_:int = -1

    if forall.IntCheck(phrase):
        if FreeSeats(int(phrase), game_id):
            halt = True
            level = 5
            seats = int(phrase)
            text = S["choose_paymethod"]
            kbd = forall.KbPay(S["online"], S["cash"], language_dictionary_for_all.String[language]["main_menu_kb"])
        else:
            (level, _game_launch_point_, _game_id_, text, kbd, _halt_) = InputGameId(S, str(game_id), level, language, _game_launch_point_, game_id, _user_id_, halt)
    else:
        (level,_game_launch_point_, _game_id_, text, kbd, _halt_) = InputGameId(S, str(game_id), level, language, _game_launch_point_, game_id, _user_id_, halt)

    return (level, seats, text, kbd, halt)

def InputPaymethod(S: dict[str, str], phrase: str, level: int, language: str, user_id: int, game_id: int, seats: int, act: str, halt: bool, paymethod: str) -> tuple[int, str, str, str, object, bool]:
    text:str = ''
    kbd:object = ''

    if phrase in ("cash", "card"):
        halt = True
        level = 3
        paymethod = phrase
        act = "divarication"
        price, currency = SelectPriceAndCurrency(game_id)
        RegClient(user_id, game_id, seats, paymethod)
        text = S["client_reged"] % ((price*seats), currency) + language_dictionary_for_all.String[language]["main_menu_text"]
        kbd = forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"])
    else:
        (level, _seats_, text, kbd, _halt_) = InputSeats(S, str(seats), level, language, game_id, seats, halt)
    
    return (level, paymethod, act, text, kbd, halt)

def HeadFuncOfCreate(S:dict[str, str], phrase: str, language: str, level: int, act: str, client_direction: str, fromwhere: str, name: str, last_name: str, phonenum: int, halt: bool, aid: int) -> tuple[int, str, str, str, str, int, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    prmode:str = ''

    if level == 2:
        (level, fromwhere, text, kbd, halt, prmode) = CreateFromWhere(S, phrase, fromwhere, language, client_direction, level, halt)
    elif level == 3:
        (level, name, text, kbd, prmode) = CreateName(S, phrase, fromwhere, language)
    elif level == 4:
        (level, last_name, text, kbd, prmode) = CreateLastName(S, phrase, language, name, fromwhere)
    elif level == 5:
        (level, phonenum, text, kbd, halt, prmode) = CreatePhoneNum(S, phrase, language, halt, level, name, last_name, phonenum, fromwhere)
    elif level == 6:
        (level, act, text, kbd, halt, prmode) = CreateSaveOrChange(S, phrase, level, language, aid, act, phonenum, name, last_name, fromwhere)
    else:
        assert(False)
    return (level, act, fromwhere, name, last_name, phonenum, text, kbd, halt, prmode)

def HeadFuncOfChange(S: dict[str, str], phrase: str, language: str, level: int, user_id: int, changeoption:str, changeddata_str: str, changeddata_int: int, halt:bool, client_direction: str, launch_point: int) -> tuple[int, int, int, str, str, str, int, str, str, object, bool]:
    text:str = ''
    kbd:object = None
    prmode:str = ''

    if level == 2:
        (level, launch_point, user_id, prmode, text, kbd, halt) = InputUserId(S, phrase, level, halt, language, user_id, client_direction, launch_point)
    elif level == 3:
        (level, changeoption, prmode, text, kbd, halt) = InputChangeOption(S, phrase, user_id, changeoption, language, level, halt)
    elif level == 4:
        (level, changeddata_str, changeddata_int, prmode, text, kbd, halt) = InputNewData(S, phrase, user_id, changeoption, language, halt, level)
    elif level == 5:
        (level, prmode, text, kbd, halt) = InputRepeat(S, phrase, level, user_id, language, changeoption, changeddata_int, changeddata_str, halt)
    
    return (level, launch_point, user_id, client_direction, changeoption, changeddata_str, changeddata_int, prmode, text, kbd, halt)

def HeadFuncOfDelete(S: dict[str, str], phrase: str, level: int, client_direction: str, language: str, launch_point: int, act: str, halt: bool) -> tuple[int, int, str, str, object, bool]:
    text:str = ''
    kbd:object = None

    if level == 2:
        (level, launch_point, act, text, kbd, halt) = DeleteClient(S, phrase, client_direction, language, launch_point, level, act, halt)

    return (level, launch_point, act, text, kbd, halt)


def HeadFuncOfRegToGame(S: dict[str, str], phrase: str, level: int, language: str, game_launch_point: int, client_launch_point: int, client_direction: str, user_id:int, game_id: int, seats:int, paymethod: str, halt: bool, act: str) -> tuple[int, int, int, str, int, int, int, str, str, object, bool]:
    text:str = ''
    kbd:object = None

    if level == 2:
        (level, client_launch_point, user_id, text, kbd, halt) = InputClientId(S, phrase, language, game_launch_point, client_launch_point, client_direction, level, user_id, halt)
    elif level == 3:
        (level, game_launch_point, game_id, text, kbd, halt) = InputGameId(S, phrase, level, language, game_launch_point, game_id, user_id, halt)
    elif level == 4:
        (level, seats, text, kbd, halt) = InputSeats(S, phrase, level, language, game_id, seats, halt)
    elif level == 5:
        (level, paymethod, act, text, kbd, halt) = InputPaymethod(S, phrase, level, language, user_id, game_id, seats, act, halt, paymethod)
    else:
        assert(False)

    return (level, client_launch_point, game_launch_point, act, user_id, game_id, seats, paymethod, text, kbd, halt)
