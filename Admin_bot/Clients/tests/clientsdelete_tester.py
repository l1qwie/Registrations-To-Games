from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, DeleteClientOrNo
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Clients.clients_database import SelectCountClient, SelectClient
from Admin_bot.language_dictoinary import String as S
import used_by_everyone as forall
import language_dictionary_for_all


def ShowClients(text: str, kbd: object, lang: str, limit: int, launch_point: int):
    length:int = SelectCountClient()
    names:list[tuple[int, str, str]] = SelectClient(limit, launch_point)
    assert(text == S[lang]["chose_your_client"])
    assert(kbd == forall.KeyboardWithClientsNames(names, limit, launch_point, length, lang))
    assert(2 == testSelectLevel(738070596))

def CorrectId(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["client_delete"] + language_dictionary_for_all.String[lang]["main_menu_text"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert(True == DeleteClientOrNo(int(phrase)))



def DeleteClient(userids: list[str], lang: str):
    item:str = ''
    for item in userids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CorrectId(text, kbd, lang, item)
        else:
            launch_point = testSelectSomthingColumn(738070596, "client_launch_point")
            ShowClients(text, kbd, lang, 7, launch_point)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)



def HeadFunc(alloflist: list[str], lang: str, level: int):
    if level == 2:
        DeleteClient(alloflist, lang)
    else:
        assert(False)