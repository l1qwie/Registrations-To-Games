from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testChangeLanguageOrNo
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Settings.settings_keyboard import Language
from Admin_bot.language_dictoinary import String as S
import language_dictionary_for_all
import used_by_everyone as forall



def ChangeLanguage(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["choose_your_language"])
    assert(kbd == Language(S[lang]["ru"], S[lang]["en"], S[lang]["tur"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))

def Correctlang(text: str, kbd: object, lang: str):
    assert(text == S[lang]["language_changed"] + language_dictionary_for_all.String[lang]["main_menu_text"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))
    assert(3 == testSelectLevel(738070596))
    assert(True == testChangeLanguageOrNo(738070596, lang))



def InputLanguage(languages: list[str], lang: str):
    item:str = ''
    for item in languages:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            Correctlang(text, kbd, item)
        else:
            ChangeLanguage(text, kbd, lang, testSelectSomthingColumn(738070596, "direction"))
        assert(chattext == '')
        assert(chatkbd == None)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)





def HeadFunc(alloflist: list[str], lang: str, level: int):
    if level == 2:
        InputLanguage(alloflist, lang)
    else:
        assert(False)