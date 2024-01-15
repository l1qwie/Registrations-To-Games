from Admin_bot.language_dictoinary import String as S
from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, ChangePaidOrNo
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Money.money_keyboard import CallOrConfirm
from Admin_bot.Money.money_database import SelectCountClient, ScheduleOfGames, SelectClientNickname, SelectCountHowManyGame, SelectInfAboutClientGame, SelectClient, CountClientGames, SelectClientAfterGameId
from Admin_bot.Clients.clients_database import SelectAllInf
import language_dictionary_for_all
import used_by_everyone as forall

class Paid:
    launch_point:int
    user_id:int
    game_id:int


def SeeDebtors(text: str, kbd: object, lang: str, names: list[tuple[int, str, str]], launch_point: int, phrase: str):
    length:int = SelectCountClient()
    assert(text == S[lang]["choose_your_debtor"])
    assert(kbd == forall.KeyboardWithClientsNames(names, 7, launch_point, length, lang))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))

def ALotOfGames(text: str, kbd: object, lang: str, length: int, launch_point: int):
    schedule_input:list[tuple[int, str, int, int]] = ScheduleOfGames(Paid.user_id, 7, launch_point)
    _schedule_, schedule_output = forall.SheduleStr([], schedule_input, lang)
    assert(text == S[lang]["choose_game"])
    assert(kbd == forall.Schedule(schedule_output, 7, launch_point, '', length))
    assert(4 == testSelectLevel(738070596))

def OneGame(text: str, kbd: object, lang: str):
    assert(text == S[lang]["client_paided"] + language_dictionary_for_all.String[lang]["main_menu_text"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))
    assert(3 == testSelectLevel(738070596))
    assert(True == ChangePaidOrNo(Paid.user_id, Paid.game_id))

def CorrectUserId(text: str, kbd: object, lang: str, phrase: str, prmode: str):
    testtext:str = ''
    i:int = 0
    nickname:str = SelectClientNickname(int(phrase))
    game_ids:list[int] = SelectCountHowManyGame(int(phrase))

    while i < len(game_ids):
        (sport, date, time, price, currency, cl_seats, payment) = SelectInfAboutClientGame(game_ids[i], int(phrase))
        sum = price * cl_seats
        testtext += S[lang]["cl_game_inf"] % (sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), sum, currency, cl_seats, payment)
        i += 1
    
    name, lastname, phone, fromwhere, cl_lang = SelectAllInf(int(phrase))
    phone_str = str(phone)
    if name == "no_data":
        name = language_dictionary_for_all.String[lang]["no_data"]
    elif lastname == "no_data":
        lastname = language_dictionary_for_all.String[lang]["no_data"]
    elif phone_str == "no_data":
        phone_str = language_dictionary_for_all.String[lang]["no_data"]
    elif fromwhere == "no_data":
        fromwhere = language_dictionary_for_all.String[lang]["no_data"]
    elif cl_lang == "no_data":
        cl_lang = language_dictionary_for_all.String[lang]["no_data"]

    assert(text == S[lang]["user_inf"] % (name, lastname, phone_str, fromwhere, cl_lang) + testtext)
    assert(kbd == CallOrConfirm(S[lang]["call"], S[lang]["paided"], language_dictionary_for_all.String[lang]["main_menu_kb"], nickname))
    assert(3 == testSelectLevel(738070596))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "finances_user_id"))
    assert(prmode == "HTML")


def InputUserId(user_ids: list[str], lang: str):
    item:str = ''
    for item in user_ids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            Paid.user_id = int(item)
            CorrectUserId(text, kbd, lang, item, prmode)
        else:
            launch_point = testSelectSomthingColumn(738070596, "client_launch_point")
            names:list[tuple[int, str, str]] = SelectClient(7, launch_point)
            direc:str = testSelectSomthingColumn(738070596, "direction")
            print("client_launch_point =", launch_point)
            SeeDebtors(text, kbd, lang, names, launch_point, direc)
        assert(chattext == '')
        assert(chatkbd == None)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)

def InputPaided(paided: list[str], lang: str):
    item:str = ''
    for item in paided:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            number_of_games:int = CountClientGames(Paid.user_id)
            if number_of_games > 1:
                launch_point = testSelectSomthingColumn(738070596, "game_launch_point")
                ALotOfGames(text, kbd, lang, number_of_games, launch_point)
            else:
                Paid.game_id = SelectClientAfterGameId(Paid.user_id)
                OneGame(text, kbd, lang)
        else:
            CorrectUserId(text, kbd, lang, str(Paid.user_id), prmode)
        assert(chattext == '')
        assert(chatkbd == None) 
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
    
def InputGameId(game_ids: list[str], lang: str):
    item:str = ''
    for item in game_ids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            Paid.game_id = int(item)
            OneGame(text, kbd, lang)
        else:
            number_of_games:int = CountClientGames(Paid.user_id)
            launch_point = testSelectSomthingColumn(738070596, "game_launch_point")
            print("game_launch_point =", launch_point)
            ALotOfGames(text, kbd, lang, number_of_games, launch_point)
        assert(chattext == '')
        assert(chatkbd == None)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)


def HeadFunc(alloflist: list[str], lang: str, level: int):
    if level == 2:
        InputUserId(alloflist, lang)
    elif level == 3:
        InputPaided(alloflist, lang)
    elif level == 4:
        InputGameId(alloflist, lang)