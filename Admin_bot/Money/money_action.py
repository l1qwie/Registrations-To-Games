from Admin_bot.Money.money_database import MoneyInf, SelectClient, SelectCountClient, SelecTWaitingClients, SelectClientNickname, SelectCountHowManyGame, SelectInfAboutClientGame, CountClientGames, ScheduleOfGames, SelectClientBeforeGameId, SelectWaitGameId
from Admin_bot.Money.money_database import Paid as dbPaid
from Admin_bot.Money.money_keyboard import DirectionsOfMoney, CallOrConfirm
from Admin_bot.Clients.clients_database import SelectAllInf
import language_dictionary_for_all
import used_by_everyone as forall




def ChooseMoneyDirection(S: dict[str, str], language: str) -> tuple[int, str, object]:
    return (1, S["choose_money_dir"], DirectionsOfMoney(S["money_stat"], S["money_paid_act"], language_dictionary_for_all.String[language]["main_menu_kb"]))

def CreateStrFromListTuple(inf: list[tuple[str, int, int, int]], S: dict[str, str], how: bool) -> str:
    text:str = ''
    i:int = 0
    while i < len(inf):
        if how:
            text = S["money_have"] % (inf[i][0], inf[i][2])
        else:
            text = S["money_have"] % (inf[i][0], inf[i][3])
        i += 1
    return text

def StartAct(S: dict[str, str], phrase: str, language: str, level: int, clients_launch_point: int, act: str, direction: str, halt: bool, prmode: str) -> tuple[int, str, str, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    names:list[tuple[int, str, str]] = []
    length:int = -1
    inf:list[tuple[str, int, int, int]] = []

    if phrase in ("paid action", "see stat"):
        halt = True
        level = 2
        direction = phrase
        if phrase == "see stat":
            prmode = "HTML"
            inf = MoneyInf()
            if inf != []:
                text = S["see_stat1"] + CreateStrFromListTuple(inf, S, True) + "\n" + S["see_stat2"] + CreateStrFromListTuple(inf, S, False)
                kbd = forall.GoToAdmin(language_dictionary_for_all.String[language]["main_menu_kb"])
            else:
                text = S["no_stat"] + language_dictionary_for_all.String[language]["main_menu_text"]
                kbd = forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"])
                level = 3
                act = "divarication"
        else:
            names = SelectClient(7, clients_launch_point)
            if names != []:
                length = SelectCountClient()
                text = S["choose_your_debtor"]
                kbd = forall.KeyboardWithClientsNames(names, 7, clients_launch_point, length, language)
            else:
                text = S["no_debtors"] + language_dictionary_for_all.String[language]["main_menu_text"]
                kbd = forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"])
                level = 3
                act = "divarication"
    else:
        (level, text, kbd) = ChooseMoneyDirection(S, language)
    
    return (level, direction, act, text, kbd, halt, prmode)


def InputUserId(S: dict[str, str], phrase: str, user_id: int, level: int, direction: str, language: str, clients_launch_point: int, prmode: str, halt: bool) -> tuple[int, int, int, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    i:int = 0
    nickname:str = ''
    game_ids:list[int] = []
    sport:str = ''
    date:int = -1
    time:int = -1
    price:int = -1
    currency:str = ''
    cl_seats:int = -1
    payment:str = ''
    _direction_:str = ''
    _act_:str = ''
    _halt_:bool = False

    if forall.IntCheck(phrase):
        if SelecTWaitingClients(int(phrase)):
            halt = True
            user_id = int(phrase)
            level = 3
            prmode = "HTML"
            nickname = SelectClientNickname(int(phrase))
            game_ids = SelectCountHowManyGame(int(phrase))
            name, lastname, phone, fromwhere, lang = SelectAllInf(user_id)
            phone_str = str(phone)
            if name == "no_data":
                name = language_dictionary_for_all.String[language]["no_data"]
            elif lastname == "no_data":
                lastname = language_dictionary_for_all.String[language]["no_data"]
            elif phone_str == "no_data":
                phone_str = language_dictionary_for_all.String[language]["no_data"]
            elif fromwhere == "no_data":
                fromwhere = language_dictionary_for_all.String[language]["no_data"]
            elif lang == "no_data":
                lang = language_dictionary_for_all.String[language]["no_data"]
            text = S["user_inf"] % (name, lastname, phone_str, fromwhere, lang)

            while i < len(game_ids):
                (sport, date, time, price, currency, cl_seats, payment) = SelectInfAboutClientGame(game_ids[i], user_id  )
                sum = price * cl_seats
                text += S["cl_game_inf"] % (sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), sum, currency, cl_seats, payment)
                i += 1

            kbd = CallOrConfirm(S["call"], S["paided"], language_dictionary_for_all.String[language]["main_menu_kb"], nickname)
        else:
            (level, _direction_, _act_, text, kbd, _halt_, prmode) = StartAct(S, direction, language, level, clients_launch_point, _act_, _direction_, _halt_, prmode)
    else:
        if phrase == "next page":
            clients_launch_point += 7
        elif phrase == "previous page":
            clients_launch_point += -7
        (level, _direction_, _act_, text, kbd, _halt_, prmode) = StartAct(S, direction, language, level, clients_launch_point, _act_, direction, _halt_, prmode)
    return (level, clients_launch_point, user_id, text, kbd, halt, prmode)

def Paid(S:dict[str, str], language: str, user_id: int, game_id: int) -> tuple[int, str, object, str]:
    dbPaid(user_id, game_id)
    return (3, S["client_paided"] + language_dictionary_for_all.String[language]["main_menu_text"], forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"]), "divarication")

def InputPaided(S: dict[str, str], phrase: str, user_id: int, language: str, game_launch_point: int, act: str, halt: bool, level: int, prmode: str) -> tuple[int, str, str, object, bool, str]:
    text:str = ''
    kbd: object = None
    number_of_games:int = -1
    _user_id_:int = -1
    _direction_:str = ''
    _clients_launch_point_:int = -1
    _prmode_:str = ''
    _halt_:bool = False

    if phrase == "paided":
        halt = True
        level = 4
        number_of_games = CountClientGames(user_id)
        print("????", number_of_games)
        if number_of_games > 1:
            schedule_input:list[tuple[int, str, int, int]] = ScheduleOfGames(user_id, 7, game_launch_point)
            _schedule_, schedule_output = forall.SheduleStr([], schedule_input, language)
            text = S["choose_game"]
            kbd = forall.Schedule(schedule_output, 7, game_launch_point, '', number_of_games)
        else:
            game_id = SelectClientBeforeGameId(user_id)
            (level, text, kbd, act) = Paid(S, language, user_id, game_id)
    else:
        (level, _clients_launch_point_, _user_id_, text, kbd, _halt_, prmode) = InputUserId(S, str(user_id), _user_id_, level, _direction_, language, _clients_launch_point_, _prmode_, _halt_)
    return (level, act, text, kbd, halt, prmode)

def InputGameId(S: dict[str, str], phrase: str, user_id: int, level: int, language: str, game_launch_point: int, act: str, halt: bool) -> tuple[int, int, str, str, object, bool]:
    text:str = ''
    kbd:object = None
    _act_:str = ''
    _halt_:bool = False
    _prmode_:str = ''

    if forall.IntCheck(phrase):
        if SelectWaitGameId(int(phrase), user_id):
            halt = True
            (level, text, kbd, act) = Paid(S, language, user_id, int(phrase))
        else:
            (level, _act_, text, kbd, _halt_, _prmode_) = InputPaided(S, "paided", user_id, language, game_launch_point, _act_, _halt_, level, _prmode_)
    else:
        if phrase == "next page":
            game_launch_point += 7
        elif phrase == "previous page":
            game_launch_point += -7    
        (level, _act_, text, kbd, _halt_, _prmode_) = InputPaided(S, "paided", user_id, language, game_launch_point, _act_, _halt_, level, _prmode_)
    return (level, game_launch_point, act, text, kbd, halt)

def HeadOfPaid(S: dict[str, str], phrase: str, language: str, level: int, direction: str,user_id: int, clients_launch_point: int, game_launch_point: int, act: str, halt: bool) -> tuple[int, int, int, int, str, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    prmode:str = ''

    if level == 2:
        (level, clients_launch_point, user_id, text, kbd, halt, prmode) = InputUserId(S, phrase, user_id, level, direction, language, clients_launch_point, prmode, halt)
    elif level == 3:
        (level, act, text, kbd, halt, prmode) = InputPaided(S, phrase, user_id, language, game_launch_point, act, halt, level, prmode)
    elif level == 4:
        (level, game_launch_point, act, text, kbd, halt) = InputGameId(S, phrase, user_id, level, language, game_launch_point, act, halt)
    else:
        assert(False)
    return (level, user_id, clients_launch_point, game_launch_point, act, text, kbd, halt, prmode)