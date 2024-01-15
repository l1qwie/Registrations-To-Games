from User_bot.Registration.registration_database import SelectDate, SelectTime, SelectAdressGame, SelectAllScheduleData, SelectAllGId, WhatAboutMoney, SelectSport, ComNewRegGameUser, HowMutchSeats, BalanceOfTheUniverse
import language_dictionary_for_all
import used_by_everyone as forall
#Executive functions
def RemainingSeats(id: int, seat: int) -> bool:

    free_seats = None #int
    result = None #bool

    free_seats = HowMutchSeats(id)
    if seat > free_seats:
        result = False
    else:
        result = True
    return result

def InfAboutNewGameUser(S: dict[str, str], sport_source: str, payment_source: str, game_id_source: int, uid: int) -> tuple[str, str, str, list[float], str]:

    sport:str = '' #str
    payment:str = '' #str
    date:str = '' #str
    time:str = '' #str
    address:list[float] = []
    sport = S[sport_source] 
    payment = S[payment_source]
    date = forall.CreateDateStr(SelectDate(game_id_source))
    time = forall.CreateTimeStr(SelectTime(game_id_source))
    address = SelectAdressGame(game_id_source)
    return sport, date, time, address, payment


#Actions functions
def PresentationScheduele(S: dict[str, str], limit: int, launch_point: int) -> tuple[int, int, str, object]:

    game_id:int = -1
    sport:str = ''
    date:int = 0
    date_str:str = ''
    time:int = 0
    time_str:str = ''
    seats:int = -1
    text:str = '' 
    kbd:object = None
    level:int = -1

    schedule:list[tuple[str, str, str, str, str]] = []

    schedule_data = SelectAllScheduleData(limit, launch_point)
    for game_id, sport, date, time, seats in schedule_data:
        sport = S[sport]
        date_str = forall.CreateDateStr(date)
        time_str = forall.CreateTimeStr(time)
        schedule.append((str(game_id), sport, date_str, time_str, str(seats)))

    print(schedule)
    text = S["what_interesing"]
    kbd = forall.Schedule(schedule, limit, launch_point, S["free_seats"], 0)
    level = 1
    return launch_point, level, text, kbd

def ChooseSeats(S: dict[str, str], phrase: str, game_id: int, limit: int, launch_point: int) -> tuple[int, int, int, str, object, bool]:

    halt:bool = False
    money:int = -1
    currency:str = '' 
    text:str = ''
    kbd:object = None
    level:int = -1 

    if phrase in SelectAllGId():
        halt = True
        game_id = int(phrase)
        money, currency = WhatAboutMoney(game_id)
        text = S["discussion_seats"] % (money, currency)
        kbd = forall.FrequentChoice(S["alone"], S["with_two"], S["with_three"])
        level = 2
    else:
        if phrase == "next page":
            launch_point += 7
        elif phrase == "previous page":
            launch_point -= 7
        launch_point, level, text, kbd = PresentationScheduele(S, limit, launch_point)
    return level, game_id, launch_point, text, kbd, halt


def ChoosePay(S: dict[str, str], uid: int, phrase: str, game_id: int, launch_point: int, seats: int, language: str) -> tuple[int, int, str, object, bool]:

    halt:bool = False
    text:str = ''
    kbd:object = None 
    level:int = -1
    _limit_:int = -1
    _launch_point_:int = -1
    _game_id_:int = -1
    _halt_:bool = False

    if forall.IntCheck(phrase):
        if RemainingSeats(uid, int(phrase)):
            halt = True
            seats = int(phrase)
            text = S["choose_payment"]
            kbd = forall.KbPay(S["pay_online"], S["pay_cash"], language_dictionary_for_all.String[language]["main_menu_kb"])
            level = 3
        else:
            text = S["wrond_number"]
            level = 2
            kbd = forall.FrequentChoice(S["alone"], S["with_two"], S["with_three"])
    else:
        level, _game_id_, _launch_point_, text, kbd, _halt_ = ChooseSeats(S, str(game_id), game_id, _limit_, launch_point)
    return level, seats, text, kbd, halt

def CardPayment(S: dict[str, str], game_id: int, seats: int, uid: int, phrase: str, sport: str, payment: str, language: str) -> tuple[int, str, str, str, str, object, bool, str, list[float], str]:

    text:str = ''
    kbd:object = None
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    halt:bool = False
    money:int = -1
    currency:str = ''
    price:int = -1
    level:int = -1
    _game_id_:int = -1
    _seats_:int = -1
    _halt_:bool = False
    act:str = "reg to games"
    _launch_point_:int = -1
    sport = SelectSport(game_id)

    if phrase in ("card", "cash"):
        halt = True
        payment = phrase
        if phrase == "card":
            money, currency = WhatAboutMoney(game_id)
            price = money * seats
            text = S["online_oplata"] % (price, currency)
            kbd = forall.Papara(S["pay"], S["next"])
            img = 'qr.jpg'
            level = 4
        else:
            level, act, text, kbd, prmode, address = BestWishes(S, game_id, seats, uid, sport, payment)
    else:

        level, _seats_, text, kbd, _halt_ = ChoosePay(S, uid, str(seats), _game_id_, _launch_point_, seats, language)
    return level, payment, act, sport, text, kbd, halt, prmode, address, img

def BestWishes(S: dict[str, str], game_id: int, seats: int, uid: int, sport: str, payment: str) -> tuple[int, str, str, object, str, list[float]]:

    date:str = ''
    time:str = ''
    address:list[float] = []
    money:int = -1
    currency:str = ''
    finalyprice:int = -1
    text:str = ''
    kbd:object = None
    prmode:str = ''
    level:int = -1 
    act:str = ''
    upd_seats:int = -1

    sport, date, time, address, payment = InfAboutNewGameUser(S, sport, payment, game_id, uid)
    money, currency = WhatAboutMoney(game_id)
    finalyprice = money * seats
    text = S["grac_to_reg"] % (sport, date, time, seats, payment, finalyprice, currency, address[0], address[1])
    prmode = "HTML"
    kbd = forall.Options(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"])
    level = 3
    act = "divarication"
    ComNewRegGameUser(uid)
    upd_seats = HowMutchSeats(uid) - seats
    BalanceOfTheUniverse(upd_seats, uid)
    return level, act, text, kbd, prmode, address
