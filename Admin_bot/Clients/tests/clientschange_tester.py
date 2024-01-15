from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, InfUserChangeOrNoDataInt, InfUserChangeOrNoDataStr
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Clients.clients_keyboard import OptionChange, FromWhere
from Admin_bot.Clients.clients_database import SelectClient, SelectCountClient, SelectAllInf
from Admin_bot.language_dictoinary import String as S
import used_by_everyone as forall
import language_dictionary_for_all

class ChangeUser:
    launch_point:int
    user_id:int
    changeopt:str
    changedata_str:str
    changedata_int:int

def ShowClients(text: str, kbd: object, lang: str, limit: int):
    names:list[tuple[int, str, str]] = SelectClient(limit, ChangeUser.launch_point)
    length:int = SelectCountClient()
    assert(text == S[lang]["chose_your_client"])
    assert(kbd == forall.KeyboardWithClientsNames(names, limit, ChangeUser.launch_point, length, lang))
    assert(2 == testSelectLevel(738070596))

def CorrectUserId(text: str, kbd: object, lang: str, phrase: str, prmode: str):
    assert(text == S[lang]["user_inf"] % (SelectAllInf(ChangeUser.user_id)) + S[lang]["choose_dir_for_change"])
    assert(kbd == OptionChange(S[lang]["fromwhere_kb"], S[lang]["name_kb"], S[lang]["last_name_kb"], S[lang]["phonenum_kb"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "client_user_id"))
    assert(prmode == "HTML")

def CorrectChangeOpt(text: str, kbd: object, lang: str, phrase: str):
    if phrase == "from_where":
        assert(text == S[lang]["choose_fromwhere"])
        assert(kbd == FromWhere(S[lang]["teledirectionary"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    elif phrase == "name":
        assert(text == S[lang]["writename"])
    elif phrase == "last_name":
        assert(text == S[lang]["writelastname"])
    elif phrase == "phone_number":
        assert(text == S[lang]["writephonenum"])
    assert(phrase == testSelectSomthingColumn(738070596, "client_change_option"))
    
def InputNewData(text: str, kbd: object, lang: str, phrase: str, halt: bool):
    if ChangeUser.changeopt == "phone_number":
        if halt:
            ChangeUser.changedata_int = int(phrase)
            assert(True == InfUserChangeOrNoDataInt(ChangeUser.changedata_int, ChangeUser.user_id))
            assert(text == S[lang]["user_inf"] % (SelectAllInf(ChangeUser.user_id)) + S[lang]["inf_saved"] + S[lang]["data_changed"])
            assert(kbd == forall.AnotherChange(S[lang]["yes"], S[lang]["no"]))
        else:
            CorrectChangeOpt(text, kbd, lang, ChangeUser.changeopt)
    elif ChangeUser.changeopt == "from_where":
        if halt:
            ChangeUser.changedata_str = phrase
            print(text == S[lang]["user_inf"] % (SelectAllInf(ChangeUser.user_id)) + S[lang]["inf_saved"] + S[lang]["data_changed"])
            assert(True == InfUserChangeOrNoDataStr(ChangeUser.changedata_str, ChangeUser.changeopt, ChangeUser.user_id))
            assert(text == S[lang]["user_inf"] % (SelectAllInf(ChangeUser.user_id)) + S[lang]["inf_saved"] + S[lang]["data_changed"])
            assert(kbd == forall.AnotherChange(S[lang]["yes"], S[lang]["no"]))
        else:
            CorrectChangeOpt(text, kbd, lang, ChangeUser.changeopt)
    elif ChangeUser.changeopt in ("name", "last_name"):
        ChangeUser.changedata_str = phrase
        assert(True == InfUserChangeOrNoDataStr(ChangeUser.changedata_str, ChangeUser.changeopt, ChangeUser.user_id))
        assert(text == S[lang]["user_inf"] % (SelectAllInf(ChangeUser.user_id)) + S[lang]["inf_saved"] + S[lang]["data_changed"])
        assert(kbd == forall.AnotherChange(S[lang]["yes"], S[lang]["no"]))
    else:
        assert(False)

def InputUserId(userids: list[str], lang: str):
    item:str = ''
    for item in userids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            ChangeUser.user_id = int(item)
            CorrectUserId(text, kbd, lang, item, prmode)
        else:
            ChangeUser.launch_point = testSelectSomthingColumn(738070596, "client_launch_point")
            print("client_launch_point =", ChangeUser.launch_point)
            ShowClients(text, kbd, lang, 7)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputChangeOption(options: list[str], lang: str):
    item:str = ''
    for item in options:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            ChangeUser.changeopt = item
            CorrectChangeOpt(text, kbd, lang, item)
        else:
            CorrectUserId(text, kbd, lang, str(ChangeUser.user_id), prmode)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputChangeData(datas: list[str], lang: str):
    item:str = ''
    for item in datas:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid)= DispatchPhrase(738070596, item, lang)
        InputNewData(text, kbd, lang, item, halt)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputRepeat(repatorno:list[str], lang: str):
    item:str = ''
    for item in repatorno:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CorrectUserId(text, kbd, lang, str(ChangeUser.user_id), prmode)
        else:
            if ChangeUser.changeopt == "phone_number":
                InputNewData(text, kbd, lang, str(ChangeUser.changedata_int), True)
            else:
                InputNewData(text, kbd, lang, ChangeUser.changedata_str, True)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def HeadFunc(alloflist: list[str], lang: str, level: int):
    if level == 2:
        InputUserId(alloflist, lang)
    elif level == 3:
        InputChangeOption(alloflist, lang)
    elif level == 4:
        InputChangeData(alloflist, lang)
    elif level == 5:
        InputRepeat(alloflist, lang)
    else:
        assert(False)