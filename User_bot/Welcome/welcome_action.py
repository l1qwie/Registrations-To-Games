from User_bot.Welcome.welcome_keyboard import Registration, Further
from User_bot.Welcome.welcome_database import CompletionOfRegistration
import used_by_everyone as forall



def GreetingsToUser(S: dict[str, str]) -> tuple[int, str, object]:
    return 1, S["welcome_to_bot"], Registration(S["reg"])


def WarningRules(S: dict[str, str], phrase: str) -> tuple[int, str, object, bool]:

    halt:bool = False #bool
    text:str = '' #str
    kbd:object = None #list
    level:int = -1 #int

    if phrase == "GoReg":
        halt = True
        text = S["bot_rules"]
        kbd = Further(S["all_right"])
        level = 2
    else:
        level, text, kbd = GreetingsToUser(S)
    return level, text, kbd, halt
#end WarningRules

def GoToOptions(S: dict[str, str], uid: int, phrase: str) -> tuple[int, str, str, object, bool]:

    halt:bool = False
    text:str = ''
    kbd:object = None
    level:int = -1
    uact:str = ''
    _halt_:bool = False


    if phrase == "GoNext":
        halt = True
        CompletionOfRegistration(uid)
        text = S["choose_option"]
        kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
        level = 3
        uact = "divarication"
    else:
        level, text, kbd, _halt_ = WarningRules(S, "GoReg")
    return level, uact, text, kbd, halt
#end GoToOptions