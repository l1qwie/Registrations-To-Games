from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testDataFitting
from Admin_bot.language_dictoinary import String as S
from Admin_bot.Welcome.welcome_keyboard import ComStartReg
import language_dictionary_for_all
import used_by_everyone as forall

text:str = ''
kbd:object = None
prmode:str = ''
halt:bool = False
spreadsheet:str = ''
fixed:bool = False



#Action functions
def SayHello(text: str, kbd: object, lang: str):
    assert(text == S[lang]["first_message"])
    assert(kbd == ComStartReg(S[lang]["hello"]))
    assert(1 == testSelectLevel(738070596))

def Password(text: str, kbd: object, lang: str):
    assert(text == S[lang]["enter_password"])
    assert(kbd == None)
    assert(2 == testSelectLevel(738070596))

def WrongPassword(text: str, lang: str):
    assert(text == S[lang]["wrong_pass"])
    assert(2 == testSelectLevel(738070596))

def CorrectPassword(text: str, kbd: object, lang: str, prmode: str, fixed: bool):
    assert(text == S[lang]["global_rules"])
    assert(kbd == forall.GoToAdmin(language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(3 == testSelectLevel(738070596))
    assert(prmode == "HTML")
    assert(fixed == True)

def AlomostShowMenu(text: str, kbd: object, lang: str):
    assert(text == language_dictionary_for_all.String[lang]["main_menu_text"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))
    assert(3 == testSelectLevel(738070596))

#Header functions
def FirstMessage(first_message: list[str], lang: str):
    item:str = ''
    for item in first_message:
        testDataFitting("registration", 0, 738070596)
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        SayHello(text, kbd, lang)
        assert(halt == False)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def EnterPassword(reg: list[str], lang: str):
    item:str = ''
    for item in reg:
        testDataFitting("registration", 1, 738070596)
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            Password(text, kbd, lang)
        else:
            SayHello(text, kbd, lang)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def ShowRules(password: list[str], lang: str):
    item:str = ''
    for item in password:
        testDataFitting("registration", 2, 738070596)
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CorrectPassword(text, kbd, lang, prmode, fixed)
        else:
            WrongPassword(text, lang)
            assert(prmode == '')
            assert(kbd == None)
            assert(fixed == False)
        assert(spreadsheet == '')
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def ShowMenu(main_menu: list[str], lang: str):
    item:str = ''
    for item in main_menu:
        testDataFitting("registration", 3, 738070596)
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if item == "Main_Menu":
            AlomostShowMenu(text, kbd, lang)
            assert(prmode == '')
            assert(fixed == False)
        else:
            CorrectPassword(text, kbd, lang, prmode, fixed)
        assert(spreadsheet == '')
        print(halt)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)
