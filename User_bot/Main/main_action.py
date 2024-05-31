from User_bot.Main.main_database import ConnectTo as mainConntectTo
from User_bot.Main.main_database import RetainUser as dbRetainUser
from User_bot.Main.main_database import ResetAllInf, FindAllDb, WhoSleep, IsItFirsTime, WhoNeedNotifFirstTime, RecordingTimeNotif, IsItNotFirstTime, WhoNeedNotifNotInTheFirstTime, DeleteRecordOfUser, FindUser, RecallUser, RecognizeExMesID, AddNewMesID
#from User_bot.Main.main_database import FindNamedb, 
from User_bot.Main.main_keyboard import Notif as kbNotif
from User_bot.Main.main_keyboard import WhatHappend, GoTo
#from User_bot.secretdata import host, user, password, db_name
from User_bot.secretdata import phiz_host, phiz_user, phiz_password, phiz_db_name
from User_bot.Welcome.welcome_action import GreetingsToUser, WarningRules, GoToOptions
from User_bot.Welcome.welcome_database import ConnectTo as welcomeConnectTo
from User_bot.Welcome.welcome_keyboard import Registration
#from User_bot.Welcome.welcome_keyboard import Error
from User_bot.Media.media_action import InspectionFileId, FirstQuestion, ChoiceOfDirection, WhatGamesNeedToShow, CreateMediaList, StartLoading, SaveToMediaRep, TryAgainToSave
from User_bot.Media.media_database import ConnectTo as mediaConnectTo
from User_bot.Registration.registration_action import PresentationScheduele, ChooseSeats, ChoosePay, CardPayment, BestWishes
from User_bot.Registration.registration_database import ConnectTo as regConnectTo
from User_bot.Settings.settings_action import TypeOfSetting, ChooseDiractions, SetActions, GameSettings, SetiingsAction, IntermediateAction, ChangePaymethod
from User_bot.Settings.settings_database import ConnectTo as setConnectTo
from User_bot.Settings.settings_keyboard import Languages
from User_bot.ShowSchedule.showschedule_action import CreateAFile
from User_bot.ShowSchedule.showschedule_database import ConnectTo as showConnectTo
from User_bot.Notifications.notifications_action import WhatHeppend, IrreversibleDecision
from User_bot.Notifications.notification_database import ConnectTo as notifConnectTo
from User_bot.language_dictionary import Strings
import language_dictionary_for_all
import used_by_everyone as forall


class User:
#ID
    id:int = -1
    language:str = ''
#Reg to Games
    game_id_reg_to_game:int = -1
    seats_reg_to_game:int = -1
    launch_point_reg_to_game:int = 0
    sport_reg_to_game:str = ''
    payment_reg_to_game:str = ''
#Media
    media_time_interval:str = ''
    media_direction:str = ''
    media_limit:int = -1
    media_launch_point:int = 0
    del_game_game_id:int = -1
    counter_mediagroup:int = -1
    id_mediagroup:str = '0'
#SeeUserRecords
    us_set_lanuch_point:int = 0
    us_set_what_set:str = ''
    us_set_game_id:int = -1
    us_set_act_game:str = ''
    us_set_what_we_will_change:str = ''
    us_set_new_pay:str = ''
#Notif
    notifgameid:int = -1
#Inf For Me
    act:str = ''
    level:int = -1


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
SOMTHING = 111

def DispatchMisstakes(language:str | None, misstake: str) -> tuple[str, object]:

    text:str = ''
    kbd:object = None

    if language:
        if misstake == "content_type":
            text = language_dictionary_for_all.String[language]["uncorrectly_type"]
            kbd = forall.Options(Strings[language]["first_option"], Strings[language]["second_option"], Strings[language]["third_option"], Strings[language]["fourth_option"])
    else:
        text = Strings["en"]["dismislang"]
        kbd = Languages(Strings["en"]["english"], Strings["en"]["rus"], Strings["en"]["turk"], Strings["en"]["main_menu"])
    return text, kbd

def DispatchMedia(id: int, file_id: str, mgid: str, type: str, language:str) -> tuple[str, object, bool, str, list[float], str, list[str], bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    #mainConntectTo(host, user, password, db_name)
    #name:str = FindNamedb(id)
    #if name == '':
    #    text:str = Strings[language]["ups_no_profile"]
    #else:
    #    mainConntectTo(host, user, password, nam*e)
    mainConntectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    u = RetrieveUser(id, language)
    print("id =", id, "file_id =", file_id, "mediagroup_id =", mgid, "type_of_file =", type)
    u.id_mediagroup = mgid
    (u.counter_mediagroup, text, kbd, halt, prmode, address, img, files_id, edit) = InspectionFileId(Strings[u.language], u.media_direction, u.counter_mediagroup, u.level, u.id, file_id, mgid, type)        
    RetainUser(u)
    print("TEXT =", text, "edit =", edit)
    return text, kbd, halt, prmode, address, img, files_id, edit

def DispatchPhrase(id: int, phrase: str, language: str) -> tuple[str, object, bool, str, list[float], str, list[str], list[str], bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    typeoffile:list[str] = []
    name:str = ''
    #mainConntectTo(host, user, password, db_name)
    #name:str = FindNamedb(id)
    #if name == '':
    #    text = language_dictionary_for_all.String[language]["ups_no_profile"]
    #    kbd = Error()
    #else:
    #    mainConntectTo(host, user, password, nam*e)
    mainConntectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    u = RetrieveUser(id, language)
    print('level =', u.level, 'phrase =', phrase, 'action =', u.act, 'u.media_diraction =', u.media_direction)
    if phrase == "Main_Menu" or phrase == "MainMenu" or phrase == "/menu":
        text = language_dictionary_for_all.String[u.language]["main_menu_text"]
        kbd = forall.Options(Strings[u.language]["first_option"], Strings[u.language]["second_option"], Strings[u.language]["third_option"], Strings[u.language]["fourth_option"])
        u.level = OPTIONS
        u.act = "divarication"
    elif phrase == "continue":
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = Continue(u, name)
    elif phrase == "/reset":
        ResetAllInf(u.id)
        text = Strings[u.language]["reset_all"]
        kbd = Registration(Strings[u.language]["reg"])
        u.act = "registration"
        u.level = LEVEL1
    #if phrase in ("en", "ru", "tur") and u.level == START and u.act == "registration":
        #_level_, _act_, u.us_set_lanuch_point, u.language, _us_set_game_id_, prmode, text, kbd, halt, _img_ = SetActions(Strings[phrase], phrase, u.us_set_what_set, u.id, 7, u.us_set_lanuch_point, u.language, u.us_set_game_id, prmode)
    elif u.act == "we decide what to do" and u.level == START:
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = Notification(u, phrase, name)
    elif u.act == "registration":
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = Welcome(u, phrase, name)
    elif u.act == "divarication":
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = Options(u, phrase, name)
    elif u.act == "reg to games":
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = RegToGames(u, phrase, name)
    elif u.act == "see schedule":
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = FromHtmlToJpg(u, name)
    elif u.act == "photos&videos":
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = StartMediaOption(u, phrase, name)
    elif u.act == "user records":
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = SeeUserRecords(u, phrase, name)
    RetainUser(u)
    print("TEXT =", text)
    return text, kbd, halt, prmode, address, img, files_id, typeoffile, edit

def Continue(u: User, name: str) -> tuple[str, object, bool, str, list[float], str, list[str], list[str], bool]:
    message:str = ''
    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    typeoffile:list[str] = []

    if u.level != START:
        u.level = u.level-1
    if u.act == "reg to games":
        if u.level == START:
            message = "Заводи шарманку"
        elif u.level == LEVEL1:
            message = f"{u.game_id_reg_to_game}"
        elif u.level == LEVEL2:
            message = f"{u.seats_reg_to_game}"
        elif u.level == LEVEL3:
            message = u.payment_reg_to_game
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = RegToGames(u, message, name)
    elif u.act == "photos&videos":
        if u.level == START:
            message = "Заводи шарманку"
        elif u.level == LEVEL1:
            message = u.media_direction
        elif u.level == LEVEL2:
            message = u.media_time_interval
        elif u.level == LEVEL3:
            month_str = f"{u.del_game_game_id}"
            message = month_str
        else:
            u.level = NEGATIVE
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = StartMediaOption(u, message, name)
    elif u.act == "user records":
        if u.level == START:
            message = "Заводи шарманку"
        elif u.level == LEVEL1:
            message = u.us_set_what_set
        elif u.level == LEVEL2:
            if u.us_set_what_set == "u.us_set_what_set":
                message = u.language
            elif u.us_set_what_set == "seting regs":
                message = str(u.us_set_game_id)
        elif u.level == LEVEL3:
            message = u.us_set_act_game
        elif u.level == LEVEL4:
            message = u.us_set_what_we_will_change
        elif u.level == LEVEL5:
            message = u.us_set_new_pay
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = SeeUserRecords(u, message, name)
    return (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit)

def Notification(u: User, phrase: str, name: str) -> tuple[str, object, bool, str, list[float], str, list[str], list[str], bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    typeoffile:list[str] = []

    notifConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    if u.level == START:
        u.level, u.act, u.notifgameid, text, kbd, prmode = WhatHeppend(Strings[u.language], u.id)
    elif u.level == LEVEL1:
        u.level, u.act, text, kbd, halt, prmode = IrreversibleDecision(Strings[u.language], u.id, phrase, u.notifgameid)
    return text, kbd, halt, prmode, address, img, files_id, typeoffile, edit

def StartMediaOption(u: User, phrase: str, name: str) -> tuple[str, object, bool, str, list[float], str, list[str], list[str], bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    typeoffile:list[str] = []

    mediaConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    if u.level == START:
        print("u.language =", u.language)
        u.level, u.counter_mediagroup, text, kbd, halt = FirstQuestion(Strings[u.language], u.language, u.level, u.counter_mediagroup, halt)
    elif u.level == LEVEL1:
        u.level, u.media_direction, text, kbd, halt = ChoiceOfDirection(Strings[u.language], phrase, u.media_direction, u.language)
    elif u.level == LEVEL2:
        u.level, u.media_time_interval, u.media_limit, u.media_launch_point, text, kbd, halt = WhatGamesNeedToShow(Strings[u.language], u.media_direction, phrase, u.media_time_interval, 0, u.language)
    elif u.level == LEVEL3:
        if u.media_direction == "viewing":
            u.level, u.act, u.media_launch_point, u.del_game_game_id, text, kbd, halt, files_id, typeoffile = CreateMediaList(Strings[u.language], phrase, u.id, u.media_direction, u.media_time_interval, u.del_game_game_id, u.level, u.language, u.media_launch_point)
        elif u.media_direction == "loading":
            u.level, u.media_launch_point, u.act, u.del_game_game_id, text, kbd, halt = StartLoading(Strings[u.language], u.media_direction, u.media_time_interval, phrase, u.del_game_game_id, u.language, u.media_launch_point)
    elif u.level == LEVEL4:
        u.level, text, kbd, halt, u.counter_mediagroup = SaveToMediaRep(Strings[u.language], u.counter_mediagroup, u.id, phrase, u.del_game_game_id)
    elif u.level == LEVEL5:
        u.level, u.counter_mediagroup, u.act, text, kbd, halt = TryAgainToSave(Strings[u.language], u.id, phrase, u.del_game_game_id, u.counter_mediagroup)
    else:
       u.act = "divarication"
       u.level = OPTIONS
       kbd = forall.Options(Strings[u.language]["first_option"], Strings[u.language]["second_option"], Strings[u.language]["third_option"], Strings[u.language]["fourth_option"])
       text = "К сожалению, продолжить с этого места никак не получится. Возвращаю вас в главное меню."
    return text, kbd, halt, prmode, address, img, files_id, typeoffile, edit

def Options(u: User, phrase: str, name: str) -> tuple[str, object, bool, str, list[float], str, list[str], list[str], bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    typeoffile:list[str] = []

    if phrase == "Reg to games":
        u.level = START
        u.act = "reg to games"
        text, kbd, halt, prmode, address, img, files_id, typeoffile, edit = RegToGames(u, phrase, name)
    elif phrase == "Looking Schedule":
        u.act = "see schedule"
        u.level = START
        text, kbd, halt, prmode, address, img, files_id, typeoffile, edit = FromHtmlToJpg(u, name)
    elif phrase == "Photo&Video":
        u.act = "photos&videos"
        u.level = START
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = StartMediaOption(u, phrase, name)
    elif phrase == "My records":
        u.act = "user records"
        u.level = START
        text, kbd, halt, prmode, address, img, files_id, typeoffile, edit = SeeUserRecords(u, phrase, name)
    else:
        text = Strings[u.language]["cannottunderstend"]
        kbd = forall.Options(Strings[u.language]["first_option"], Strings[u.language]["second_option"], Strings[u.language]["third_option"], Strings[u.language]["fourth_option"])
    return (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit)

def SeeUserRecords(u: User, phrase: str, name: str) -> tuple[str, object, bool, str, list[float], str, list[str], list[str], bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    typeoffile:list[str] = []

    setConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    if u.level == START:
        u.level, text, kbd, halt, prmode, u.act = TypeOfSetting(Strings[u.language], u.id)
    elif u.level == LEVEL1:
        u.level, u.language, u.act, u.us_set_what_set, u.us_set_lanuch_point, text, kbd, halt, prmode = ChooseDiractions(Strings[u.language], phrase, u.id, 7, u.us_set_lanuch_point, u.us_set_what_set, u.language)
    elif u.level == LEVEL2:
        u.level, u.act, u.us_set_lanuch_point, u.language, u.us_set_game_id, prmode, text, kbd, halt, img = SetActions(Strings[u.language], phrase, u.us_set_what_set, u.id, 7, u.us_set_lanuch_point, u.language, u.us_set_game_id, prmode)
    elif u.level == LEVEL3:
        u.level, u.act, u.us_set_act_game, text, kbd, halt, prmode = GameSettings(Strings[u.language], phrase, u.id, u.us_set_game_id, u.us_set_what_set, u.us_set_act_game, u.language, prmode)
    elif u.level == LEVEL4:
        regConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
        u.level, u.us_set_what_we_will_change, text, kbd, halt = SetiingsAction(Strings[u.language], phrase, u.us_set_game_id, u.us_set_act_game, u.id, u.us_set_what_we_will_change, u.language)
    elif u.level == LEVEL5:
        u.level, u.act, u.us_set_new_pay, img, text, kbd, halt = IntermediateAction(Strings[u.language], phrase, u.us_set_game_id, u.id, u.us_set_what_we_will_change, u.us_set_new_pay, u.language)
    elif u.level == LEVEL6:
        u.level, u.act, text, kbd, halt, img = ChangePaymethod(Strings[u.language], phrase, u.us_set_new_pay, u.us_set_game_id, u.id, u.us_set_what_we_will_change, img, u.language)
    return text, kbd, halt, prmode, address, img, files_id, typeoffile, edit

def FromHtmlToJpg(u: User, name: str) -> tuple[str, object, bool, str, list[float], str, list[str], list[str], bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    typeoffile:list[str] = []

    showConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    if u.level == START:
        text, kbd, prmode = CreateAFile(Strings[u.language])

    return text, kbd, halt, prmode, address, img, files_id, typeoffile, edit

def RegToGames(u: User, phrase: str, name: str) -> tuple[str, object, bool, str, list[float], str, list[str], list[str], bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    typeoffile:list[str] = []

    regConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)


    if u.level == START:
        u.launch_point_reg_to_game, u.level, text, kbd, = PresentationScheduele(Strings[u.language], 7, u.launch_point_reg_to_game)
    elif u.level == LEVEL1:
        u.level, u.game_id_reg_to_game, u.launch_point_reg_to_game, text, kbd, halt = ChooseSeats(Strings[u.language], phrase, u.game_id_reg_to_game, 7, u.launch_point_reg_to_game)
    elif u.level == LEVEL2:
        u.level, u.seats_reg_to_game, text, kbd, halt = ChoosePay(Strings[u.language], u.id, phrase, u.game_id_reg_to_game, u.launch_point_reg_to_game, u.seats_reg_to_game, u.language)
    elif u.level == LEVEL3:
        u.level, u.payment_reg_to_game, u.act, u.sport_reg_to_game, text, kbd, halt, prmode, address, img = CardPayment(Strings[u.language], u.game_id_reg_to_game, u.seats_reg_to_game, u.id, phrase, u.sport_reg_to_game, u.payment_reg_to_game, u.language)
    elif u.level == LEVEL4:
        u.level, u.act, text, kbd, prmode, address = BestWishes(Strings[u.language], u.game_id_reg_to_game, u.seats_reg_to_game, u.id, u.sport_reg_to_game, u.payment_reg_to_game)

    return text, kbd, halt, prmode, address, img, files_id, typeoffile, edit


def Welcome(u: User, phrase: str, name: str) -> tuple[str, object, bool, str, list[float], str, list[str], list[str], bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []
    typeoffile:list[str] = []

    welcomeConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

    if u.level == START:
        u.level, text, kbd = GreetingsToUser(Strings[u.language])
    elif u.level == LEVEL1:
        u.level, text, kbd, halt = WarningRules(Strings[u.language], phrase)
    elif u.level == LEVEL2:
        u.level, u.act, text, kbd, halt = GoToOptions(Strings[u.language], u.id, phrase)
    return text, kbd, halt, prmode, address, img, files_id, typeoffile, edit
#end Welcome

def BotCheskWhoSleep() -> tuple[list[str], list[object], list[int], list[int]]:

    text_list:list[str] = []
    keyboards:list[object] = []
    user_ids:list[int] = []
    exmesids:list[int] = []
    list_db_names:list[str] = []
    user_langs:list[str] = []

    mainConntectTo(host, user, password, db_name)
    list_db_names = FindAllDb()
    if list_db_names != []:
        for name in list_db_names:
            mainConntectTo(host,  user, password, name)
            user_ids, exmesids, user_langs = WhoSleep()
            if user_ids != []:
                for id, lang in zip(user_ids, user_langs):
                    print(id)
                    text_list.append(Strings[lang]["donotsleep"])
                    keyboards.append(kbNotif(Strings[lang]["continue"], Strings[lang]["main_menu"]))
    return text_list, keyboards, user_ids, exmesids
    

def WhoNeedNotification() -> tuple[list[str], list[object], list[int], list[int]]:

    text_list:list[str] = []
    keyboards:list[object] = []
    counternotifs:list[int] = []
    user_ids:list[int] = []
    exmessids:list[int] = []
    gameids:list[int] = []
    list_db_names:list[str] = []
    howmuthusesneednotif:int = -1
    user_language:list[str] = []

    mainConntectTo(host, user, password, db_name)
    list_db_names = FindAllDb()
    if list_db_names != []:
        for name in list_db_names:
            mainConntectTo(host, user, password, name)
            howmuthusesneednotif = IsItFirsTime()
            if howmuthusesneednotif > 0:
                user_ids, exmessids, gameids, user_language = WhoNeedNotifFirstTime()
                if user_ids != []:
                    for id, gid, lang in zip(user_ids, gameids, user_language):
                        text_list.append(Strings[lang]["press_the_button"])
                        keyboards.append(WhatHappend(Strings[lang]["what_hap"]))
                        RecordingTimeNotif(id, gid)
            elif IsItNotFirstTime() > 0:
                user_ids, exmessids, gameids, counternotifs, user_language = WhoNeedNotifNotInTheFirstTime()
                if user_ids != []:
                    for counter, id, gid, lang in zip(counternotifs, user_ids, gameids, user_language):
                        if counter < 6:
                            text_list.append(Strings[lang]["press_the_button_again"])
                            keyboards.append(WhatHappend(Strings[lang]["what_hap"]))
                            RecordingTimeNotif(id, gid)
                        else:
                            text_list.append(Strings[lang]["goodbuy"])
                            keyboards.append(GoTo(Strings[lang]["main_menu"]))
                            DeleteRecordOfUser(id, gid)
    return text_list, keyboards, user_ids, exmessids

def RetrieveUser(uid: int, ad_lang: str) -> User:
#ID    
    u = User()
    u.id = uid

    if FindUser(uid, ad_lang):
        (u.id, 
        u.language,
        u.game_id_reg_to_game, u.launch_point_reg_to_game, u.sport_reg_to_game, u.seats_reg_to_game, u.payment_reg_to_game,
        u.media_time_interval, u.media_direction, u.media_limit,  u.media_launch_point, u.del_game_game_id, u.id_mediagroup,
        u.counter_mediagroup,
        u.us_set_lanuch_point, u.us_set_what_set, u.us_set_game_id, u.us_set_act_game, u.us_set_what_we_will_change, u.us_set_new_pay,
        u.notifgameid,
        u.act, u.level) = RecallUser(uid, 
                                            u.language,
                                            u.game_id_reg_to_game, u.launch_point_reg_to_game, u.sport_reg_to_game, u.seats_reg_to_game, u.payment_reg_to_game,
                                            u.media_time_interval, u.media_direction, u.media_limit,  u.media_launch_point, u.del_game_game_id, u.id_mediagroup,
                                            u.counter_mediagroup,
                                            u.us_set_lanuch_point, u.us_set_what_set, u.us_set_game_id, u.us_set_act_game, u.us_set_what_we_will_change, u.us_set_new_pay,
                                            u.notifgameid,
                                            u.act, u.level)
    else:
        u.level = START
        u.act = 'registration'
        u.language = ad_lang
    return u

def RetainUser(u: User):
    dbRetainUser(u.id, 
                            u.language,
                            u.game_id_reg_to_game, u.launch_point_reg_to_game, u.sport_reg_to_game, u.seats_reg_to_game, u.payment_reg_to_game,
                            u.media_time_interval, u.media_direction, u.media_limit,  u.media_launch_point, u.del_game_game_id, u.id_mediagroup,
                            u.counter_mediagroup,
                            u.us_set_lanuch_point, u.us_set_what_set, u.us_set_game_id, u.us_set_act_game, u.us_set_what_we_will_change, u.us_set_new_pay,
                            u.notifgameid,
                            u.act, u.level)

def EvPrevMsgId(uid: int, name: str, lname: str, usname: str, language: str) -> tuple[int, str]:
    mes_id, action = RecognizeExMesID(uid, name, lname, usname, language)
    return mes_id, action

def RetainPrevMsgId(uid: int, m_id: int, mgid: str):
    AddNewMesID(uid, m_id, mgid)