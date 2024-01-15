from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testDataFitting
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Settings.settings_keyboard import DirectionOfSettings, Language
from Admin_bot.Settings.tests.settings_lang import HeadFunc
from Admin_bot.language_dictoinary import String as S
import language_dictionary_for_all



def Direction(text: str, kbd: object, lang: str):
    assert(text == S[lang]["choose_dir_set"])
    assert(kbd == DirectionOfSettings(S[lang]["change_lang"], language_dictionary_for_all.String[lang]["main_menu_kb"])) 
    assert(1 == testSelectLevel(738070596))

def ChangeLanguage(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["choose_your_language"])
    assert(kbd == Language(S[lang]["ru"], S[lang]["en"], S[lang]["tur"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))



def ChooseSettingDirection(firstmessage: list[str], lang: str):
    item:str = ''
    for item in firstmessage:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        Direction(text, kbd, lang)
        assert(chattext == '')
        assert(chatkbd == None)
        assert(prmode == '')
        assert(halt == False)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)

def StartSettings(directions: list[str], lang: str):
    item:str = ''
    for item in directions:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            if item == "change language":
                ChangeLanguage(text, kbd, lang, item)
            else:
                Direction(text, kbd, lang)
        else:
            Direction(text, kbd, lang)
        assert(chattext == '')
        assert(chatkbd == None)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)



def DirectionOfActionSettings(alloflist: list[str], lang: str, level: int):
    testDataFitting("settings", level, 738070596)
    direction = testSelectSomthingColumn(738070596, "direction")
    if direction not in ("change language", "!free space!"):
        if level == 0:
            ChooseSettingDirection(alloflist, lang)
        elif level == 1:
            StartSettings(alloflist, lang)
    else:
        if direction == "change language":
            HeadFunc(alloflist, lang, level)
