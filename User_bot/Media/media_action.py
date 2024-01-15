from User_bot.Media.media_database import FindSomeGames, FindSomeMedia, FoundSomePhotosInLastGamesSchedule, FoundSomeverInLastGamesSchedule, FoundSomePhotosInSchedule, FoundSomeverInSchedule, CreateListOfViewGamesForLastGames, CreateListOfViewGames
from User_bot.Media.media_database import CreateListOfLoadGamesForLastGames, CreateListOfLoadGames, CheckGameId, SelectMediaDelGame, CoutFreeSeatsOfFile, SaveToDatabase, TryAgainSaveToDatbase, UpdateMediaGroup
from User_bot.Media.media_keyboard import DirectionBouth, DirectionOnce, TimeInterval, OneTimeInterval, GoTo, TryAgain, EndMediaGroup
import used_by_everyone as forall
import language_dictionary_for_all

#Main Actions
def FirstQuestion(S: dict[str, str], language: str, level: int, counter_mediagroup: int, halt:bool) -> tuple[int, int, str, object, bool]:
    text:str = ''
    kbd:object = None
    print("LANGUAGE", language)

    if FindSomeGames():
        halt = True
        level = 1
        counter_mediagroup = 0
        text = S["direction"]
        if FindSomeMedia():
            kbd = DirectionBouth(S["kbload"], S["kbview"], language_dictionary_for_all.String[language]["main_menu_kb"])
        else:
            kbd = DirectionOnce(S["kbload"], language_dictionary_for_all.String[language]["main_menu_kb"])
    else:
        level = 3
        text = S["nothing_there"] + language_dictionary_for_all.String[language]["main_menu_text"]
        kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
    return (level, counter_mediagroup, text, kbd, halt)

def ChoiceOfDirection(S: dict[str, str], phrase: str, media_direction: str, language: str) -> tuple[int, str, str, object, bool]:

    halt:bool = False
    text:str = ''
    text2:str = ''
    kbd:object = None
    level:int = -1
    _counter_mediagroup_:int = -1
    _halt_:bool = False
    
    if phrase in ("viewing", "loading"):
        halt = True
        media_direction = phrase
        level = 2

        if (FoundSomePhotosInLastGamesSchedule()) and (FoundSomeverInLastGamesSchedule()):
            text = S["time"]
            kbd = TimeInterval(S["kblastgames"], S["kball_of_rest"])
        else:
            if (phrase == "viewing") and (not FoundSomePhotosInLastGamesSchedule()) and (not FoundSomePhotosInSchedule()):
                text = S["nothing_to_watch"]
                (level, _counter_mediagroup_, text2, kbd, _halt_) = FirstQuestion(S, language, level, _counter_mediagroup_, _halt_)
                text += text2
            elif (phrase == "loading") and (not FoundSomeverInLastGamesSchedule()) and (not FoundSomeverInSchedule()):
                text = S["nothing_to_load"]
                (level, _counter_mediagroup_, text2, kbd, _halt_) = FirstQuestion(S, language, level, _counter_mediagroup_, _halt_)
                text += text2
            else:
                text = S["time"]
                kbd = OneTimeInterval(S["kball_of_rest"])
    else:
        level, _counter_mediagroup_, text, kbd, _halt_ = FirstQuestion(S, language, level, _counter_mediagroup_, _halt_)
    return level, media_direction, text, kbd, halt

def ShowGamesWithPhoto(language: str, media_limit: int, launch_point: int, interval: str, media_direction: str) -> tuple[int, int, object]:

    schedule:list[tuple[str, ...]] = []
    kbd:object = None #list
    level:int = -1 #int
    schedule_from_db:list[tuple[int, str, int, int]] = []
    length:int = -1

    if media_direction == "viewing":
        if interval == "last_games":
            schedule_from_db, length = CreateListOfViewGamesForLastGames(media_limit, launch_point)
        else:
            schedule_from_db, length = CreateListOfViewGames(media_limit, launch_point)
    else:
        if interval == "last_games":
            schedule_from_db, length = CreateListOfLoadGamesForLastGames(media_limit, launch_point)
        else:
            schedule_from_db, length = CreateListOfLoadGames(media_limit, launch_point)
    _trash_, schedule = forall.SheduleStr([], schedule_from_db, language)
    kbd = forall.Schedule(schedule, media_limit, launch_point, '', length)
    level = 3

    return level, media_limit, kbd

def WhatGamesNeedToShow(S: dict[str, str], media_direction: str, phrase: str, media_time_interval: str, launch_point: int, language: str) -> tuple[int, str, int, int, str, object, bool]:

    halt:bool = False
    text:str = ''
    kbd:object = None
    level:int = -1 #int
    __:str = '' #str
    _language_:str = ''
    media_limit:int = -1 #int
    _halt_:bool = False

    if phrase in ("last_games", "all_games"):
        halt = True
        media_time_interval = phrase
        media_limit = 7
        level, media_limit, kbd = ShowGamesWithPhoto(language, media_limit, launch_point, media_time_interval, media_direction)
        text = S[media_time_interval]
    else:
        level, __, text, kbd, _halt_ = ChoiceOfDirection(S, media_direction, media_direction, _language_)
    print("launch_point in WhatGamesNeedToShow =", launch_point)
    return level, media_time_interval, media_limit, launch_point, text, kbd, halt

def NextPageGames(S: dict[str, str], launch_point: int, media_time_interval: str, language: str, media_direction: str) -> tuple[int, int, str, object]:

    text:str = '' #str
    kbd:object = None #list
    level:int = -1 #int
    media_limit:int = 7 #int
    launch_point += 7
    level, media_limit, kbd = ShowGamesWithPhoto(language, media_limit, launch_point, media_time_interval, media_direction)
    text = S[media_time_interval]

    return level, launch_point, text, kbd


def CreateMediaList(S: dict[str, str], phrase: str, uid: int, media_direction: str, media_time_interval: str, game_id: int, level: int, language: str, launch_point: int) -> tuple[int, str, int, int, str, object, bool, list[str], list[str]]:

    halt:bool = False
    __:int = -1
    _media_time_interval_:str = ''
    _media_limit_:int = -1
    _halt_:bool = False
    files_id:list[str] = []
    typesoffiles:list[str] = []
    text:str = ''
    kbd:object = None

    act:str = "photos&videos"
    
    if forall.IntCheck(phrase):
        halt = True
        if CheckGameId(int(phrase)):
            game_id = int(phrase)
            files_id, typesoffiles = SelectMediaDelGame(uid)
            if files_id != []:
                text = S["all_media"]
                kbd = GoTo(S["main_menu"])
            else:
                text = S["its_not_time_yet"]
                kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
                act = "divarication"
                level = 4
        else:
            level, _media_time_interval_, _media_limit_, launch_point, text, kbd, _halt_ =  WhatGamesNeedToShow(S, media_direction, media_time_interval, _media_time_interval_, launch_point, language)
    else:
        if phrase == "next page":
            launch_point += 7
        elif phrase == "previous page":
            launch_point += -7
        level, _media_time_interval_, _media_limit_, launch_point, text, kbd, _halt_ =  WhatGamesNeedToShow(S, media_direction, media_time_interval, _media_time_interval_, launch_point, language)
    return level, act, launch_point, game_id, text, kbd, halt, files_id, typesoffiles

def StartLoading(S: dict[str, str], media_direction: str, media_time_interval: str, phrase: str, game_id: int, language: str, launch_point: int) -> tuple[int, int, str, int, str, object, bool]:

    halt:bool = False #bool
    filesseats:int = -1 #int
    freefilesseats:int = -1 #int
    text:str = '' #str
    kbd:object = None #list
    level:int = -1 #int
    _media_time_interval_:str = ''
    _media_limit_:int = -1
    _halt_:bool = False
    _launch_point_:int = -1

    act = "photos&videos"

    if forall.IntCheck(phrase):
        if CheckGameId(int(phrase)):
            halt = True
            game_id = int(phrase)
            filesseats = CoutFreeSeatsOfFile(game_id)
            if filesseats != 20:
                freefilesseats = 20 - filesseats
                text = S["Can_downloaded"] % (freefilesseats)
                kbd = GoTo(S["main_menu"])
                level = 4
            else:
                text = S["cant_download"]
                kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
                level = 3
                act = "divarication"
        else:
            level, _media_time_interval_, _media_limit_, launch_point, text, kbd, _halt_ =  WhatGamesNeedToShow(S, media_direction, media_time_interval, media_time_interval, launch_point, language)
    else:
        if phrase == "next page":
            launch_point += 7
        elif phrase == "previous page":
            launch_point += -7
        level, _media_time_interval_, _media_limit_, launch_point, text, kbd, _halt_ =  WhatGamesNeedToShow(S, media_direction, media_time_interval, media_time_interval, launch_point, language)
    return level, launch_point, act, game_id, text, kbd, halt



def SaveToMediaRep(S: dict[str, str], counter_mediagroup: int, uid: int, phrase: str, game_id: int) -> tuple[int, str, object, bool, int]:

    halt:bool = False
    text:str = ''
    kbd:object = None
    level:int = -1
    freespace:int = -1
    
    if phrase == "END":
        freespace, halt, counter_mediagroup = SaveToDatabase(counter_mediagroup, game_id, uid)
        if halt:
            text = S["grac_to_download"] % (counter_mediagroup)
            kbd = GoTo(S["main_menu"])
        else:
            if freespace == 0:
                text = S["no_data"]
                kbd = GoTo(S["main_menu"])
            else:
                text = S["somthingwrong"] % (counter_mediagroup, freespace, freespace)
                kbd = TryAgain(S["all_good"], S["not_all_good"])
                level = 5
    else:
        text = S["pleese_ckick_to_button"]
        kbd = EndMediaGroup(S["all_loaded"])
    return level, text, kbd, halt, counter_mediagroup

def TryAgainToSave(S: dict[str, str], uid: int, phrase: str, game_id: int, loadedmedia: int) -> tuple[int, int, str, str, object, bool]:

    halt:bool = False
    text:str = ''
    kbd:object = None
    level:int = -1
    act:str = "photos&videos"

    if phrase == "try again":
        halt, loadedmedia =  TryAgainSaveToDatbase(uid, game_id)
        if halt:
            text = S["success"] % (loadedmedia)
        else:
            text = S["wrong_again"]
        kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
        level = 3
        act = "divarication"
    else:
        text = S["not_completely"]
        kbd = TryAgain(S["all_good"], S["not_all_good"])
    return level, loadedmedia, act, text, kbd, halt

def SaveToUser(S: dict[str, str], uid: int, file_id: str, mgid: str, type: str, counter: int) -> tuple[int, str, object, bool, bool]:
    
    edit:bool = False
    halt:bool = False
    text:str = ''
    kbd:object = None

    halt, counter = UpdateMediaGroup(mgid, file_id, uid, type)
    if halt:
        text = S["loading_in_progress"] % (counter)
        kbd = EndMediaGroup(S["all_loaded"])
        if counter > 1:
            edit = True
    else:
        text = S["violation"]
        kbd = GoTo(S["main_menu"])
    return counter, text, kbd, halt, edit

def InspectionFileId(S: dict[str, str], media_direction: str, counter_mediagroup: int, level: int, uid: int, file_id: str, mgid: str, type: str) -> tuple[int, str, object, bool, str, list[float], str, list[str], bool]:
    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    edit:bool = False
    files_id:list[str] = []

    if media_direction == "loading":
        if level == 4:
            counter_mediagroup, text, kbd, halt, edit = SaveToUser(S, uid, file_id, mgid, type, counter_mediagroup)
        else:
            text = S["cant_understend"]
            kbd = GoTo(S["main_menu"])
    else:
        text = S["cant_understend"]
        kbd = GoTo(S["main_menu"])
    return counter_mediagroup, text, kbd, halt, prmode, address, img, files_id, edit