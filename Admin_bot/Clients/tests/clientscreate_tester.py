from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Clients.clients_keyboard import FromWhere, SaveOrChange
from Admin_bot.language_dictoinary import String as S
import used_by_everyone as forall
import language_dictionary_for_all

class CreateClient:
    fromwhere: str
    name: str
    last_name: str
    phone_num: int

def CorrectFromWhere(text: str, kbd: object, lang: str, phrase: str):
    assert(text == (S[lang]["fromwhere"] % (CreateClient.fromwhere)) + S[lang]["writename"])
    assert(kbd == forall.GoToAdmin(language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(phrase == testSelectSomthingColumn(738070596, "client_fromwhere"))

def StartCreate(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["choose_fromwhere"])
    assert(kbd == FromWhere(S[lang]["teledirectionary"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))

def SaveName(text: str, kbd: object, lang: str, phrase: str):
    assert(text == (S[lang]["fromwhere+name"] % (CreateClient.fromwhere, CreateClient.name)) + S[lang]["writelastname"])
    assert(kbd == forall.GoToAdmin(language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(phrase == testSelectSomthingColumn(738070596, "client_name"))

def SaveLastName(text: str, kbd: object, lang: str, phrase: str):
    assert(text == (S[lang]["fromwhere+name+last_name"] % (CreateClient.fromwhere, CreateClient.name, CreateClient.last_name)) + S[lang]["writephonenum"])
    assert(kbd == forall.GoToAdmin(language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(phrase == testSelectSomthingColumn(738070596, "client_last_name"))

def SavePhoneNum(text: str, kbd: object, lang: str, phrase: str):
    assert(text == (S[lang]["fromwhere+name+last_name+phonenum"] % (CreateClient.fromwhere, CreateClient.name, CreateClient.last_name, CreateClient.phone_num)) + S[lang]["saveorchange"])
    assert(kbd == SaveOrChange(S[lang]["savegame"], S[lang]["changegame"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "client_phonenum"))

def SaveAll(text: str, kbd: object, lang: str):
    assert(text == S[lang]["data_save"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))




def InputFromWhere(fromwhere: list[str], lang: str):
    item:str = ''
    for item in fromwhere:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CreateClient.fromwhere = item
            CorrectFromWhere(text, kbd, lang, item)
            assert(prmode == 'HTML')
        else:
            StartCreate(text, kbd, lang, "create client")
            assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)


def InputName(names: list[str], lang: str):
    item:str = ''
    for item in names:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        CreateClient.name = item
        SaveName(text, kbd, lang, item)
        assert(prmode == "HTML")
        assert(halt == False)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputLastName(last_names: list[str], lang: str):
    item:str = ''
    for item in last_names:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        CreateClient.last_name = item
        SaveLastName(text, kbd, lang, item)
        assert(prmode == "HTML")
        assert(halt == False)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)


def InputPhoneNum(phnums: list[str], lang: str):
    item:str = ''
    for item in phnums:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CreateClient.phone_num = int(item)
            SavePhoneNum(text, kbd, lang, item)
        else:
            SaveLastName(text, kbd, lang, CreateClient.last_name)
        assert(prmode == "HTML")
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputSaveOrChange(saveorchange: list[str], lang: str):
    item:str = ''
    for item in saveorchange:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            SaveAll(text, kbd, lang)
            assert(prmode == '')
        else:
            SavePhoneNum(text, kbd, lang, str(CreateClient.phone_num))
            assert(prmode == "HTML")
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def HeadFunc(alloflist: list[str], lang: str, level: int):
    if level == 2:
        InputFromWhere(alloflist, lang)
    elif level == 3:
        InputName(alloflist, lang)
    elif level == 4:
        InputLastName(alloflist, lang)
    elif level == 5:
        InputPhoneNum(alloflist, lang)
    elif level == 6:
        InputSaveOrChange(alloflist, lang)
    else:
        assert(False)