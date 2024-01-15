from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testDataFitting
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.language_dictoinary import String as S
from Admin_bot.Clients.clients_keyboard import ClientsDirections, FromWhere
from Admin_bot.Clients.clients_database import SelectCountClient, SelectClient
from Admin_bot.Clients.tests.clientscreate_tester import HeadFunc as createClHeadFunc
from Admin_bot.Clients.tests.clientschange_tester import HeadFunc as changeClHeadFunc
from Admin_bot.Clients.tests.clientsdelete_tester import HeadFunc as deleteClHeadFunc
from Admin_bot.Clients.tests.clientsreg_tester import HeadFunc as regClHeadFunc
import language_dictionary_for_all
import used_by_everyone as forall

def Directions(text: str, kbd: object, lang: str):
    assert(text == S[lang]["choose_cl_dir"])
    assert(kbd == ClientsDirections(S[lang]["create_client"], S[lang]["change_client"], S[lang]["delete_client"], S[lang]["reg_client"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(1 == testSelectLevel(738070596))

def ShowClients(text: str, kbd: object, lang: str, phrase: str, names: list[tuple[int, str, str]], limit: int, launch_point: int):
    length:int = SelectCountClient()
    assert(text == S[lang]["chose_your_client"])
    assert(kbd == forall.KeyboardWithClientsNames(names, limit, launch_point, length, lang))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))

def NoClients(text: str, kbd: object, lang: str):
    assert(text == S[lang]["no_clients"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))

def StartCreate(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["choose_fromwhere"])
    assert(kbd == FromWhere(S[lang]["teledirectionary"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))


def ChooseClientDirection(firstmes: list[str], lang: str):
    item:str = ''
    for item in firstmes:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        Directions(text, kbd, lang)
        assert(prmode == '')
        assert(halt == False)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def ShowClientsByDirection(directions: list[str], lang: str):
    item:str = ''
    for item in directions:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            if item != "create client":
                limit = 7
                launch_point = testSelectSomthingColumn(738070596, "client_launch_point")
                names:list[tuple[int, str, str]] = SelectClient(limit, launch_point)
                if names != []:
                    ShowClients(text, kbd, lang, item, names, limit, launch_point)
                else:
                    NoClients(text, kbd, lang)
            else:
                StartCreate(text, kbd, lang, item)
        else:
            Directions(text, kbd, lang)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)
        


def DirectionOfActionClients(alloflist:list[str], lang: str, level: int):
    testDataFitting("clients", level, 738070596)
    direction = testSelectSomthingColumn(738070596, "direction")
    if direction not in ("create client", "change client", "delete client", "reg client to game"):
        if level == 0:
            ChooseClientDirection(alloflist, lang)
        elif level == 1:
            ShowClientsByDirection(alloflist, lang)
        else:
            assert(False)
    else:
        if direction == "create client":
            createClHeadFunc(alloflist, lang, level)
        elif direction == "change client":
            changeClHeadFunc(alloflist, lang, level)
        elif direction == "delete client":
            deleteClHeadFunc(alloflist, lang, level)
        elif direction == "reg client to game":
            regClHeadFunc(alloflist, lang, level)
