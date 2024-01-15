from Admin_bot.Settings.settings_keyboard import DirectionOfSettings, Language
from Admin_bot.Settings.settings_database import ChangeLanguage
from Admin_bot.language_dictoinary import String
import language_dictionary_for_all
import used_by_everyone as forall

def ChooseSettingDirection(S: dict[str, str], language: str) -> tuple[int, str, object]:
    return (1, S["choose_dir_set"], DirectionOfSettings(S["change_lang"], language_dictionary_for_all.String[language]["main_menu_kb"]))

def StartSettings(S: dict[str, str], phrase: str, level: int, language: str, direction: str, halt: bool) -> tuple[int, str, str, object, bool]:
    text:str = ''
    kbd:object = None

    if phrase in ("change language"):
        halt = True
        level = 2
        direction = phrase
        if phrase == "change language":
            text = S["choose_your_language"]
            kbd = Language(S["ru"], S["en"], S["tur"], language_dictionary_for_all.String[language]["main_menu_kb"])
        else:
            (level, text, kbd) = ChooseSettingDirection(S, language)
    else:
        (level, text, kbd) = ChooseSettingDirection(S, language)
    return (level, direction, text, kbd, halt)

def InputLanguage(S: dict[str,str], phrase: str, level: int, new_language: str, act: str, halt: bool, aid: int, language: str, direction: str) -> tuple[int, str, str, str, object, bool]:
    text:str = ''
    kbd:object = None
    _halt_:bool = False
    _direction_:str = ''

    if phrase in ("ru", "en", "tur"):
        ChangeLanguage(aid, phrase)
        new_language = phrase
        halt = True
        level = 3
        act = "divarication"
        text = String[new_language]["language_changed"] + language_dictionary_for_all.String[new_language]["main_menu_text"]
        kbd = forall.OptionsAdmin(String[new_language]["first_option"], String[new_language]["second_option"], String[new_language]["third_option"], String[new_language]["fourth_option"], String[new_language]["fifth_option"])
    else:
        (level, _direction_, text, kbd, _halt_) = StartSettings(S, direction, level, language, _direction_, _halt_)
    return (level, act, new_language, text, kbd, halt)
        
def HeadFuncOfChangeLanguages(S: dict[str, str], phrase: str, level: int, language: str, act: str, halt: bool, aid: int, direction: str):
    if level == 2:
        (level, act, language, text, kbd, halt) = InputLanguage(S, phrase, level, language, act, halt, aid, language, direction)
    else:
        assert(False)
    return (level, act, language, text, kbd, halt)