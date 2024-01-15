from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testDataFitting
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Money.money_keyboard import DirectionsOfMoney
from Admin_bot.Money.tests.money_paid import HeadFunc
from Admin_bot.Money.money_database import MoneyInf, SelectCountClient, SelectClient
from Admin_bot.Money.money_action import CreateStrFromListTuple
from Admin_bot.language_dictoinary import String as S
import language_dictionary_for_all
import used_by_everyone as forall


def Directions(text: str, kbd: object, lang: str):
    assert(text == S[lang]["choose_money_dir"])
    assert(kbd == DirectionsOfMoney(S[lang]["money_stat"], S[lang]["money_paid_act"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(1 == testSelectLevel(738070596))

def ShowAllMoneyStat(text: str, kbd: object, lang: str, phrase: str, prmode: str):
    inf:list[tuple[str, int, int, int]] = MoneyInf()
    if inf != []:
        assert(text == S[lang]["see_stat1"] + CreateStrFromListTuple(inf, S[lang], True) + "\n" + S[lang]["see_stat2"] + CreateStrFromListTuple(inf, S[lang], False))
        assert(kbd == forall.GoToAdmin(language_dictionary_for_all.String[lang]["main_menu_kb"]))
        assert(phrase == testSelectSomthingColumn(738070596, "direction"))
        assert(2 == testSelectLevel(738070596))
        assert(prmode == "HTML")
    else:
        assert(text == S[lang]["no_stat"] + language_dictionary_for_all.String[lang]["main_menu_text"])
        assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
        assert(3 == testSelectLevel(738070596))
        assert("divarication" == testSelectSomthingColumn(738070596, "action"))

def SeeDebtors(text: str, kbd: object, lang: str, names: list[tuple[int, str, str]], launch_point: int, phrase: str):
    length:int = SelectCountClient()
    assert(text == S[lang]["choose_your_debtor"])
    assert(kbd == forall.KeyboardWithClientsNames(names, 7, launch_point, length, lang))
    assert(2 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "direction"))

def NoDebtors(text: str, kbd: object, lang: str):
    assert(text == S[lang]["no_debtors"] + language_dictionary_for_all.String[lang]["main_menu_text"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))


def ChooseMoneyDirection(first: list[str], lang: str):
    item:str = ''
    for item in first:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        Directions(text, kbd, lang)
        assert(chattext == '')
        assert(chatkbd == None)
        assert(prmode == '')
        assert(halt == False)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)

def StartAct(directions: list[str], lang: str):
    item:str = ''
    for item in directions:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            if item == "see stat":
                ShowAllMoneyStat(text, kbd, lang, item, prmode)
            else:
                launch_point = testSelectSomthingColumn(738070596, "client_launch_point")
                names:list[tuple[int, str, str]] = SelectClient(7, launch_point)
                if names != []:
                    SeeDebtors(text, kbd, lang, names, launch_point, item)
                else:
                    NoDebtors(text, kbd, lang)
        else:
            Directions(text, kbd, lang)
        assert(chattext == '')
        assert(chatkbd == None)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)






def DirectionOfActionActivities(alloflist:list[str], lang: str, level: int):
    testDataFitting("money", level, 738070596)
    direction = testSelectSomthingColumn(738070596, "direction")
    if direction not in ("paid action", "see stat"):
        if level == 0:
            ChooseMoneyDirection(alloflist, lang)
        elif level == 1:
            StartAct(alloflist, lang)
        else:
            assert(False)
    else:
        if direction == "paid action":
            HeadFunc(alloflist, lang, level)
        elif direction == "see stat":
            alloflist = ["see stat"]
            StartAct(alloflist, lang)