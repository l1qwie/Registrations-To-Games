from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testChangeOrNo, testSelectLatAndLong
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Main.main_database import SelectDataFromSchedule
from Admin_bot.language_dictoinary import String as S
from Admin_bot.Game.game_database import ScheduleOfGames, LengthOfGames
from Admin_bot.Game.game_keyboard import OptionsOfChange, KindOfSport
from Admin_bot.Game.tests.creategames_tester import CreateGame
import language_dictionary_for_all as foralllang
import used_by_everyone as forall


class ChangeGame:
    game_id:int
    change_type:str
    data:str


#action functions
def CorrectPhrase(text: str, kbd: object, lang: str, launch_point: int):
    schedule_output:list[tuple[str, str, str, str]] = []
    schedule_input:list[tuple[int, str, int, int]] = ScheduleOfGames(launch_point, 7)
    length:int = LengthOfGames()
    _schedule_, schedule_output = forall.SheduleStr([], schedule_input, lang)
    assert(text == S[lang]["choose_game"])
    assert(kbd == forall.Schedule(schedule_output, 7, launch_point, '', length))
    assert(2 == testSelectLevel(738070596))

def CorrectGameId(text: str, kbd: object, lang: str, phrase: str, prmode: str):
    assert(text == S[lang]["game_inf"] % (CreateGame.sport, CreateGame.date, CreateGame.time, CreateGame.seats, CreateGame.price, CreateGame.currency, CreateGame.latitude, CreateGame.longitude, CreateGame.address) + S[lang]["choose_change"])
    assert(kbd == OptionsOfChange(S[lang]["sport"], S[lang]["date"], S[lang]["time"], S[lang]["seats"], S[lang]["price"], S[lang]["currency"], S[lang]["link"], S[lang]["nameaddress"], foralllang.String[lang]["main_menu_kb"]))
    assert(3 == testSelectLevel(738070596))
    assert(prmode == "HTML")
    assert(int(phrase) == testSelectSomthingColumn(738070596, "game_game_id"))

def CorrectType(text: str, kbd: object, lang: str, phrase: str):
    if phrase == "sport":
        assert(text == S[lang]["start_create_game"])
        assert(kbd == KindOfSport(foralllang.String[lang]["volleyball"], foralllang.String[lang]["football"], foralllang.String[lang]["main_menu_kb"]))
    elif phrase == "date":
        assert(text == S[lang]["writedate"])
    elif phrase == "time":
        assert(text == S[lang]["whitetime"])
    elif phrase == "seats":
        assert(text == S[lang]["writeseats"])
    elif phrase == "price":
        assert(text == S[lang]["writeprice"])
    elif phrase == "currency":
        assert(text == S[lang]["writecurrency"])
    elif phrase == "link":
        assert(text == S[lang]["writelink"])
    elif phrase == "nameaddress":
        assert(text == S[lang]["writeaddress"])
    assert(phrase == testSelectSomthingColumn(738070596, "game_change_direction"))

def InputNewData(text: str, kbd: object, lang: str, change_direction: str, phrase: str, dir: bool, game_id: int):
    assert(text == S[lang]["data_changed"])
    if change_direction == "link":
        direc:list[str] = ["latitude", "longitude"]
        i:int = 0
        while i < 2:
            assert(True == testChangeOrNo(direc[i], phrase, dir, 738070596, game_id))
            i += 1
        CreateGame.latitude, CreateGame.longitude = testSelectLatAndLong(game_id)
    else:
        assert(True == testChangeOrNo(change_direction, phrase, dir, 738070596, game_id))
        if change_direction == "sport":
            CreateGame.sport = phrase
        elif change_direction == "date":
            CreateGame.date = phrase
        elif change_direction == "time":
            CreateGame.time = phrase
        elif change_direction == "seats":
            CreateGame.seats = int(phrase)
        elif change_direction == "price":
            CreateGame.price = int(phrase)
        elif change_direction == "currency":
            CreateGame.currency = phrase
        elif change_direction == "address":
            CreateGame.address = phrase
    assert(kbd == forall.AnotherChange(S[lang]["yes"], S[lang]["no"]))

#Header functions
def InputGameId(game_ids: list[str], lang: str):
    item:str = ''
    for item in game_ids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            ChangeGame.game_id = int(item)
            CreateGame.sport, date, time, CreateGame.seats, CreateGame.price, CreateGame.currency, CreateGame.latitude, CreateGame.longitude, CreateGame.address = SelectDataFromSchedule(ChangeGame.game_id)
            CreateGame.date = forall.CreateDateStr(date); CreateGame.time = forall.CreateTimeStr(time)
            CorrectGameId(text, kbd, lang, item, prmode)
        else:
            print("launch_point =",testSelectSomthingColumn(738070596, "game_launch_point"))
            CorrectPhrase(text, kbd, lang, testSelectSomthingColumn(738070596, "game_launch_point"))
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)
        

def InputKindOfChanging(kindofchanging: list[str], lang: str):
    item:str = ''
    for item in kindofchanging:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            ChangeGame.change_type = item
            CorrectType(text, kbd, lang, item)
        else:
            CorrectGameId(text, kbd, lang, str(ChangeGame.game_id), prmode)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputChangeData(change_data: list[str], lang: str, dir: bool):
    item:str = ''
    for item in change_data:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            ChangeGame.data = item
            InputNewData(text, kbd, lang, ChangeGame.change_type, item, dir, ChangeGame.game_id)
        else:
            CorrectType(text, kbd, lang, ChangeGame.change_type)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputRepeat(repeat: list[str], lang: str, dir: bool):
    item:str = ''
    for item in repeat:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CorrectGameId(text, kbd, lang, str(ChangeGame.game_id), prmode)
        else:
            InputNewData(text, kbd, lang, ChangeGame.change_type, ChangeGame.data, dir, ChangeGame.game_id)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)


def ChangeDiraction(infaboutgame: list[str], lang: str, level: int):
    print("level?", level)
    if level == 2:
        InputGameId(infaboutgame, lang)
    elif level == 3:
        InputKindOfChanging(infaboutgame, lang)
    elif level == 4:
        InputChangeData(infaboutgame, lang, False)
    elif level == 5:
        InputRepeat(infaboutgame, lang, False)