from Admin_bot.Welcome.welcome_keyboard import ComStartReg
from Admin_bot.Welcome.welcome_database import Password, StatusReg
import language_dictionary_for_all
import used_by_everyone as forall

#Action functions





#Header functions
def FirstMessage(S: dict[str, str]) -> tuple[int, str, object]:
    return 1, S["first_message"], ComStartReg(S["hello"])

def EnterPassword(S: dict[str, str], phrase: str, level: int) -> tuple[int, str, object, bool]:
    halt:bool = False
    text:str = ''
    kbd:object = None

    if phrase == "start reg":
        halt = True
        text = S["enter_password"]
        level = 2
    else:
        level, text, kbd = FirstMessage(S)

    return level, text, kbd, halt

def ShowRules(S: dict[str, str], phrase: str, level: int, lang: str, aid: int) -> tuple[int, str, object, str, bool, bool]:

    halt:bool = False
    text:str = ''
    kbd:object = None
    prmode:str = ''
    fixed:bool = False

    if Password(phrase, aid) or StatusReg(aid):
        halt = True
        text = S["global_rules"]
        kbd = forall.GoToAdmin(language_dictionary_for_all.String[lang]["main_menu_kb"])
        prmode = "HTML"
        fixed = True
        level = 3
    else:
        text = S["wrong_pass"]
    
    return level, text, kbd, prmode, fixed, halt