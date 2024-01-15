from Admin_bot.Main.main_database import FindAdmin, RecallAdmin, SelectDataFromSchedule, Reupdate, ReupdateGames, ReupdateClients, ReupdateActivities, ReupdateFinances, ChatsInfo, FindChats, AddNewChat, FindGameIds, RegistrtionClientToGame, SelectChatLang, InfUpdate
from Admin_bot.Main.main_database import ConnectTo as mainConnectTo
#from Admin_bot.Main.main_database import FindNamedb
from Admin_bot.Main.main_database import RetainAdmin as databaseRetainAdmin
#from Admin_bot.secretdata import host, user, password, db_name
from Admin_bot.secretdata import phiz_host, phiz_user, phiz_password, phiz_db_name
from Admin_bot.language_dictoinary import String
from Admin_bot.Welcome.welcome_action import FirstMessage, EnterPassword, ShowRules
from Admin_bot.Welcome.welcome_database import ConnectTo as welcConnectTo
from Admin_bot.Game.game_database import ConnectTo as gameConnectTo
from Admin_bot.Game.game_action import ChooseDiraction, DirectionsOfDirection, ChangeGame, DeleteGame, CreateGame
from Admin_bot.Clients.clients_action import ChooseClientDirection, ShowClientsByDirection, HeadFuncOfCreate, HeadFuncOfChange, HeadFuncOfDelete, HeadFuncOfRegToGame
from Admin_bot.Clients.clients_database import ConnectTo as clConnectTo
from Admin_bot.Activities.activities_action import ChooseActivitiesDirection, ChatGame, ActiveGames
from Admin_bot.Activities.activities_action import StartAct as actStartAct
from Admin_bot.Activities.activities_database import ConnectTo as actConnectTo
from Admin_bot.Activities.activities_database import SelectAllInfFromSchedule, SelectYourClients
from Admin_bot.Activities.activities_keyboard import LetsGO
from Admin_bot.Money.money_database import ConnectTo as moneyConnectTo
from Admin_bot.Money.money_action import ChooseMoneyDirection, HeadOfPaid
from Admin_bot.Money.money_action import StartAct as moneyStartAct
from Admin_bot.Settings.settings_action import ChooseSettingDirection, StartSettings, HeadFuncOfChangeLanguages
from Admin_bot.Settings.settings_database import ConnectTo as setConnectTo
import language_dictionary_for_all
import used_by_everyone as forall

NEGATIVE = -1
START = 0
LEVEL1 = 1
LEVEL2 = 2
LEVEL3 = 3
OPTIONS = 3
LEVEL4 = 4
LEVEL5 = 5
LEVEL6 = 6
LEVEL7 = 7
LEVEL8 = 8
LEVEL9 = 9
LEVEL10 = 10

class Admin:
    id:int = -1

    name:str = ''
    last_name:str = ''
    language:str = ''

    act:str = ''
    direction:str = ''

    class Game:

        launch_point:int = 0
        sport:str = ''
        date:int = -1
        time:int = -1
        seats:int = -1
        price:int = -1
        currency:str = ''
        latitude:float = -1
        longitude:float = -1
        nameaddress:str = ''
        change_direction:str = ''
        game_id:int = -1
        change_create:bool = False
        typeofchange:str = ''


    class Clients:
        fromwhere:str = ''
        name:str = ''
        last_name:str = ''
        phonenum:int = -1
        user_id:int = -1
        change_option:str = ''
        launch_point:int = 0
        changeddata_str:str = '' 
        changeddata_int:int = -1
        game_id:int = -1
        seats:int = -1
        paymethod:str = ''

    class Activities:
        actwithchats:str = ''
        launch_point:int = 0
        chat_id:int = -1
        game_id:int = -1
        chat_language:str = ''

    class Finances:
        user_id:int = -1

    class Settings:
        pass

    level:int = -1


def RetrieveAdmin(id: int, ad_lang: str) -> Admin:
    a = Admin()
    a.id = id

    if FindAdmin(id, ad_lang):
        (a.id, a.name, a.last_name, a.language, a.act, a.direction,
        a.Game.launch_point, a.Game.sport, a.Game.date, a.Game.time, a.Game.seats, a.Game.price, a.Game.currency, a.Game.latitude, a.Game.longitude, a.Game.nameaddress, a.Game.change_direction, a.Game.game_id, a.Game.change_create, a.Game.typeofchange,
        a.Clients.fromwhere, a.Clients.name, a.Clients.last_name, a.Clients.phonenum, a.Clients.user_id, a.Clients.change_option, a.Clients.launch_point, a.Clients.changeddata_str, a.Clients.changeddata_int, a.Clients.game_id, a.Clients.seats, a.Clients.paymethod,
        a.Activities.actwithchats, a.Activities.launch_point, a.Activities.chat_id, a.Activities.game_id, a.Activities.chat_language,
        a.Finances.user_id,
        a.level) = RecallAdmin(a.id, a.name, a.last_name, a.language, a.act, a.direction,
                                            a.Game.launch_point, a.Game.sport, a.Game.date, a.Game.time, a.Game.seats, a.Game.price, a.Game.currency, a.Game.latitude, a.Game.longitude, a.Game.nameaddress, a.Game.change_direction, a.Game.game_id, a.Game.change_create, a.Game.typeofchange,
                                            a.Clients.fromwhere, a.Clients.name, a.Clients.last_name, a.Clients.phonenum, a.Clients.user_id, a.Clients.change_option, a.Clients.launch_point, a.Clients.changeddata_str, a.Clients.changeddata_int, a.Clients.game_id, a.Clients.seats, a.Clients.paymethod,
                                            a.Activities.actwithchats, a.Activities.launch_point, a.Activities.chat_id, a.Activities.game_id, a.Activities.chat_language,
                                            a.Finances.user_id,
                                            a.level)
    else:
        a.level = START
        a.act = 'registration'
        a.language = ad_lang

    return a

def RetainAdmin(a: Admin):
    databaseRetainAdmin(a.id, a.name, a.last_name, a.language, a.act, a.direction,
    a.Game.launch_point, a.Game.sport, a.Game.date, a.Game.time, a.Game.seats, a.Game.price, a.Game.currency, a.Game.latitude, a.Game.longitude, a.Game.nameaddress, a.Game.change_direction, a.Game.game_id, a.Game.change_create, a.Game.typeofchange,
    a.Clients.fromwhere, a.Clients.name, a.Clients.last_name, a.Clients.phonenum, a.Clients.user_id, a.Clients.change_option, a.Clients.launch_point, a.Clients.changeddata_str, a.Clients.changeddata_int, a.Clients.game_id, a.Clients.seats, a.Clients.paymethod,
    a.Activities.actwithchats, a.Activities.launch_point, a.Activities.chat_id, a.Activities.game_id, a.Activities.chat_language,
    a.Finances.user_id,
    a.level)
    
def DataForChange(a: Admin):
    if a.Game.game_id and a.Game.game_id != -1:
        a.Game.sport, a.Game.date, a.Game.time, a.Game.seats, a.Game.price, a.Game.currency, a.Game.latitude, a.Game.longitude, a.Game.nameaddress = SelectDataFromSchedule(a.Game.game_id)

def Welocme(a: Admin, phrase: str, name: str) -> tuple[str, object, bool, str, bool]:

    welcConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    text:str = ''
    kbd:object = None
    prmode:str = ''
    halt:bool = False
    fixed:bool = False

    if a.level == START:
        a.level, text, kbd = FirstMessage(String[a.language])
    elif a.level == LEVEL1:
        a.level, text, kbd, halt = EnterPassword(String[a.language], phrase, a.level)
    elif a.level == LEVEL2 or a.level == LEVEL3:
        a.level, text, kbd, prmode, fixed, halt = ShowRules(String[a.language], phrase, a.level, a.language, a.id)
    
    return (text, kbd, halt, prmode, fixed)

def Games(a: Admin, phrase: str, name: str) -> tuple[str, object, bool, str]:

    gameConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    text:str = ''
    kbd:object = None
    prmode:str = ''
    halt:bool = False


    if a.direction not in ("create games", "change games", "delete games"):
        if a.level == 0:
            (a.level, text, kbd) = ChooseDiraction(String[a.language])
        elif a.level == 1:
            (a.level, a.direction, text, kbd, halt) = DirectionsOfDirection(String[a.language], phrase, a.level, a.language, a.direction, a.Game.launch_point)
        else:
            assert(False)
    else:
        if a.direction == "create games":
            (a.level, a.direction, a.act, text, kbd, halt, prmode, a.Game.sport, a.Game.date, a.Game.time, a.Game.seats, a.Game.price, a.Game.currency, a.Game.latitude, a.Game.longitude, a.Game.nameaddress, a.Game.change_create) = CreateGame(String[a.language], phrase, a.level, a.direction, a.act, a.id, a.Game.sport, a.Game.date, a.Game.time, a.Game.seats, a.Game.price, a.Game.currency, a.Game.latitude, a.Game.longitude, a.Game.nameaddress, a.language, a.Game.change_create)
        elif a.direction == "change games":
            DataForChange(a)
            (a.level, a.Game.launch_point, a.Game.game_id, a.Game.change_direction, a.Game.typeofchange, text, kbd, halt, prmode) = ChangeGame(String[a.language], a.level, a.Game.change_direction, a.Game.game_id, phrase, a.Game.sport, a.Game.date, a.Game.time, a.Game.seats, a.Game.price, a.Game.currency, a.Game.latitude, a.Game.longitude, a.Game.nameaddress, a.language, a.direction, a.Game.launch_point, a.Game.typeofchange)
        elif a.direction == "delete games":
            (a.level, a.Game.launch_point, a.direction, text, kbd, halt, prmode) = DeleteGame(String[a.language], phrase, a.language, a.direction, a.Game.launch_point, a.level)
        else:
            assert(False)

    return (text, kbd, halt, prmode)

def Clients(a: Admin, phrase: str, name: str) -> tuple[str, object, bool, str]:

    clConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    gameConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''

    if a.direction not in ("create client", "change client", "delete client", "reg client to game"):
        if a.level == 0:
            (a.level, text, kbd) = ChooseClientDirection(String[a.language], a.language)
        elif a.level == 1:
            (a.level, a.act, a.direction, text, kbd, halt) = ShowClientsByDirection(String[a.language], phrase, a.language, a.direction, a.level, a.act, a.Clients.launch_point)
        else:
            assert(False)
    else:
        if a.direction  == "create client":
            (a.level, a.act, a.Clients.fromwhere, a.Clients.name, a.Clients.last_name, a.Clients.phonenum, text, kbd, halt, prmode) = HeadFuncOfCreate(String[a.language], phrase, a.language, a.level, a.act, a.direction, a.Clients.fromwhere, a.Clients.name, a.Clients.last_name, a.Clients.phonenum, halt, a.id)
        elif a.direction == "change client":
            (a.level, a.Clients.launch_point, a.Clients.user_id, a.direction, a.Clients.change_option, a.Clients.changeddata_str, a.Clients.changeddata_int, prmode, text, kbd, halt) = HeadFuncOfChange(String[a.language], phrase, a.language, a.level, a.Clients.user_id, a.Clients.change_option, a.Clients.changeddata_str, a.Clients.changeddata_int, halt, a.direction, a.Clients.launch_point)
        elif a.direction == "delete client":
            (a.level, a.Clients.launch_point, a.act, text, kbd, halt) = HeadFuncOfDelete(String[a.language], phrase, a.level, a.direction, a.language, a.Clients.launch_point, a.act, halt)
        elif a.direction == "reg client to game":
            (a.level, a.Clients.launch_point, a.Game.launch_point, a.act, a.Clients.user_id, a.Clients.game_id, a.Clients.seats, a.Clients.paymethod, text, kbd, halt) = HeadFuncOfRegToGame(String[a.language], phrase, a.level, a.language, a.Game.launch_point, a.Clients.launch_point, a.direction, a.Clients.user_id, a.Clients.game_id, a.Clients.seats, a.Clients.paymethod, halt, a.act)

    return text, kbd, halt, prmode

def Activities(a: Admin, phrase: str, name: str) -> tuple[str, str, object, object, str, bool, bool, int]:

    gameConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    actConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    clConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    text:str = ''
    chattext:str = ''
    kbd:object = None
    chatkbd:object = None
    halt:bool = False
    findchats:bool = False
    prmode:str = ''
    chatid:int = -1

    if a.direction not in ("create game", "active games"):
        if a.level == 0:
            a.level, text, kbd = ChooseActivitiesDirection(String[a.language], a.language)
        elif a.level == 1:
            a.level, a.direction, text, kbd, halt = actStartAct(String[a.language], phrase, a.direction, halt, a.language, a.level, 0)
        else:
            assert(False)
    else:
        if a.direction == "create game":
            (a.level, findchats, a.direction, a.Activities.chat_id, a.Activities.launch_point, a.Game.launch_point, a.Activities.game_id, a.Activities.chat_language, chatid, a.act, text, chattext, kbd, chatkbd, prmode, halt) = ChatGame(String[a.language], phrase, a.level, findchats, a.language, a.direction, a.Game.launch_point, a.Activities.launch_point, a.Activities.chat_language, a.Activities.chat_id, a.Activities.game_id, a.act, chatid)
        elif a.direction == "active games":
            (a.level, a.Activities.game_id, a.Game.launch_point, a.Clients.user_id, a.Clients.launch_point, a.act, text, kbd, halt, prmode) = ActiveGames(String[a.language], phrase, halt, a.act, a.language, a.level, a.direction, a.Game.launch_point, a.Activities.game_id, a.Clients.launch_point, a.Clients.user_id)
        else:
            assert(False)
    return (text, chattext, kbd, chatkbd, prmode, halt, findchats, chatid)

def Money(a: Admin, phrase: str, name: str) -> tuple[str, object, bool, str]:

    moneyConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    clConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    text:str = ''
    kbd:object = None
    prmode:str = ''
    halt:bool = False

    if a.direction not in ("paid action", "see stat"):
        if a.level == 0:
            (a.level, text, kbd) = ChooseMoneyDirection(String[a.language], a.language)
        elif a.level == 1:
            (a.level, a.direction, a.act, text, kbd, halt, prmode) = moneyStartAct(String[a.language], phrase, a.language, a.level, a.Clients.launch_point, a.act, a.direction, halt, prmode)
        else:
            assert(False)
    else:
        if a.direction == "paid action":
            (a.level, a.Finances.user_id, a.Clients.launch_point, a.Game.launch_point, a.act, text, kbd, halt, prmode) = HeadOfPaid(String[a.language], phrase, a.language, a.level, a.direction, a.Finances.user_id, a.Clients.launch_point, a.Game.launch_point, a.act, halt)
        elif a.direction == "see stat":
            (a.level, a.direction, a.act, text, kbd, halt, prmode) = moneyStartAct(String[a.language], a.direction, a.language, a.level, a.Clients.launch_point, a.act, a.direction, halt, prmode)
        else:
            assert(False)
    return (text, kbd, halt, prmode)

def Settings(a: Admin, phrase: str, name: str) -> tuple[str, object, bool]:

    setConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    text:str = ''
    kbd:object = None
    halt:bool = False

    if a.direction not in ("change language", "!free space!"):
        if a.level == 0:
            (a.level, text, kbd) = ChooseSettingDirection(String[a.language], a.language)
        elif a.level == 1:
            (a.level, a.direction, text, kbd, halt) = StartSettings(String[a.language], phrase, a.level, a.language, a.direction, halt)
    else:
        if a.direction == "change language":
            (a.level, a.act, a.language, text, kbd, halt) = HeadFuncOfChangeLanguages(String[a.language], phrase, a.level, a.language, a.act, halt, a.id, a.direction)
    return (text, kbd, halt)

def OptionsOfAdmin(a: Admin, phrase: str, name: str) -> tuple[str, str, object, object, str, bool, bool, int]:
    text:str = ''
    chattext:str = ''
    kbd:object = None
    chatkbd:object = None
    halt:bool = False
    prmode:str = ''
    findchats:bool = False
    chatid:int = -1

    a.level = START
    Reupdate(a.id)
    a.direction = ''

    if phrase == "Games":
        ReupdateGames(a.id)
        a.act = 'game'
        (text, kbd, halt, prmode) = Games(a, phrase, name)
    elif phrase == "Clients":
        ReupdateClients(a.id)
        a.act = 'clients'
        (text, kbd, halt, prmode) = Clients(a, phrase, name)
    elif phrase == "Activity":
        ReupdateActivities(a.id)
        a.act = 'activities'
        (text, chattext, kbd, chatkbd, prmode, halt, findchats, chatid) = Activities(a, phrase, name)
    elif phrase == "Finances":
        ReupdateFinances(a.id)
        a.act = 'money'
        (text, kbd, halt, prmode) = Money(a, phrase, name)
    elif phrase == "Settings":
        a.act = 'settings'
        (text, kbd, halt) = Settings(a, phrase, name)

    return (text, chattext, kbd, chatkbd, prmode, halt, findchats, chatid)
        
def GetChatIds(chatinf:list[tuple[int, str]], aid: int):
    ChatsInfo(chatinf, aid)

def DispatchPhrase(id: int, phrase: str, language: str) -> tuple[str, str, object, object, str, bool, str, bool, bool, int]:

    text:str = ''
    chattext:str = ''
    kbd:object = None
    chatkbd:object = None
    prmode:str = ''
    halt:bool = False
    spreadsheet:str = ''
    fixed:bool = False
    findchats:bool = False
    chatid:int = -1
    name:str = ''

    #mainConnectTo(host, user, password, db_name)
    #name:str = FindNamedb(id)
    #if name == '':
        #text:str = language_dictionary_for_all.String[language]["ups_no_profile"]
    #else:
        #mainConnectTo(host, user, password, name)
    mainConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    a:Admin = RetrieveAdmin(id, language)
    print("a.id =", id, "phrase =", phrase, "a.level =", a.level, "a.act =", a.act)

    if phrase == "Main_Menu":
        text = language_dictionary_for_all.String[a.language]["main_menu_text"]
        kbd = forall.OptionsAdmin(String[a.language]["first_option"], String[a.language]["second_option"], String[a.language]["third_option"], String[a.language]["fourth_option"], String[a.language]["fifth_option"])
        a.act = "divarication"
        a.level = OPTIONS
    elif a.act == "registration":
        (text, kbd, halt, prmode, fixed) = Welocme(a, phrase, name)
    elif a.act == "game":
        (text, kbd, halt, prmode) = Games(a, phrase, name)
    elif a.act == "clients":
        (text, kbd, halt, prmode) = Clients(a, phrase, name)
    elif a.act == "activities":
        (text, chattext, kbd, chatkbd, prmode, halt, findchats, chatid) = Activities(a, phrase, name)
    elif a.act == "money":
        (text, kbd, halt, prmode) = Money(a, phrase, name)
    elif a.act == "settings":
        (text, kbd, halt) = Settings(a, phrase, name)
    elif a.act == "divarication":
        (text, chattext, kbd, chatkbd, prmode, halt, findchats, chatid) = OptionsOfAdmin(a, phrase, name)

    RetainAdmin(a)
    print("TEXT =", text)
    return (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid)

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

def DispatchGroups(chatid: int, id: int, phrase: str, chatname: str) -> tuple[str, object, int, str]:
    chattext:str = ''
    chatkbd:object = ''
    exmess:int = -1
    prmode:str = ''
    users:list[tuple[str, str]] = []
    #mainConnectTo(host, user, password, db_name)
    #name:str = FindNamedb(id)
    #if name == '':
    #    pass
    #else:
        #mainConnectTo(host, user, password, name)
    mainConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    actConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    print("chatid =", chatid, "id =", id, "phrase =", phrase, "chatname =", chatname)
    if phrase == "/add":
        if not FindChats(chatid):
            AddNewChat(chatid, chatname)
    elif forall.IntCheck(phrase):
        if FindGameIds(int(phrase)):
            RegistrtionClientToGame(int(phrase), id)
            chatlang, exmess = SelectChatLang(chatid)
            sport, date, time, seats, price, currency, lat, long, nameaddress = SelectAllInfFromSchedule(int(phrase))
            users_from_db = SelectYourClients((int(phrase)))
            for name, lastname in users_from_db:
                if name == "no_data":
                    name = language_dictionary_for_all.String[chatlang]["no_data"]
                if lastname == "no_data":
                    lastname = language_dictionary_for_all.String[chatlang]["no_data"]
                users.append((name, lastname))
            chattext = String[chatlang]["start_chatgame"] + String[chatlang]["sport+date+time+seats+price+currency+link+nameaddress"] % (language_dictionary_for_all.String[chatlang][sport], forall.CreateDateStr(date), forall.CreateTimeStr(time), seats, price, currency, lat, long, nameaddress) + (StrSeats(seats, String[chatlang], users))
            chatkbd = LetsGO(String[chatlang]["participate"], int(phrase))
            prmode = "HTML"
    return (chattext, chatkbd, exmess, prmode)


def UpdateExMessageId(message_id: int, id: int):
    UpdateExMessageId(message_id, id)

def UpdateExMessageFromChat(message_id: int, chat_id: int):
    UpdateExMessageFromChat(message_id, chat_id)

def EvPrevMsgId(admin_id: int, name: str, last_name: str, username: str, language: str) -> int:
    exmess:int = InfUpdate(admin_id, name, last_name, username, language)
    return exmess