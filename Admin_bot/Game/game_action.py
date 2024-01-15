from Admin_bot.Game.game_keyboard import SaveorChange, OptionsOfChange, KindOfSport, GamesOptions, AnotherFunc
from Admin_bot.Game.game_database import NewScheduleGame, SelectGameId, ChangeColumnInt, ChangeColumnStr, ChangeColumnsFloat, SelectDataChanged, GameRemove, ScheduleOfGames, LengthOfGames
from Admin_bot.Main.main_database import SelectDataFromSchedule
import used_by_everyone as forall
import language_dictionary_for_all
import re
import datetime
from typing import Any

def ValidTime(hr: int, min: int):
    try:
        _ = datetime.time(hr, min)
        res = True
    except:
        res = False
    print("EMMMMMM", res, hr, min)
    return res

def ValidDate(d: int, m: int, y: int) -> bool:
    try:
        _ = datetime.date(y, m, d)
        res = True
    except:
        res = False
    return res

def TimeCheck(input_time: str, year: int, month: int, day: int):

    halt:bool = False
    time:int = -1
    time_match:str = ''
    components:list[Any] = []
    hour:int = -1
    minute:int = -1

    if re.findall(r'\d{1,2}[^0-9]+\d{1,2}', input_time):
        time_pattern = r'\d{1,2}[^0-9]+\d{1,2}'
        match = re.search(time_pattern, input_time)
        if match:
            time_match = match.group(0)
            components = re.findall(r'\d+', time_match)
            hour, minute = map(int, components)
            print(time_match, components, hour, minute)
            if ValidTime(hour, minute) and datetime.datetime(year, month, day, hour, minute) > datetime.datetime.now():
                halt = True
                time = (hour * 100) + minute
    return (halt, time)

def DateCheck(input_date: str) -> tuple[bool, int]:

    date:int = -1
    halt:bool = False
    date_match:str = ''
    components:list[Any] = []
    day:int = -1
    month:int = -1
    year:int = -1

    if re.findall(r'\d{1,2}[^0-9]+\d{1,2}[^0-9]+\d{4}', input_date):
        date_pattern = r'\d{1,2}[^0-9]+\d{1,2}[^0-9]+\d{4}'
        match = re.search(date_pattern, input_date)
        if match:
            date_match = match.group(0)
            components = re.findall(r'\d+', date_match)
            day, month, year = map(int, components)
            if ValidDate(day, month, year) and datetime.date(year, month, day) >= datetime.date.today():
                date = (day*1)+(month*100)+(year*10000)
                halt = True
    return (halt, date)

def TryToFindLocation(link: str):
    latitude:float = -1
    longitude:float = -1
    halt:bool = False
    pattern = r'https://www\.google\.com/maps\?q=(-?\d+\.\d+),(-?\d+\.\d+)'
    match = re.search(pattern, link)
    if match:
        latitude = float(match.group(1))
        longitude = float(match.group(2))
        halt = True
    return (latitude, longitude, halt)

def InputSport(phrase: str, sport: str) -> tuple[str, bool]:
    halt:bool = False

    if phrase in ("volleyball", "football"):
        halt = True
        sport = phrase
    return (sport, halt)

def CreateSport(S: dict[str, str], NewS: dict[str, str], phrase: str, level: int, sport: str, direction: str, language: str) -> tuple[int, str, str, object, bool]:
    text:str = ''
    kbd:object = None
    halt:bool = False

    (sport, halt) = InputSport(phrase, sport)
    if halt:
        text = S["onlysport"] % (sport) + S["writedate"]
        kbd = forall.GoToAdmin(NewS["main_menu_kb"])
        level = 3
    else:
        (level, _direction_, text, kbd, _halt_) = DirectionsOfDirection(S, direction, level, language, direction, 0)
    
    return (level, sport, text, kbd, halt)

def InputDate(phrase: str, date: int) -> tuple[int, bool]:
    halt:bool = False
    truedate:int = -1

    halt, truedate = DateCheck(phrase)
    if halt:
        date = truedate
    return (date, halt)

def CreateDate(S: dict[str, str], NewS: dict[str, str], phrase: str, level: int, sport: str, date: int):
    text:str = ''
    kbd:object = None
    halt:bool = False
    _direction_:str = ''
    _language_:str = ''

    (date, halt) = InputDate(phrase, date)
    if halt:
        level = 4
        text = S["sport+date"] % (sport, forall.CreateDateStr(date)) + S["whitetime"]
        kbd = forall.GoToAdmin(NewS["main_menu_kb"])
    else:
       (level, _sport_, text, kbd, _halt_) = CreateSport(S, NewS, sport, level, sport, _direction_, _language_)
    
    return level, date, text, kbd, halt


def InputTime(phrase: str, time: int, date: int) -> tuple[int, bool]:
    halt:bool = False
    truetime:int = -1

    halt, truetime = TimeCheck(phrase, date//10000, (date-((date//10000)*10000))//100, (date-((date//10000)*10000)-(((date-((date//10000)*10000))//100*100))//1))
    if halt:
        time = truetime
    return (time, halt)

def CreateTime(S: dict[str, str], NewS: dict[str, str], phrase: str, level: int, sport: str, date: int, time: int) -> tuple[int, int, str, object, bool]:
    text:str = ''
    kbd:object = None
    halt:bool = False

    (time, halt) = InputTime(phrase, time, date)
    if halt:
        level = 5
        text = S["sport+date+time"] % (sport, forall.CreateDateStr(date), forall.CreateTimeStr(time)) + S["writeseats"]
        kbd = forall.GoToAdmin(NewS["main_menu_kb"])
    else:
        (level, _date_, text, kbd, _halt_) = CreateDate(S, NewS, forall.CreateDateStr(date), level, sport, date)

    return (level, time, text, kbd, halt)

def InputSeatsOrPrice(phrase: str, seatsorprice: int) -> tuple[int, bool]:
    halt:bool = False

    if forall.IntCheck(phrase):
        halt = True
        seatsorprice = int(phrase)

    return (seatsorprice, halt)

def CreateSeats(S: dict[str, str], NewS: dict[str, str], phrase: str, level: int, sport: str, date: int, time: int, seats: int) -> tuple[int, int, str, object, bool]:
    text:str = ''
    kbd:object = None
    halt:bool = False

    (seats, halt) = InputSeatsOrPrice(phrase, seats)
    if halt: 
        level = 6
        text = S["sport+date+time+seats"] % (sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), seats) + S["writeprice"]
        kbd = forall.GoToAdmin(NewS["main_menu_kb"])
    else:
        (level, _time_, text, kbd, _halt_) = CreateTime(S, NewS, forall.CreateTimeStr(time), level, sport, date, time)

    return (level, seats, text, kbd, halt)

def CreatePrice(S: dict[str, str], NewS: dict[str, str], phrase: str, level: int, sport: str, date: int, time: int, seats: int, price: int) -> tuple[int, int, str, object, bool]:
    text:str = ''
    kbd:object = None 
    halt:bool = False   

    (price, halt) = InputSeatsOrPrice(phrase, price)
    if halt:
        level = 7
        text = S["sport+date+time+seats"] % (sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), seats) + S["writecurrency"]
        kbd = forall.GoToAdmin(NewS["main_menu_kb"])
    else:
        (level, _seats_, text, kbd, _halt_) = CreateSeats(S, NewS, str(seats), level, sport, date, time, seats)

    return (level, price, text, kbd, halt)

def CreateCurrecny(S: dict[str, str], NewS: dict[str, str], phrase: str, sport: str, date: int, time: int, seats: int, price: int, currency: str) -> tuple[int, str, str, object]:
    return (8, phrase, (S["sport+date+time+seats+price+currency"] % (sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), seats, price, phrase) + S["writelink"]), forall.GoToAdmin(NewS["main_menu_kb"]))

def InputLink(phrase: str, lat: float, long: float) -> tuple[float, float, bool]:
    halt:bool = False

    truelat, truelong, halt = TryToFindLocation(phrase)
    if halt:
        lat, long = truelat, truelong
    return (lat, long, halt)

def CreateLink(S: dict[str, str], NewS: dict[str, str], phrase: str, level: int, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float) -> tuple[int, float, float, str, object, bool]:
    text:str = ''
    kbd:object = ''
    halt:bool = False
    
    truelat, truelong, halt = InputLink(phrase, lat, long)
    if halt:
        lat = truelat
        long = truelong
        level = 9
        text = S["sport+date+time+seats+price+currency+link"] % (sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), seats, price, currency, lat, long) + S["writeaddress"]
        kbd = forall.GoToAdmin(NewS["main_menu_kb"])
    else:
        (level, _currency_, text, kbd) = CreateCurrecny(S, NewS, currency, sport, date, time, seats, price, currency)

    return (level, lat, long, text, kbd, halt)

def CreateAddress(S: dict[str, str], phrase: str, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float) -> tuple[int, str, str, object]:
    return (10, phrase, (S["sport+date+time+seats+price+currency+link+nameaddress"] % (sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), seats, price, currency, lat, long, phrase) + S["clarification"]), SaveorChange(S["savegame"], S["changegame"]))

def SaveOrChange(S: dict[str, str], NewS: dict[str, str], phrase: str, level: int, action: str, direction: str, aid: int, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float, address: str, language: str, change_create: bool) -> tuple[int, str, str, str, object, bool, bool, str]:
    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''

    if phrase in ("save", "change"):
        halt = True
        if phrase == "save":
            NewScheduleGame(aid)
            text = NewS["gamewassave"] + NewS["main_menu_text"]
            kbd = forall.OptionsAdmin(S["first_option"], S["second_option"], S["third_option"], S["fourth_option"], S["fifth_option"])
            action = "divarication"
            level = 3
        else:
            direction = "change games"
            level = 2
            change_create = True
            (text, kbd, prmode) = InputGameId(S, text, kbd, language, sport, date, time, seats, price, currency, lat, long, address)
    else:
        (level, _address_, text, kbd) = CreateAddress(S, address, sport, date, time, seats, price, currency, lat, long)
    
    return (level, direction, action, text, kbd, halt, change_create, prmode)

def InputGameId(S:dict[str, str], text: str, kbd: object, language: str, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float, address: str) -> tuple[str, object, str]:
    text = S["game_inf"] % (sport, forall.CreateDateStr(date), forall.CreateTimeStr(time), seats, price, currency, lat, long, address) + S["choose_change"]
    kbd = OptionsOfChange(S["sport"], S["date"], S["time"], S["seats"], S["price"], S["currency"], S["link"], S["nameaddress"], language_dictionary_for_all.String[language]["main_menu_kb"])
    prmode = "HTML"
    return text, kbd, prmode

def ChangeGameId(S: dict[str, str], phrase: str, language: str, level: int, direction:str, launch_point: int, game_id: int, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float, address: str) -> tuple[int, int, int, str, object, bool, str]:
    text:str = ''
    kbd:object = None    
    halt:bool = False
    prmode:str = ''
    
    if forall.IntCheck(phrase):
        if SelectGameId(int(phrase)):
            halt = True
            level = 3
            game_id = int(phrase)
            sport, date, time, seats, price, currency, lat, long, address = SelectDataFromSchedule(game_id)
            (text, kbd, prmode) = InputGameId(S, text, kbd, language, sport, date, time, seats, price, currency, lat, long, address)
        else:
            (level, _direction_, text, kbd, _halt_) = DirectionsOfDirection(S, direction, level, language, direction, launch_point)
    else:
        if phrase == "previous page":
            launch_point += -7
        elif phrase == "next page":
            launch_point += 7
        (level, _direction_, text, kbd, _halt_) = DirectionsOfDirection(S, direction, level, language, direction, launch_point)
    return (level, launch_point, game_id, text, kbd, halt, prmode)

def InputKindOfChanging(S: dict[str, str], phrase: str, level: int, direction_of_change: str, language: str, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float, address: str) -> tuple[int, str, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''

    if phrase in ("sport", "date", "time", "seats", "price", "currency", "link", "nameaddress"):
        halt = True
        level = 4
        if phrase == "sport":
            text = S["start_create_game"]
            kbd = KindOfSport(language_dictionary_for_all.String[language]["volleyball"], language_dictionary_for_all.String[language]["football"], language_dictionary_for_all.String[language]["main_menu_kb"])
        elif phrase == "date":
            text = S["writedate"]
        elif phrase == "time":
            text = S["whitetime"]
        elif phrase == "seats" or phrase == "price":
            if phrase == "seats":
                text = S["writeseats"]
            else:
                text = S["writeprice"]
        elif phrase == "currency":
            text = S["writecurrency"]
        elif phrase == "link":
            text = S["writelink"]
        elif phrase == "nameaddress":
            text = S["writeaddress"]
        direction_of_change = phrase
    else:
        (text, kbd, prmode) = InputGameId(S, text, kbd, language, sport, date, time, seats, price, currency, lat, long, address)
    return (level, direction_of_change, text, kbd, halt, prmode)

def PreparationData(S: dict[str, str], direction_of_change: str, phrase: str, sport: str, date: int, time: int, seats: int, price: int, lat: float, long: float) -> tuple[int, str, float, float, bool]:
    changedata_int:int = -1
    changedata_str:str = ''
    changedata_float:float = -1
    changedata_float2:float = -1
    halt:bool = False

    if direction_of_change == "sport":
        changedata_str, halt = InputSport(phrase, sport)
    elif direction_of_change == "date":
        changedata_int, halt = InputDate(phrase, date)
    elif direction_of_change == "time":
        print("WATTA FUCK", phrase)
        changedata_int, halt = InputTime(phrase, time, date)
    elif direction_of_change == "seats":
        changedata_int, halt = InputSeatsOrPrice(phrase, seats)
    elif direction_of_change == "price":
        changedata_int, halt = InputSeatsOrPrice(phrase, price)
    elif direction_of_change == "currency":
        changedata_str = phrase
        halt = True
    elif direction_of_change == "link":
        changedata_float, changedata_float2, halt = InputLink(phrase, lat, long)
    elif direction_of_change == "nameaddress":
        changedata_str = phrase
        halt = True
    return changedata_int, changedata_str, changedata_float, changedata_float2, halt

def ChangeDataInt(data: int, column: str, game_id: int):
    ChangeColumnInt(data, column, game_id)

def ChangeDataStr(data: str, column: str, game_id: int):
    ChangeColumnStr(data, column, game_id)

def ChangeData2xFloat(lat: float, long: float, game_id: int):
    ChangeColumnsFloat(lat, long, game_id)

def InputChangeData(S: dict[str, str], direction_of_change: str, phrase: str, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float, address: str, game_id: int, language: str, level: int, typeofchange: str) -> tuple[int, str, str, object, bool, str]:
    halt:bool = False
    text:str = ''
    kbd:object = None
    prmode:str = ''
    changedata_int:int = -1
    changedata_str:str = ''
    changedata_float:float = -1
    changedata_float2:float = -1

    if direction_of_change in ("sport", "date", "time", "seats", "price", "currency", "link", "address"):
        level = 5
        (changedata_int, changedata_str, changedata_float, changedata_float2, halt) = PreparationData(S, direction_of_change, phrase, sport, date, time, seats, price, lat, long)
        print("AHAHAHHAHAHAHAHHAHAHA", halt)
        if halt:
            text = S["data_changed"]
            kbd = forall.AnotherChange(S["yes"], S["no"])
            if changedata_int != -1:
                typeofchange = "int"
                ChangeDataInt(changedata_int, direction_of_change, game_id)
            elif changedata_str != '':
                typeofchange = "str"
                ChangeDataStr(changedata_str, direction_of_change, game_id)
            elif (changedata_float != -1) and (changedata_float2 != -1):
                typeofchange = "float"
                ChangeData2xFloat(changedata_float, changedata_float2, game_id)
        else:
            (level, _direction_of_change_, text, kbd, _halt_, prmode) = InputKindOfChanging(S, direction_of_change, level, direction_of_change, language, sport, date, time, seats, price, currency, lat, long, address)
    else:
        (level, _direction_of_change_, text, kbd, _halt_, prmode) = InputKindOfChanging(S, direction_of_change, level, direction_of_change, language, sport, date, time, seats, price, currency, lat, long, address)

    return level, typeofchange, text, kbd, halt, prmode

def InputRepeat(S: dict[str, str], phrase: str, game_id: int, language: str, level: int, direction: str, launch_point: int, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float, address: str, direction_of_change: str, typeofchange: str) -> tuple[int, str, object, bool, str]:
    datachange:str = ''
    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    data_changed_str:str = ''
    data_changed_int:int = -1
    lat_changed:float = -1
    long_changed:float = -1
    _launch_point_:int = -1

    if phrase == "another data change":
        halt = True
        (level, _launch_point_, _game_id_, text, kbd, _halt_, prmode) = ChangeGameId(S, str(game_id), language, level, direction, launch_point, game_id, sport, date, time, seats, price, currency, lat, long, address)
    else:
        data_changed_str, data_changed_int, lat_changed, long_changed = SelectDataChanged(game_id, direction_of_change, typeofchange)
        
        if (typeofchange == "str") and (data_changed_str != ''):
            datachange = data_changed_str
        elif (typeofchange == "int") and (data_changed_int != -1):
            if direction_of_change == "date":
                datachange = forall.CreateDateStr(data_changed_int)
            elif direction_of_change == "time":
                datachange = forall.CreateTimeStr(data_changed_int)
            else:
                datachange = str(data_changed_int)
        elif (typeofchange == "float") and (lat_changed != -1) and (long_changed != -1):
            datachange = f"https://www.google.com/maps?q={lat_changed},{long_changed}"
    
        (level, _typeofchange_, text, kbd, _halt_, prmode) = InputChangeData(S, direction_of_change, datachange, sport, date, time, seats, price, currency, lat, long, address, game_id, language, level, typeofchange)

    return (level, text, kbd, halt, prmode)

def ChangeGame(S: dict[str, str], level: int, direction_of_change: str, game_id: int, phrase: str, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float, address: str, language: str, direction: str, launch_point: int, typeofchange: str) -> tuple[int, int, int, str, str, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''

    if level == 2:
        (level, launch_point, game_id, text, kbd, halt, prmode) = ChangeGameId(S, phrase, language, level, direction, launch_point, game_id, sport, date, time, seats, price, currency, lat, long, address)
    elif level == 3:
        (level, direction_of_change, text, kbd, halt, prmode) = InputKindOfChanging(S, phrase, level, direction_of_change, language, sport, date, time, seats, price, currency, lat, long, address)
    elif level == 4:
        (level, typeofchange, text, kbd, halt, prmode) = InputChangeData(S, direction_of_change, phrase, sport, date, time, seats, price, currency, lat, long, address, game_id, language, level, typeofchange)
    elif level == 5:
        (level, text, kbd, halt, prmode) = InputRepeat(S, phrase, game_id, language, level, direction, launch_point, sport, date, time, seats, price, currency, lat, long, address, direction_of_change, typeofchange)

    return (level, launch_point, game_id, direction_of_change, typeofchange, text, kbd, halt, prmode)

def DeleteGame(S: dict[str, str], phrase: str, language: str, game_direction: str, game_launch_point: int, level: int) -> tuple[int, int, str, str, object, bool, str]:
    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    if forall.IntCheck(phrase):
        if SelectGameId(int(phrase)):
            halt = True
            GameRemove(int(phrase))
            text = S["game_removed"]
            kbd = AnotherFunc(S["change_games"], S["create_games"], language_dictionary_for_all.String[language]["main_menu_kb"])
            level = 1
        else:
            (level, _game_direction_, text, kbd, _halt_) = DirectionsOfDirection(S, game_direction, level, language, game_direction, game_launch_point)
    else:
        if phrase == "previous page":
            game_launch_point += -7
        elif phrase == "next page":
            game_launch_point += 7
        (level, _game_direction_, text, kbd, _halt_) = DirectionsOfDirection(S, game_direction, level, language, game_direction, game_launch_point)

    return (level, game_launch_point, game_direction, text, kbd, halt, prmode)

def CreateGame(S: dict[str, str], phrase: str, level: int, direction: str, action: str, aid: int, sport: str, date: int, time: int, seats: int, price: int, currency: str, lat: float, long: float, address: str, language: str, change_create: bool) -> tuple[int, str, str, str, object, bool, str, str, int, int, int, int, str, float, float, str, bool]:
    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = "HTML"
    forallS = language_dictionary_for_all.String[language]
    
    if level == 2:
        (level, sport, text, kbd, halt) = CreateSport(S, forallS, phrase, level, sport, direction, language)
    elif level == 3:
        (level, date, text, kbd, halt) = CreateDate(S, forallS, phrase, level, sport, date)
    elif level == 4:
        (level, time, text, kbd, halt) = CreateTime(S, forallS, phrase, level, sport, date, time)
    elif level == 5:
        (level, seats, text, kbd, halt) = CreateSeats(S, forallS, phrase, level, sport, date, time, seats)
    elif level == 6:
        (level, price, text, kbd, halt) = CreatePrice(S, forallS, phrase, level, sport, date, time, seats, price)
    elif level == 7:
        (level, currency, text, kbd) = CreateCurrecny(S, forallS, phrase, sport, date, time, seats, price, currency)
    elif level == 8:
        (level, lat, long, text, kbd, halt) = CreateLink(S, forallS, phrase, level, sport, date, time, seats, price, currency, lat, long)
    elif level == 9:
        level, address, text, kbd = CreateAddress(S, phrase, sport, date, time, seats, price, currency, lat, long)
    elif level == 10:
        (level, direction, action, text, kbd, halt, change_create, prmode) = SaveOrChange(S, forallS, phrase, level, action, direction, aid, sport, date, time, seats, price, currency, lat, long, address, language, change_create)

    return (level, direction, action, text, kbd, halt, prmode, sport, date, time, seats, price, currency, lat, long, address, change_create)


def ChooseDiraction(S: dict[str, str]) -> tuple[int, str, object]:
    return (1, S["games_directions"], GamesOptions(S["change_games"], S["create_games"], S["delete_games"]))

def DirectionsOfDirection(S: dict[str, str], phrase: str, level: int, language: str, direction: str, launch_point: int) -> tuple[int, str, str, object, bool]:
    schedule_output:list[tuple[str, str, str, str]] = []
    text:str = ''
    kbd:object = None
    halt:bool = False
    if phrase in ("change games", "delete games", "create games", "previous page", "next page"):
        halt = True
        level = 2
        direction = phrase
        if phrase in ("change games", "delete games", "previous page", "next page"):
            schedule_input:list[tuple[int, str, int, int]] = ScheduleOfGames(launch_point, 7)
            length:int = LengthOfGames()
            _schedule_, schedule_output = forall.SheduleStr([], schedule_input, language)

            text = S["choose_game"]
            kbd = forall.Schedule(schedule_output, 7, launch_point, '', length)
        else:
            text = S["start_create_game"]
            kbd = KindOfSport(language_dictionary_for_all.String[language]["volleyball"], language_dictionary_for_all.String[language]["football"], language_dictionary_for_all.String[language]["main_menu_kb"])
    else:
        level, text, kbd = ChooseDiraction(S)

    return level, direction, text, kbd, halt