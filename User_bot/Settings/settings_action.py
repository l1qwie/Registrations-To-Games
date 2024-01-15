from User_bot.Settings.settings_keyboard import ChangeOrDel, ChangeLang, Languages, OptionGameUser, WhatChange
from User_bot.Settings.settings_database import CreateTableForUser, FindUserRecords, SelAllUserGames, ChangeLanguage, TryToFFindGameid, InfGameUser, CountUserGames, DeleteUserGame, SelectPaymentStatus, SelectSeats, SelectSomeData, UpdateSeats, SelectPaymethod
from User_bot.Settings.settings_database import ChangePaymethod as dbChangePaymethod
from User_bot.Registration.registration_database import WhatAboutMoney
from User_bot.language_dictionary import Strings as newS
import language_dictionary_for_all
import used_by_everyone as forall
import subprocess

def HTML(html_table: str, name: str) -> str:
    with open(name, "w", encoding="UTF-8") as html_file:
        html_file.write('<html><head><meta charset="UTF-8"></head><body>')
        
        html_file.write('<style>table {margin: 0 auto; text-align: center;}</style>')
        html_file.write('<style>td {padding-top: 10px; padding-bottom: 10px;}</style>')
        html_file.write('<style>th {font-size: 25px; padding: 10px; color: #006400;}</style>')
        html_file.write("</head><body>")
        html_file.write('<style>body {background-color: #C0C0C0; color: #000000;}</style>')
        html_file.write(html_table)
        html_file.write("</body></html>")

    with open(name, "r", encoding="UTF-8") as html_file:
        return html_file.read()


def CreateHtmlFileForUser(S: dict[str, str], id: int):

    data:list[tuple[int, str, str, int, int]]= []
    html_table:str = ''
    row:tuple[int, str, str, int, int]
    seats:int = -1
    payment:str = ''
    sport:str = ''
    date:int = -1
    date_str:str = ''
    time:int = -1
    time_str:str = ''
    sport_us:str = ''
    payment_us:str = ''

    data = CreateTableForUser(id)
    html_table = "<table>"
    html_table += f"<tr><th>{S['sport_for_html']}</th><th>{S['date_for_html']}</th><th>{S['time_for_html']}</th><th>{S['seats_for_html']}</th><th>{S['paymethod_for_html']}</th></tr>"
    for row in data:
        seats, payment, sport, date, time = row
        time_str = forall.CreateTimeStr(time)
        date_str = forall.CreateDateStr(date)

        sport_us = S[sport]
        payment_us = S[payment]
        
        print("YA!!!", payment_us)
        html_table += f"<tr><td>{sport_us}</td><td>{date_str}</td><td>{time_str}</td><td>{seats}</td><td>{payment_us}</td></tr>"
    html_table += "</table>"
    HTML(html_table, "personalhtml.html")


def TypeOfSetting(S: dict[str, str], uid: int) -> tuple[int, str, object, bool, str, str]:

    halt:bool = False #bool
    result:subprocess.CompletedProcess[str]
    img:str = ''
    text:str = '' 
    kbd:object = None
    res:bool = FindUserRecords(uid)
    level:int = 1
    act:str = "user records"

    text = S["what_set"]
    if res:
        halt = True
        CreateHtmlFileForUser(S, uid)
        result = subprocess.run("User_bot\\wkhtmltoimage User_bot\\personalhtml.html User_bot\\PersonalSchedule.jpg", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("Файлы созданы и данные в них записаны.")
            img = 'User_bot\\PersonalSchedule.jpg'
            kbd = ChangeOrDel(S["set_lan"], S["my_games"], S["main_menu"])
        else:
            print('Произошла ошибка:')
            print(result)
            text = S["somthing_happend"]
            kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
            level = 3
            act = "divarication"
    elif res == False:
        kbd = ChangeLang(S["set_lan"], S["main_menu"])
    
    return level, text, kbd, halt, img, act

def ChooseDiractions(S: dict[str, str], phrase: str, uid: int, limit: int, launch_point: int, what_setting: str, user_lang: str) -> tuple[int, str, str, str, int, str, object, bool, str]:

    halt:bool = False
    _halt_:bool = False
    text:str = ''
    kbd:object = None
    img:str = ''
    schedule_from_database:list[tuple[int, str, int, int]] = []
    game_id:int = -1
    sport:str = ''
    date_int:int = -1
    date_str:str = ''
    time_int:int = -1
    time_str:str = ''
    level:int = -1
    act:str = "user records"
    schedule:list[tuple[str, str, str, str]] = []

    if phrase == "change language":
        halt = True
        level = 2
        what_setting = phrase
        text = S["what_lang"] % (S[user_lang])
        kbd = Languages(S["en"], S["ru"], S["tur"], S["main_menu"])
    elif phrase == "seting regs":
        what_setting = phrase
        text = S["choose_ur_game"]
        schedule_from_database = SelAllUserGames(uid, limit, launch_point)

        for game_id, sport, date_int, time_int in schedule_from_database:
            sport = S[sport]
            date_str = forall.CreateDateStr(date_int)
            time_str = forall.CreateTimeStr(time_int)
            schedule.append((str(game_id), sport, date_str, time_str))
        kbd = forall.Schedule(schedule, limit, launch_point, '', len(schedule_from_database))
        level = 2
    else:
        level, text, kbd, _halt_, img, act = TypeOfSetting(S, uid)

    return level, user_lang, act, what_setting, launch_point, text, kbd, halt, img

def SetActions(S: dict[str, str], phrase: str, what_setting: str, uid: int, limit: int, launch_point: int, user_lang: str, set_game_id: int, prmode: str) -> tuple[int, str, int, str, int, str, str, object, bool, str]:

    halt:bool = False
    _halt_:bool = False
    text:str = ''
    kbd:object = None
    level:int = -1
    _e_:str= ''
    img:str = ''
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
    counter_games:int = -1

    act:str = "user records"

    if what_setting == "change language":
        if phrase in ("en", "ru", "tur"):
            halt = True
            ChangeLanguage(phrase, uid)
            user_lang = phrase
            text = newS[phrase]["lang_changed"]
            kbd = forall.Options(newS[phrase]["first_option"], newS[phrase]["second_option"], newS[phrase]["third_option"], newS[phrase]["fourth_option"])
            act = "divarication"
            level = 3
        else:
            level, user_lang, act, _e_, launch_point, text, kbd, _halt_, img = ChooseDiractions(S, what_setting, uid, limit, launch_point, what_setting, user_lang)
    elif what_setting == "seting regs":
        if phrase in ("previous page", "next page"):
            halt = True
            limit = 7
            if phrase == "previous page":
                launch_point -= 7
            elif phrase == "next page":
                launch_point += 7
            level, user_lang, act, _e_, launch_point, text, kbd, _halt_, img = ChooseDiractions(S, what_setting, uid, limit, launch_point, what_setting, user_lang)
        elif forall.IntCheck(phrase):
            if TryToFFindGameid(int(phrase)):
                level = 3
                set_game_id = int(phrase)
                sport, date, time, latitude, longitude, address, price, currency, seats, payment, payment_status = InfGameUser(uid, set_game_id)
                date_str = forall.CreateDateStr(date)
                time_str = forall.CreateTimeStr(time)
                sum_for_pay = price * seats

                text = S["inf_game_user"] % (S[sport], date_str, time_str, address, seats, S[payment], sum_for_pay, currency, S[str(payment_status)], latitude, longitude)
                prmode = "HTML"
                counter_games = CountUserGames(uid)
                kbd = OptionGameUser(S["delete_game"], S["change_game"], S["see_more_games"], S["main_menu"], counter_games)
            else:
                level, user_lang, act, _e_, launch_point, text, kbd, _halt_, img = ChooseDiractions(S, what_setting, uid, limit, launch_point, what_setting, user_lang)
        else:
            level, user_lang, act, _e_, launch_point, text, kbd, _halt_, img = ChooseDiractions(S, what_setting, uid, limit, launch_point, what_setting, user_lang)
    else:
        level, user_lang, act, _e_, launch_point, text, kbd, _halt_, img = ChooseDiractions(S, what_setting, uid, limit, launch_point, what_setting, user_lang)

    return level, act, launch_point, user_lang, set_game_id, prmode, text, kbd, halt, img

def GameSettings(S: dict[str, str], phrase: str, uid: int, game_id: int, what_setting: str, change_action_with_game: str, user_lang: str, prmode: str):
    halt:bool = False
    text:str = ''
    kbd:object = None
    level:int = -1
    _str_:str = ''
    _img_:str = ''
    status:bool = False 
    _bool_:bool = False
    _user_choose_lang_:str = ''
    _set_game_id_:int  = -1
    _limit_:int = -1
    _launch_point_:int = -1
    _prmode_:str = ''
    act:str = "user records"

    if phrase in ("delete my game", "change my game", "see more games"):
        halt = True
        change_action_with_game = phrase
        if phrase == "delete my game":
            DeleteUserGame(uid, game_id)
            text = S["game_was_del"]
            kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
            act = "divarication"
            level = 3
        elif phrase == "change my game":
            text = S["try_to_change_your_game"]
            status = SelectPaymentStatus(uid, game_id)
            kbd = WhatChange(S["change_seats"], S["change_payment"], S["main_menu"], status)
            level = 4
        elif phrase == "see more games":
           level, user_lang, act, _e_, _launch_point_, text, kbd, _halt_, _img_ = ChooseDiractions(S, what_setting, uid, 7, 0, what_setting, user_lang)
    else:
        level, act, _launch_point_, _user_choose_lang_, _set_game_id_, prmode, text, kbd, _bool_, _img_ = SetActions(S, str(game_id), what_setting, uid, _limit_, _launch_point_, user_lang, game_id, _prmode_)

    return level, act, change_action_with_game, text, kbd, halt, prmode

def SetiingsAction(S: dict[str, str], phrase: str, game_id: int, change_action_with_game: str, uid: int, what_we_will_change: str, language: str) -> tuple[int, str, str, object, bool]:

    halt:bool = False
    text:str = ''
    kbd:object = None
    money:int = -1
    currency:str = ''
    user_seats:int = -1
    global_seats:int = -1
    level:int = -1
    _str_:str = ''
    _bool_:bool = False 
    _act_:str = ''
    _limit_:int = -1
    _launch_point_:int = -1
    _what_setting_:str = ''
    _user_lang_:str = ''
    _prmode_:str = ''


    if phrase in ("change seats", "change payment"):
        halt = True
        what_we_will_change = phrase
        level = 5
        if phrase == "change seats":
            money, currency = WhatAboutMoney(game_id)
            user_seats, global_seats = SelectSeats(game_id, uid)
            text = S["discussion_seats_with_rules"] % (user_seats + global_seats, money, currency)
            kbd = forall.FrequentChoice(S["alone"], S["with_two"], S["with_three"])
        elif phrase == "change payment":
            text = S["choose_payment"]
            kbd = forall.KbPay(S["pay_online"], S["pay_cash"], language_dictionary_for_all.String[language]["main_menu_kb"])
    else:
        level, _act_, _str_, text, kbd, _bool_, _prmode_ = GameSettings(S, change_action_with_game, uid, game_id, _what_setting_, change_action_with_game, _user_lang_, _prmode_)
    
    return level, what_we_will_change, text, kbd, halt

def IntermediateAction(S: dict[str, str], phrase: str, game_id: int, uid: int, what_we_will_change: str, new_paymethod: str, language: str) -> tuple[int, str, str, str, str, object, bool]:

    halt:bool = False
    _str_:str = ''
    _bool_:bool = False
    potential_seats:int = -1
    user_seats:int = -1
    global_seats:int = -1
    potential_seats_sum:int = -1
    text:str = ''
    kbd:object = None
    level:int = -1
    img:str = ''
    price:int = -1
    currency:str = ''
    payment_status:int = -1
    _change_action_with_game_:str = ''
    act:str = "user records"

    if what_we_will_change == "change seats":
        halt = True
        if forall.IntCheck(phrase):
            potential_seats = int(phrase)
            user_seats, global_seats, price, currency, payment_status = SelectSomeData(game_id, uid)
            potential_seats_sum = (user_seats + global_seats) - potential_seats
            if potential_seats_sum >= 0:
                UpdateSeats(uid, game_id, potential_seats_sum, potential_seats)
                if potential_seats > user_seats and payment_status == 0:
                    text = S["seats_changed_if_not_pay"] % ((potential_seats * price), currency)
                elif user_seats >= potential_seats and payment_status == 0:
                    text = S["seats_changed_if_pay_maybe"] % ((user_seats-potential_seats) * price, currency)
                elif user_seats > potential_seats and payment_status == 1:
                    text = S["seats_changed_if_pay"] % ((user_seats * price)-(potential_seats * price), currency)
                elif potential_seats > user_seats and payment_status == 1:
                    text = S["seats_changed_if_pay_but"] % ((potential_seats * price)-(user_seats * price), currency)
                kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
                level = 3
                act = "divarication"
            else:
                if global_seats == 0:
                    text = S["no_seats"]
                else:
                    text = S["seats_cant_changed"]
                kbd = forall.FrequentChoice(S["alone"], S["with_two"], S["with_three"])
        else:
            level, _str_, text, kbd, _bool_ = SetiingsAction(S, what_we_will_change, game_id, _change_action_with_game_, uid, what_we_will_change, language)
    elif what_we_will_change == "change payment":
        payment_status = SelectPaymethod(game_id, uid)
        if payment_status == 0:
            if phrase in ("card", "cash"):
                dbChangePaymethod(game_id, uid, phrase)
                new_paymethod = phrase
                if phrase == "card":
                    text = S["payment_canged_card"]
                    kbd = forall.Papara(S["pay"], S["next"])
                    img = 'qr.jpg'
                    level = 6
                elif phrase == "cash":
                    text = S["payment_canged_cash"]
                    kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
                    level = 3
                    act = "divarication"
            else:
                level, _str_, text, kbd, _bool_ = SetiingsAction(S, what_we_will_change, game_id, _change_action_with_game_, uid, what_we_will_change, language)
        else:
            text = S["Ups_cant_change_payment"]
            kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
            level = 3
            act = "divarication"
    else:
        level, _str_, text, kbd, _bool_ = SetiingsAction(S, what_we_will_change, game_id, _change_action_with_game_, uid, what_we_will_change, language)
    
    return level, act, new_paymethod, img, text, kbd, halt

def ChangePaymethod(S: dict[str, str], phrase: str, new_paymethod: str, game_id: int, uid: int, what_we_will_change: str, img: str, language: str) -> tuple[int, str, str, object, bool, str]:

    text:str = '' #str
    kbd:object = None #list
    level:int = -1 #int
    _act_:str = ''
    _new_paymethod_:str = '' #str
    _halt_:bool = False #bool
    halt:bool = False #bool
    
    act = "user records"

    if phrase == "Next":
        halt = True
        text = S["main_menu"]
        kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
        level = 3
        act = "divarication"
    else:
        level, _act_, _new_paymethod_, img, text, kbd, _halt_ = IntermediateAction(S, new_paymethod, game_id, uid, what_we_will_change, new_paymethod, language)

    return level, act, text, kbd, halt, img


