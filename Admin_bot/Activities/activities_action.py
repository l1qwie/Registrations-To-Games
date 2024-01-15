from Admin_bot.Activities.activities_keyboard import ActivitiesDirection, SendOrNo, LetsGO, RemoveFromGameOrCall
from Admin_bot.Activities.activities_database import FindChats, SelectLengthChats, SelectActiveGames, SelectLengthOfActiveGames, FoundChatId, FindSomeGames, FoundGameId, SelectAllInfFromSchedule, SelectYourClients, UpdateInfAboutChat, SelectActiveGameId, SelectWaitingClients, SelectInfClient, RemoveClientFormGame
from Admin_bot.Game.game_database import LengthOfGames, ScheduleOfGames
from Admin_bot.Clients.clients_database import SelectClient, SelectLengthOfClients
from Admin_bot.Settings.settings_keyboard import Language
from Admin_bot.language_dictoinary import String
import language_dictionary_for_all
import used_by_everyone as forall




def ChooseActivitiesDirection(S: dict[str, str], language: str) -> tuple[int, str, object]:
    return 1, S["Choose_dir_of_activities"] + S["rules_for_chat_game"], ActivitiesDirection(S["reg_game"], S["activ_game"], language_dictionary_for_all.String[language]["main_menu_kb"])

def StartAct(S: dict[str, str], phrase: str, direction: str, halt: bool, language: str, level: int, launch_point: int) -> tuple[int, str, str, object, bool]:
    text:str = ''
    kbd:object = None
    schedule:list[tuple[int, str, int, int, int]] = []
    input_schedule:list[tuple[str, str, str, str, str]] = []
    
    if phrase in ("create game", "active games"):
        halt = True
        level = 2
        if phrase == "create game":
            chatinf = FindChats(7, launch_point)
            if chatinf != []:
                direction = phrase
                length:int = SelectLengthChats()
                text = S["game_rules"] + S["foundchats"]
                kbd = forall.Chats(chatinf, 7, launch_point, length)
            else:
                text += S["no_new_chats"]
                (level, text2, kbd) = ChooseActivitiesDirection(S, language)
                text += text2
        else:
            schedule = SelectActiveGames(7, launch_point)
            if schedule != []:
                direction = phrase
                length = SelectLengthOfActiveGames()
                for game_id, sport, date, time, seats in schedule:
                    input_schedule.append((str(game_id), sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), str(seats)))
                text = S["active_games"]
                kbd = forall.Schedule(input_schedule, 7, launch_point, S["waiting_cl"], length)
            else:
                text = S["no_active_games"] 
                (level, text2, kbd) = ChooseActivitiesDirection(S, language)
                text += text2
    else:
        (level, text, kbd) = ChooseActivitiesDirection(S, language)

    return (level, direction, text, kbd, halt)

def InputChatId(S: dict[str, str], phrase: str, game_launch_point: int, chat_launch_point: int, limit: int, language: str, level: int, chatid: int, halt: bool, direction: str) -> tuple[int, int, int, str, object, bool]:
    _direction_:str = ''
    _halt_:bool = False
    length:int = -1
    text:str = ''
    text2:str = ''
    kbd:object = None

    if forall.IntCheck(phrase):
        if FoundChatId(int(phrase)):
            if FindSomeGames():
                halt = True
                chatid = int(phrase)
                level = 3

                length = LengthOfGames()
                schedule_input:list[tuple[int, str, int, int]] = ScheduleOfGames(game_launch_point, limit)
                _schedule_, schedule_output = forall.SheduleStr([], schedule_input, language)

                text = S["choose_game_for_chatgame"]
                kbd = forall.Schedule(schedule_output, limit, game_launch_point, '', length)
            else:
                text += S["no_games"]
                (level, _direction_, text2, kbd, _halt_) = StartAct(S, direction, direction, _halt_, language, level, chat_launch_point)
                text += text2
        else:
            text += S["no_chats"]
            (level, _direction_, text2, kbd, _halt_) = StartAct(S, direction, direction, _halt_, language, level, chat_launch_point)
            text += text2
    else:
        if phrase == "next page":
            chat_launch_point += 7
        elif phrase == "previous page":
            chat_launch_point += -7
        (level, _direction_, text, kbd, _halt_) = StartAct(S, direction, direction, _halt_, language, level, chat_launch_point)
    
    return (level, chatid, chat_launch_point, text, kbd, halt)

def StrSeats(seats: int, S: dict[str, str], users: list[tuple[str, str]]) -> str:
    i:int = 0
    paragraph:str = ''
    while i < seats:
        if i < len(users):
            space = f"{users[i][0]} {users[i][1]}"
        else:
            space = S["theseatsisfree"]
        paragraph += S["seats_counter"] % (i, space)
        i += 1
    return paragraph

def InputGameId(S: dict[str, str], phrase: str, game_id: int, halt: bool, language: str, level: int, chatid: int, game_launch_point: int, prmode: str) -> tuple[int, int, int, str, object, str, bool]:
    text:str = ''
    kbd:object = None
    _chat_launch_point_:int = -1
    _chat_id_:int = -1
    _halt_:bool = False
    _actwithchats_:str = ''

    if forall.IntCheck(phrase):
        if FoundGameId(int(phrase)):
            halt = True
            game_id = int(phrase)
            level = 4
            text = S["choose_language"]
            kbd = Language(S["ru"], S["en"], S["tur"], language_dictionary_for_all.String[language]["main_menu_kb"])
        else:
            (level, _chatid_, _chat_launch_point_, text, kbd, _halt_) = InputChatId(S, str(chatid), game_launch_point, _chat_launch_point_, 7, language, level, _chat_id_, _halt_, _actwithchats_)
    else:
        if phrase == "next page":
            game_launch_point += 7
        elif phrase == "previous page":
            game_launch_point += -7
        (level, _chatid_, _chat_launch_point_, text, kbd, _halt_) = InputChatId(S, str(chatid), game_launch_point, _chat_launch_point_, 7, language, level, _chat_id_, _halt_, _actwithchats_)
    
    return (level, game_launch_point, game_id, text, kbd, prmode, halt)

def InputLang(S: dict[str, str], phrase: str, language: str, game_id: int, halt: bool, level: int, chat_lang: str, prmode: str) -> tuple[int, str, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    sport:str = ''
    date:int = -1
    time:int = -1
    seats:int = -1
    price: int = -1
    currency:str = ''
    lat:float = -1
    long:float = -1
    nameaddress:str = ''
    _chatid_:int = -1
    _game_launch_point_:int = -1
    users:list[tuple[str, str]] = []
    users_from_db:list[tuple[str, str]] = []

    if phrase in ("en", "ru", "tur"):
        halt = True
        level = 5
        chat_lang = phrase
        prmode = "HTML"
        sport, date, time, seats, price, currency, lat, long, nameaddress = SelectAllInfFromSchedule(game_id)
        users_from_db = SelectYourClients(game_id)
        for name, lastname in users_from_db:
            if name == "no_data":
                name = language_dictionary_for_all.String[phrase][name]
            elif lastname == "no_data":
                lastname = language_dictionary_for_all.String[phrase][lastname]
            users.append((name, lastname))

        text = S["example_of_chat_game"] + String[phrase]["start_chatgame"] + String[phrase]["sport+date+time+seats+price+currency+link+nameaddress"] % (language_dictionary_for_all.String[phrase][sport], forall.CreateDateStr(date), forall.CreateTimeStr(time), seats, price, currency, lat, long, nameaddress) + (StrSeats(seats, String[phrase], users))
        kbd = SendOrNo(S["send"], language_dictionary_for_all.String[language]["main_menu_kb"])
    else:
        (level, _game_launch_point_, _game_id_, text, kbd, prmode, _halt_) = InputGameId(S, str(game_id), game_id, halt, language, level, _chatid_, _game_launch_point_, prmode)
    return (level, chat_lang, text, kbd, halt, prmode)


def InputSend(S: dict[str, str], phrase: str, language: str, game_id: int, halt: bool, level: int, act: str, chat_lang: str, chat_id: int, chatid: int) -> tuple[int, str, str, str, object, object, str, bool, int]:
    sport:str = ''
    date:int = -1
    time:int = -1
    seats:int = -1
    price: int = -1
    currency:str = ''
    lat:float = -1
    long:float = -1
    nameaddress:str = ''
    text:str = ''
    chattext:str = ''
    kbd:object = None
    chatkbd:object = None
    _chatid_:int = -1
    _game_launch_point_:int = -1
    prmode:str = ''
    users:list[tuple[str, str]] = []
    users_from_db:list[tuple[str, str]] = []

    if phrase == "send chat game":
        halt = True
        chatid = chat_id
        level = 3
        act = "divarication"
        UpdateInfAboutChat(chat_id, chat_lang)
        sport, date, time, seats, price, currency, lat, long, nameaddress = SelectAllInfFromSchedule(game_id)
        users_from_db = SelectYourClients((int(phrase)))
        for name, lastname in users_from_db:
            if name == "no_data":
                name = language_dictionary_for_all.String[phrase][name]
            elif lastname == "no_data":
                lastname = language_dictionary_for_all.String[phrase][lastname]
            users.append((name, lastname))

        text = S["chatgame_sended"] +  language_dictionary_for_all.String[language]["main_menu_text"]
        chattext = String[chat_lang]["start_chatgame"] + String[chat_lang]["sport+date+time+seats+price+currency+link+nameaddress"] % (language_dictionary_for_all.String[chat_lang][sport], forall.CreateDateStr(date), forall.CreateTimeStr(time), seats, price, currency, lat, long, nameaddress) + (StrSeats(seats, String[chat_lang], users))
        kbd = forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"])
        chatkbd = LetsGO(S["participate"], game_id)
    else:
        (level, _chat_lang_, text, kbd, _halt_, prmode) = InputLang(S, chat_lang, language, game_id, halt, level, chat_lang, prmode)
    
    return (level, act, text, chattext, kbd, chatkbd, prmode, halt, chatid)

def InputActiveGameId(S: dict[str, str], phrase: str, level: int, halt: bool, game_launch_point: int, clients_launch_point: int, language: str, direction: str, game_id: int) -> tuple[int, int, int, str, object, bool]:
    text:str = ''
    kbd:object = None
    _halt_:bool = False

    if forall.IntCheck(phrase):
        if SelectActiveGameId(int(phrase)):
            halt = True
            game_id = int(phrase)
            level = 3
            names:list[tuple[int, str, str]] = SelectClient(7, clients_launch_point)
            lengthofclients:int = SelectLengthOfClients(game_id)
            
            text = S["all_of_client_on_game"]
            kbd = forall.KeyboardWithClientsNames(names, 7, clients_launch_point, lengthofclients, language)
        else:
           (level, _direction_, text, kbd, _halt_) = StartAct(S, direction, direction, _halt_, language, level, game_launch_point)
    else:
        if phrase == "next page":
            game_launch_point += 7
        elif phrase == "previous page":
            game_launch_point += -7
        (level, _direction_, text, kbd, _halt_) = StartAct(S, direction, direction, _halt_, language, level, game_launch_point)
    
    return (level, game_id, game_launch_point, text, kbd, halt)

def InputUserId(S: dict[str, str], phrase: str, user_id: int, language: str, clients_launch_point: int, halt: bool, level: int, game_id: int) -> tuple[int, int, int, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    name:str = ''
    lastname:str = ''
    nickname:str = ''
    phone_str:str = ''
    fromwhere:str = ''
    cl_lang:str = ''
    prmode:str = ''
    _game_launch_point_:int = -1
    _game_id_:int = -1
    _halt_:bool = False
    _direction_:str = ''

    if forall.IntCheck(phrase):
        if SelectWaitingClients(int(phrase)):
            halt = True
            user_id = int(phrase)
            level = 4
            prmode = "HTML"
            name, lastname, nickname, phone_str, fromwhere, cl_lang = SelectInfClient(user_id)
            if name == "no_data":
                name = language_dictionary_for_all.String[language][name]
            elif lastname == "no_data":
                lastname = language_dictionary_for_all.String[language][lastname]
            elif phone_str == '-1':
                phone_str = language_dictionary_for_all.String[language]["no_data"]
            elif fromwhere == "no_data":
                fromwhere = language_dictionary_for_all.String[language][fromwhere]
            elif cl_lang == "no_data":
                cl_lang = language_dictionary_for_all.String[language][cl_lang]
            text = S["user_inf"] % (name, lastname, phone_str, fromwhere, cl_lang) + S["disclaimer"]
            if nickname:
                kbd = RemoveFromGameOrCall(S["removeforgame"], S["call"], language_dictionary_for_all.String[language]["main_menu_kb"], True, nickname)
            else:
                kbd = RemoveFromGameOrCall(S["removeforgame"], S["call"], language_dictionary_for_all.String[language]["main_menu_kb"], False, nickname)
        else:
            (level, _game_id_, _game_launch_point_, text, kbd, _halt_) = InputActiveGameId(S, str(game_id), level, halt, _game_launch_point_, clients_launch_point, language, _direction_, _game_id_)
    else:
        if phrase == "next page":
            clients_launch_point += 7
        elif phrase == "previous page":
            clients_launch_point += -7
        (level, _game_id_, _game_launch_point_, text, kbd, _halt_) = InputActiveGameId(S, str(game_id), level, halt, _game_launch_point_, clients_launch_point, language, _direction_, _game_id_)
    
    return (level, user_id, clients_launch_point, text, kbd, halt, prmode)

def InputDelete(S: dict[str, str], phrase: str, user_id: int, game_id: int, language: str, level: int, act: str, halt: bool) -> tuple[int, str, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    _clients_launch_point_:int = -1
    _halt_:bool = False
    _game_id_:int = -1
    prmode:str = ''

    if phrase == "remove from game":
        halt = True
        RemoveClientFormGame(user_id, game_id)
        text = S["client_removed"] + language_dictionary_for_all.String[language]["main_menu_text"]
        kbd = forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"])
        level = 3
        act = "divarication"
    else:
        (level, _user_id_, _clients_launch_point_, text, kbd, _halt_, prmode) = InputUserId(S, str(user_id), user_id, language, _clients_launch_point_, _halt_, level, _game_id_)
    
    return (level, act, text, kbd, halt, prmode)


def ChatGame(S: dict[str, str], phrase: str, level: int, findchats: bool, language: str, direction:str, game_launch_point: int, chat_launch_point: int, chat_lang: str, chat_id: int, game_id: int, act: str, chatid: int):
    text:str = ''
    chattext:str = ''
    kbd:object = None
    chatkbd:object = None
    halt:bool = False
    prmode:str = ''
    
    if level == 2:
        (level, chat_id, chat_launch_point, text, kbd, halt) = InputChatId(S, phrase, game_launch_point, chat_launch_point, 7, language, level, chat_id, halt, direction)
    elif level == 3:
        (level, game_launch_point, game_id, text, kbd, prmode, halt) = InputGameId(S, phrase, game_id, halt, language, level, chat_id, game_launch_point, prmode)
    elif level == 4:
        (level, chat_lang, text, kbd, halt, prmode) = InputLang(S, phrase, language, game_id, halt, level, chat_lang, prmode)
    elif level == 5:
        (level, act, text, chattext, kbd, chatkbd, prmode, halt, chatid) = InputSend(S, phrase, language, game_id, halt, level, act, chat_lang, chat_id, chatid)
    else:
        assert(False)
    
    return (level, findchats, direction, chat_id, chat_launch_point, game_launch_point, game_id, chat_lang, chatid, act, text, chattext, kbd, chatkbd, prmode, halt)

def ActiveGames(S: dict[str, str], phrase: str, halt: bool, act: str, language: str, level: int, direction: str, game_launch_point: int, game_id: int, clients_launch_point: int, user_id: int) -> tuple[int, int, int, int, int, str, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    prmode:str = ''

    if level == 2:
        (level, game_id, game_launch_point, text, kbd, halt) = InputActiveGameId(S, phrase, level, halt, game_launch_point, clients_launch_point, language, direction, game_id)
    elif level == 3:
        (level, user_id, clients_launch_point, text, kbd, halt, prmode) = InputUserId(S, phrase, user_id, language, clients_launch_point, halt, level, game_id)
    elif level == 4:
        (level, act, text, kbd, halt, prmode) = InputDelete(S, phrase, user_id, game_id, language, level, act, halt)
    else:
        assert(False)
    
    return (level, game_id, game_launch_point, user_id, clients_launch_point, act, text, kbd, halt, prmode)