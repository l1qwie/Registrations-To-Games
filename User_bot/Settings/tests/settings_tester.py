from User_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testCheckDelGames, testChangedPaymentOrWhat, testDataFitting
from User_bot.Main.main_action import DispatchPhrase
from User_bot.language_dictionary import Strings as S
from User_bot.Settings.settings_keyboard import ChangeOrDel, ChangeLang, Languages, OptionGameUser, WhatChange
from User_bot.Settings.settings_database import SelAllUserGames, TryToFFindGameid, CountUserGames, SelectPaymentStatus, SelectSeats, SelectSomeData, InfGameUser, FindUserRecords, SelectPaymethod
from User_bot.Registration.registration_database import WhatAboutMoney
import used_by_everyone as forall
import language_dictionary_for_all

#action functions
def UserHaveGames(text: str, kbd: object, lang: str, img: str):
    assert(text == S[lang]["what_set"])
    assert(kbd ==  ChangeOrDel(S[lang]["set_lan"], S[lang]["my_games"], S[lang]["main_menu"]))
    assert(img == 'User_bot\\PersonalSchedule.jpg')
    assert(1 == testSelectLevel(738070596))

#assert(int(phrase) == testSelectSomthingColumn(738070596, "seats_reg_to_game"))

def UserDontHave(text: str, kbd: object, lang: str):
    assert(text == S[lang]["what_set"])
    assert(kbd == ChangeLang(S[lang]["set_lan"], S[lang]["main_menu"]))
    assert(1 == testSelectLevel(738070596))

def ChooseLanguage(text: str, kbd: object, lang: str, phrase: str):
    print(lang)
    assert(text == S[lang]["what_lang"] % (S[lang][lang]))
    assert(kbd == Languages(S[lang]["en"], S[lang]["ru"], S[lang]["tur"], S[lang]["main_menu"]))
    assert(phrase == testSelectSomthingColumn(738070596, "us_set_what_set"))
    assert(2 == testSelectLevel(738070596))

def ShowGames(text: str, kbd: object, lang: str, phrase: str):
    schedule_from_database:list[tuple[int, str, int, int]] = []
    game_id:int = -1
    sport:str = ''
    date_int:int = -1
    date_str:str = ''
    time_int:int = -1
    time_str:str = ''
    schedule:list[tuple[str, str, str, str]] = []
    launch_point:int = testSelectSomthingColumn(738070596, "us_set_lanuch_point")
    
    schedule_from_database = SelAllUserGames(738070596, 7, launch_point)
    for game_id, sport, date_int, time_int in schedule_from_database:
        sport = S[lang][sport]
        date_str = forall.CreateDateStr(date_int)
        time_str = forall.CreateTimeStr(time_int)
        schedule.append((str(game_id), sport, date_str, time_str))

    assert(text == S[lang]["choose_ur_game"])
    assert(phrase == testSelectSomthingColumn(738070596, "us_set_what_set"))
    assert(kbd == forall.Schedule(schedule, 7, launch_point, '', len(schedule_from_database)))
    assert(2 == testSelectLevel(738070596))

def SettingRegs(text: str, kbd: object, lang: str, prmode: str, what: str, phrase: str):
    if phrase in ("previous page", "next page"):
        ShowGames(text, kbd, lang, what)
        assert(prmode == '')
    elif forall.IntCheck(phrase):
        if TryToFFindGameid(int(phrase)):
            ShowInfAboutGame(text, kbd, lang, phrase, prmode)
        else:
            ShowGames(text, kbd, lang, what)
            assert(prmode == '')
    else:
        ShowGames(text, kbd, lang, what)
        assert(prmode == '')




def ChangeLanguage(text: str, kbd: object, phrase: str):
    assert(text == S[phrase]["lang_changed"])
    assert(kbd == forall.Options(S[phrase]["first_option"], S[phrase]["second_option"], S[phrase]["third_option"], S[phrase]["fourth_option"]))
    assert(phrase == testSelectSomthingColumn(738070596, "language"))
    assert(True == testSelectSomthingColumn(738070596, "custom_language"))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))

def ShowInfAboutGame(text: str, kbd: object, lang: str, phrase: str, prmode: str):
    sport:str = ''
    date:int = -1
    date_str:str = ''
    time:int = -1
    time_str:str = ''
    latitude:float = -1
    longitude:float = -1
    address:str = ''
    price:int = -1
    currency:str = ''
    seats:int = -1
    payment:str = ''
    payment_status:int = -1
    sum_for_pay:int = -1

    counter_games:int = CountUserGames(738070596)
    sport, date, time, latitude, longitude, address, price, currency, seats, payment, payment_status = InfGameUser(738070596, int(phrase))
    date_str = forall.CreateDateStr(date)
    time_str = forall.CreateTimeStr(time)
    sum_for_pay = price * seats

    assert(text == S[lang]["inf_game_user"] % (S[lang][sport], date_str, time_str, address, seats, S[lang][payment], sum_for_pay, currency, S[lang][str(payment_status)], latitude, longitude))
    assert(kbd == OptionGameUser(S[lang]["delete_game"], S[lang]["change_game"], S[lang]["see_more_games"], S[lang]["main_menu"], counter_games))
    print(prmode, "GDE YAA?")
    assert(prmode == 'HTML')

def DeleteGame(text: str, kbd: object, lang: str, game_id: int):
    assert(text == S[lang]["game_was_del"])
    assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))
    assert(True == testCheckDelGames(738070596, game_id))

def StartChangeGame(text: str, kbd: object, lang: str, game_id: int):
    assert(text == S[lang]["try_to_change_your_game"])
    status = SelectPaymentStatus(738070596, game_id)
    assert(kbd == WhatChange(S[lang]["change_seats"], S[lang]["change_payment"], S[lang]["main_menu"], status))
    assert(4 == testSelectLevel(738070596))

def ChooseWhatSet(text: str, kbd: object, lang: str, phrase: str, game_id: int):
    money:int = -1
    currency:str = ''
    user_seats:int = -1
    global_seats:int = -1

    assert(phrase == testSelectSomthingColumn(738070596, "us_set_what_we_will_change"))
    assert(5 == testSelectLevel(738070596))

    if phrase == "change seats":
        money, currency = WhatAboutMoney(game_id)
        user_seats, global_seats = SelectSeats(game_id, 738070596)
        assert(text == S[lang]["discussion_seats_with_rules"] % (user_seats + global_seats, money, currency))
        assert(kbd == forall.FrequentChoice(S[lang]["alone"], S[lang]["with_two"], S[lang]["with_three"]))
    elif phrase == "change payment":
        assert(text == S[lang]["choose_payment"])
        assert(kbd == forall.KbPay(S[lang]["pay_online"], S[lang]["pay_cash"], language_dictionary_for_all.String[lang]["main_menu_kb"] ))

def ChangeSeats(text: str, kbd: object, lang: str, phrase: str, game_id: int, prev_global_seats: int, user_seats: int, potential_seats_sum: int):
    _user_seats_:int = -1
    _global_seats_:int = -1

    if forall.IntCheck(phrase):
        potential_seats = int(phrase)
        _user_seats_, _global_seats_, price, currency, payment_status = SelectSomeData(game_id, 738070596)
        print("DATA FROM TESTER =", user_seats, prev_global_seats, price, currency, payment_status, "potential_seats_sum =", potential_seats_sum)
        if potential_seats_sum >= 0:
            if potential_seats > user_seats and payment_status == 0:
                assert(text == S[lang]["seats_changed_if_not_pay"] % ((potential_seats * price), currency))
            elif user_seats >= potential_seats and payment_status == 0:
                assert(text == S[lang]["seats_changed_if_pay_maybe"] % ((user_seats-potential_seats) * price, currency))
            elif user_seats > potential_seats and payment_status == 1:
                assert(text == S[lang]["seats_changed_if_pay"] % ((user_seats * price)-(potential_seats * price), currency))
            elif potential_seats > user_seats and payment_status == 1:
                assert(text == S[lang]["seats_changed_if_pay_but"] % ((potential_seats * price)-(user_seats * price), currency))
            assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
            assert(3 == testSelectLevel(738070596))
            assert("divarication" == testSelectSomthingColumn(738070596, "action"))
        else:
            if prev_global_seats == 0:
                assert(text == S[lang]["no_seats"])
                assert(kbd == forall.FrequentChoice(S[lang]["alone"], S[lang]["with_two"], S[lang]["with_three"]))
            else:
                assert(text == S[lang]["seats_cant_changed"])
                assert(kbd == forall.FrequentChoice(S[lang]["alone"], S[lang]["with_two"], S[lang]["with_three"]))
    else:
        will_change = testSelectSomthingColumn(738070596, "us_set_what_we_will_change")
        ChooseWhatSet(text, kbd, lang, will_change, game_id)

def PreparationToChangePaymethod(text: str, kbd: object, lang: str, phrase: str, game_id: int, img: str):
    payment_status = SelectPaymethod(game_id, 738070596)
    if payment_status == 0:
        if phrase in ("card", "cash"):
            assert(True == testChangedPaymentOrWhat(738070596, game_id, phrase))
            assert(phrase == testSelectSomthingColumn(738070596, "us_set_new_pay"))
            if phrase == "card":
                assert(text == S[lang]["payment_canged_card"])
                assert(kbd == forall.Papara(S[lang]["pay"], S[lang]["next"]))
                assert(img == 'qr.jpg')
                assert(6 == testSelectLevel(738070596))
            else:
                assert(text == S[lang]["payment_canged_cash"])
                assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
                assert(3 == testSelectLevel(738070596))
                assert("divarication" == testSelectSomthingColumn(738070596, "action"))
        else:
            will_change = testSelectSomthingColumn(738070596, "us_set_what_we_will_change")
            ChooseWhatSet(text, kbd, lang, will_change, game_id)
    else:
        assert(text == S[lang]["Ups_cant_change_payment"])
        assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
        assert(3 == testSelectLevel(738070596))
        assert("divarication" == testSelectSomthingColumn(738070596, "action"))

def GoTo(text: str, kbd: object, lang: str):
    assert(text == S[lang]["main_menu"])
    assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))


#header functions
def TypeOfSetting(first_message: list[str], lang: str):
    item:str = ''
    for item in first_message:
        testDataFitting("user records", 0, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if halt:
            UserHaveGames(text, kbd, lang, img)
        else:
            UserDontHave(text, kbd, lang)
            assert(img == '')
        assert(prmode == '')
        assert(address == [])
        assert(files_id == [])
        assert(typeoffile == [])
        assert(edit == False)

def ChooseDiractions(directions: list[str], lang: str):
    item:str = ''
    for item in directions:
        testDataFitting("user records", 1, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if halt:
            ChooseLanguage(text, kbd, lang, item)
            assert(img == '')
        else:
            if item == "seting regs":
                ShowGames(text, kbd, lang, item)
                assert(img == '')
            else:
                if FindUserRecords(738070596):
                    UserHaveGames(text, kbd, lang, img)
                else:
                    UserDontHave(text, kbd, lang)
                    assert(img == '')
        assert(prmode == '')
        assert(address == [])
        assert(files_id == [])
        assert(typeoffile == [])
        assert(edit == False)


def SetActions(chan_or_cont: list[str], lang: str):
    item:str = ''
    for item in chan_or_cont:
        testDataFitting("user records", 2, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        what = testSelectSomthingColumn(738070596, "us_set_what_set")
        if what == "change language":
            if halt:
                ChangeLanguage(text, kbd, item)
                assert(prmode == '')
            else:
                ChooseLanguage(text, kbd, lang, what)
                assert(prmode == '')
        elif what == "seting regs":
            SettingRegs(text, kbd, lang, prmode, what, item)
        assert(img == '')
        assert(address == [])
        assert(files_id == [])
        assert(typeoffile == [])
        assert(edit == False)


def GameSettings(direction_of_game: list[str], lang: str):
    item:str = ''
    for item in direction_of_game:
        testDataFitting("user records", 3, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        what = testSelectSomthingColumn(738070596, "us_set_what_set")
        if halt:
            assert(item == testSelectSomthingColumn(738070596, "us_set_act_game"))
            game_id:int = testSelectSomthingColumn(738070596, "us_set_game_id")
            if item == "delete my game":
                DeleteGame(text, kbd, lang, game_id)
            elif item == "change my game":
                StartChangeGame(text, kbd, lang, game_id)
            elif item ==  "see more games":
                ShowGames(text, kbd, lang, what)
        else:
            print(prmode, "A TUT KAK?")
            game_id:int = testSelectSomthingColumn(738070596, "us_set_game_id")
            SettingRegs(text, kbd, lang, prmode, what, str(game_id))
        assert(img == '')
        assert(address == [])
        assert(files_id == [])
        assert(typeoffile == [])
        assert(edit == False)

def SetiingsAction(seats_or_payment: list[str], lang: str):
    item:str = ''
    for item in seats_or_payment:
        testDataFitting("user records", 4, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        game_id:int = testSelectSomthingColumn(738070596, "us_set_game_id")
        if halt:
            ChooseWhatSet(text, kbd, lang, item, game_id)
        else:
            StartChangeGame(text, kbd, lang, game_id)
        assert(prmode == '')
        assert(img == '')
        assert(address == [])
        assert(files_id == [])
        assert(typeoffile == [])
        assert(edit == False)


def IntermediateAction(input_data: list[str], lang: str, prev_global_seats: int, user_seats: int, potential_seats_sum: int):
    item:str = ''
    for item in input_data:
        testDataFitting("user records", 5, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        game_id:int = testSelectSomthingColumn(738070596, "us_set_game_id")
        if halt:
            ChangeSeats(text, kbd, lang, item, game_id, prev_global_seats, user_seats, potential_seats_sum)
        else:
            PreparationToChangePaymethod(text, kbd, lang, item, game_id, img)
        assert(prmode == '')
        assert(address == []) 
        assert(files_id == [])
        assert(typeoffile == [])
        assert(edit == False)


def ChangePaymethod(go_to: list[str], lang: str):
    item:str = ''
    for item in go_to:
        testDataFitting("user records", 6, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if halt:
            GoTo(text, kbd, lang)
            assert(img == '')
        else:
            game_id:int = testSelectSomthingColumn(738070596, "us_set_game_id")
            new_pay:str = testSelectSomthingColumn(738070596, "us_set_new_pay")
            PreparationToChangePaymethod(text, kbd, lang, new_pay, game_id, img)
        assert(prmode == '')
        assert(address == []) 
        assert(files_id == [])
        assert(typeoffile == [])
        assert(edit == False)
