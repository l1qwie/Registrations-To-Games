from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Main.tests.main_database_test import testSelectSomthingColumn, testSelectLevel, RemovedFromGameOrNo
from Admin_bot.Activities.activities_keyboard import RemoveFromGameOrCall
from Admin_bot.Activities.activities_database import SelectLengthOfActiveGames, SelectInfClient, SelectActiveGames
from Admin_bot.Clients.clients_database import SelectClient, SelectLengthOfClients
from Admin_bot.language_dictoinary import String as S
import language_dictionary_for_all as foralllang
import used_by_everyone as forall

class ActiveGame:
    game_id:int
    user_id:int
    game_launch_point:int
    client_launch_point:int

def CorrectGameId(text: str, kbd: object, lang: str, phrase: str):
    names:list[tuple[int, str, str]] = SelectClient(7, ActiveGame.client_launch_point)
    lengthofclients:int = SelectLengthOfClients(ActiveGame.game_id)
    assert(text == S[lang]["all_of_client_on_game"])
    assert(kbd == forall.KeyboardWithClientsNames(names, 7, ActiveGame.client_launch_point, lengthofclients, lang))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "activities_game_id"))

def StartShowActiveGame(text: str, kbd: object, lang: str, phrase: str, schedule: list[tuple[int, str, int, int, int]], launch_point: int):
    input_schedule:list[tuple[str, str, str, str, str]] = []
    game_id:int = -1
    sport:str = ''
    date:int = -1
    time:int = -1
    seats:int = -1

    length = SelectLengthOfActiveGames()
    for game_id, sport, date, time, seats in schedule:
        input_schedule.append((str(game_id), sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), str(seats)))

    assert(text == S[lang]["active_games"])
    assert(kbd == forall.Schedule(input_schedule, 7, launch_point, S[lang]["waiting_cl"], length))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))

def CorrectUserId(text: str, kbd: object, lang: str, phrase: str, prmode: str):
    name, lastname, nickname, phone_str, fromwhere, cl_lang = SelectInfClient(int(phrase))

    if name == "no_data":
        name = foralllang.String[lang][name]
    elif lastname == "no_data":
        lastname = foralllang.String[lang][lastname]
    elif phone_str == '-1':
        phone_str = foralllang.String[lang]["no_data"]
    elif fromwhere == "no_data":
        fromwhere = foralllang.String[lang][fromwhere]
    elif cl_lang == "no_data":
        cl_lang = foralllang.String[lang][cl_lang]

    assert(text == S[lang]["user_inf"] % (name, lastname, phone_str, fromwhere, cl_lang) + S[lang]["disclaimer"])
    if nickname:
        assert(kbd == RemoveFromGameOrCall(S[lang]["removeforgame"], S[lang]["call"], foralllang.String[lang]["main_menu_kb"], True, nickname))
    else:
        assert(kbd == RemoveFromGameOrCall(S[lang]["removeforgame"], S[lang]["call"], foralllang.String[lang]["main_menu_kb"], False, nickname))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "client_user_id"))
    assert(4 == testSelectLevel(738070596))
    assert(prmode == "HTML")

def CorrectComm(text: str, kbd: object, lang: str):
    assert(text == S[lang]["client_removed"] + foralllang.String[lang]["main_menu_text"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))
    assert(True == RemovedFromGameOrNo(ActiveGame.user_id, ActiveGame.game_id))


def InputActiveGameId(game_ids: list[str], lang: str):
    item:str = ''
    for item in game_ids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        ActiveGame.game_launch_point = testSelectSomthingColumn(738070596, "game_launch_point")
        if halt:
            ActiveGame.game_id = int(item)
            ActiveGame.client_launch_point = testSelectSomthingColumn(738070596, "client_launch_point")
            CorrectGameId(text, kbd, lang, item)
        else:
            direction:str = testSelectSomthingColumn(738070596, "direction")
            schedule = SelectActiveGames(7, ActiveGame.game_launch_point)
            StartShowActiveGame(text, kbd, lang, direction, schedule, ActiveGame.game_launch_point)
        assert(chattext == '')
        assert(chatkbd == None)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)

def InputUserId(userids: list[str], lang: str):
    item:str = ''
    for item in userids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            ActiveGame.user_id = int(item)
            CorrectUserId(text, kbd, lang, item, prmode)
        else:
            ActiveGame.client_launch_point = testSelectSomthingColumn(738070596, "client_launch_point")
            CorrectGameId(text, kbd, lang, str(ActiveGame.game_id))
            assert(prmode == '')
        assert(chattext == '')
        assert(chatkbd == None)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)

def InputDelete(deletecomm: list[str], lang: str):
    item:str = ''
    for item in deletecomm:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CorrectComm(text, kbd, lang)
            assert(prmode == '')
        else:
            CorrectUserId(text, kbd, lang, str(ActiveGame.user_id), prmode)
        assert(chattext == '')
        assert(chatkbd == None)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)


def HeadFunc(alloflist: list[str], lang: str, level: int):
    if level == 2:
        InputActiveGameId(alloflist, lang)
    elif level == 3:
        InputUserId(alloflist, lang)
    elif level == 4:
        InputDelete(alloflist, lang)
    else:
        assert(False)