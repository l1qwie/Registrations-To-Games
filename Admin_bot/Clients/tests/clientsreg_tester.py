from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, RegedOrNo
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Game.game_database import ScheduleOfGamesWithSeats, LengthOfGames
from Admin_bot.Clients.clients_database import SelectClient, SelectCountClient, SelectPriceAndCurrency
from Admin_bot.language_dictoinary import String as S
import used_by_everyone as forall
import language_dictionary_for_all


class RegClient:
    uid:int
    game_id:int
    seats:int
    paymethod:str


def ShowClients(text: str, kbd: object, lang: str, limit: int, launch_point: int):
    names:list[tuple[int, str, str]] = SelectClient(limit, launch_point)
    length:int = SelectCountClient()
    assert(text == S[lang]["chose_your_client"])
    assert(kbd == forall.KeyboardWithClientsNames(names, limit, launch_point, length, lang))
    assert(2 == testSelectLevel(738070596))

def CorrectId(text: str, kbd: object, lang: str, phrase: str, launch_point: int):
    schedule_input:list[tuple[int, str, int, int, int]] = ScheduleOfGamesWithSeats(launch_point, 7)
    length:int = LengthOfGames()
    schedule_output, _schedule_, = forall.SheduleStr(schedule_input, [], lang)
    print("???", launch_point)
    assert(text == S[lang]["choose_game"])
    assert(kbd == forall.Schedule(schedule_output, 7, launch_point, S[lang]["seats"], length))
    assert(3 == testSelectLevel(738070596))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "client_user_id")) 

def CorrectGameId(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["type_seats"])
    assert(kbd == forall.GoToAdmin(language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(4 == testSelectLevel(738070596))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "client_game_id")) #!

def CorrectSeat(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["choose_paymethod"])
    assert(kbd == forall.KbPay(S[lang]["online"], S[lang]["cash"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(5 == testSelectLevel(738070596))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "client_seats")) #! 

def CorrectPaymethod(text: str, kbd: object, lang: str, phrase: str):
    price, currency = SelectPriceAndCurrency(RegClient.game_id)
    assert(text == S[lang]["client_reged"] % ((price*RegClient.seats), currency) + language_dictionary_for_all.String[lang]["main_menu_text"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))
    assert(phrase == testSelectSomthingColumn(738070596, "client_paymethod")) #!
    assert(True == RegedOrNo(RegClient.uid, RegClient.game_id, RegClient.seats, RegClient.paymethod))


def InputClientId(userids: list[str], lang: str):
    item:str = ''
    for item in userids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            RegClient.uid = int(item)
            game_launch_point = testSelectSomthingColumn(738070596, "client_launch_point")
            CorrectId(text, kbd, lang, item, game_launch_point)
        else:
            cl_launch_point = testSelectSomthingColumn(738070596, "client_launch_point")
            print("cl_launch_point =", cl_launch_point)
            ShowClients(text, kbd, lang, 7, cl_launch_point)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputGameId(game_ids: list[str], lang: str):
    item:str = ''
    for item in game_ids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            RegClient.game_id = int(item)
            CorrectGameId(text, kbd, lang, item)
        else:
            game_launch_point = testSelectSomthingColumn(738070596, "game_launch_point")
            print("game_launch_point = ", game_launch_point)
            CorrectId(text, kbd, lang, str(RegClient.uid), game_launch_point)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputSeats(seatsnum: list[str], lang: str):
    item:str = ''
    for item in seatsnum:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            RegClient.seats = int(item)
            CorrectSeat(text, kbd, lang, item)
        else:
            CorrectGameId(text, kbd, lang, str(RegClient.game_id))
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputPaymethod(paymethods: list[str], lang: str):
    item:str = ''
    for item in paymethods:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            RegClient.paymethod = item
            CorrectPaymethod(text, kbd, lang, item)
        else:
            CorrectSeat(text, kbd, lang, str(RegClient.seats))
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)


def HeadFunc(alloflist: list[str], lang: str, level: int):
    if level == 2:
        InputClientId(alloflist, lang)
    elif level == 3:
        InputGameId(alloflist, lang)
    elif level == 4:
        InputSeats(alloflist, lang)
    elif level == 5:
        InputPaymethod(alloflist, lang)
