from User_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testDataFitting
from User_bot.Main.main_action import DispatchPhrase
from User_bot.language_dictionary import Strings as S
from User_bot.Welcome.welcome_keyboard import Registration, Further
import used_by_everyone as forall

text:str = ''
kbd:object = None
halt:bool = False
prmode:str = ''
address:list[float] = []
img:str = ''
edit:bool = False
files_id:list[str] = []
typeoffile:list[str] = []


#action function
def Welcome(text: str, kbd: object, lang: str):
    assert(text == S[lang]["welcome_to_bot"])
    assert(kbd == Registration(S[lang]["reg"]))
    assert(1 == testSelectLevel(738070596))

def ShowRules(text: str, kbd: object, lang: str):
    assert(text == S[lang]["bot_rules"])
    assert(kbd == Further(S[lang]["all_right"]))
    assert(2 == testSelectLevel(738070596))

def ShowOptionsAfterRules(text: str, kbd: object, lang: str):
    assert(text == S[lang]["choose_option"])
    assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("completed" == testSelectSomthingColumn(738070596, "setup_reg"))


#Header function
def GreetingsToUser(first_message: list[str], lang: str):
    item:str = ''
    for item in first_message:
        testDataFitting("registration", 0, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        Welcome(text, kbd, lang)
        assert(halt == False)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])

def WarningRules(press_GoReg: list[str], lang: str):
    item:str = ''
    for item in press_GoReg:
        testDataFitting("registration", 1, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if halt:
            ShowRules(text, kbd, lang)
        else:
            Welcome(text, kbd, lang)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])

def GoToOptions(prees_GoNext: list[str], lang: str):
    item:str = ''
    for item in prees_GoNext:
        testDataFitting("registration", 2, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if halt:
            ShowOptionsAfterRules(text, kbd, lang)
        else:
            ShowRules(text, kbd, lang)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])