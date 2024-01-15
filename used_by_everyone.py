from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re
from language_dictionary_for_all import String 

def CreateDateStr(day_int: int) -> str:
    year = day_int//10000
    month = (day_int-(year*10000))//100
    day = (day_int-(year*10000)-(month*100))//1
    date_str = f"{day}-{month}-{year}"
    return date_str

def CreateTimeStr(time_int: int) -> str:
    hour = time_int//100
    minute = (time_int-(hour*100))
    time_str = f"{hour}:{minute}"
    return time_str

def IntCheck(mes: str) -> bool:
    result:bool = False
    if re.fullmatch(r'-?\d{1,15}', mes):
        result = True
    print('result =', result)
    return result

def Buttons(keyboard: list[list[InlineKeyboardButton]], length: int, limit: int, launch_point: int) -> list[list[InlineKeyboardButton]]:
    print("DATA FROM def Buttons =", length, limit, launch_point)

    if length > limit and launch_point == 0 and length != 0: 
        keyboard.append([InlineKeyboardButton(text=f">>", callback_data=f"next page")])
    elif length > limit and length <= (limit + launch_point) and length != 0:
        keyboard.append( [InlineKeyboardButton(text=f"<<", callback_data=f"previous page")])
    elif length > limit and length > (limit + launch_point) and length != 0:
        keyboard.append([InlineKeyboardButton(text="<<", callback_data="previous page"), InlineKeyboardButton(text=">>", callback_data="next page")])
    
    return keyboard

def Options(first_option: str, second_option: str, third_option: str, fourth_option: str) -> object:
    options:object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{first_option}", callback_data="Looking Schedule")],
    [InlineKeyboardButton(text=f"{second_option}", callback_data="Reg to games")],
    [InlineKeyboardButton(text=f"{third_option}", callback_data="Photo&Video")],
    [InlineKeyboardButton(text=f"{fourth_option}", callback_data="My records")]])
    
    return options

def Schedule(sched: list[tuple[str,...]], limit: int, launch_point: int, disc_seats: str, length: int) -> InlineKeyboardMarkup:
    keyboard:list[list[InlineKeyboardButton]] = []
    game_id:str = ''
    sport:str = ''
    date:str = ''
    time:str = ''
    seats:str = ''

    if disc_seats != '':
        for game_id, sport, date, time, seats in sched:
            keyboard.append([InlineKeyboardButton(text=f"{sport}  {date}  {time}  {disc_seats}{seats}", callback_data=f"{game_id}")])
    else:
        for game_id, sport, date, time in sched:
            keyboard.append([InlineKeyboardButton(text=f"{sport}  {date}  {time}", callback_data=f"{game_id}")])
    keyboard = Buttons(keyboard, length, limit, launch_point)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


def FrequentChoice(alone: str, two: str, three: str) -> object:
    frequent_choice:object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{alone}", callback_data="1")],
    [InlineKeyboardButton(text=f"{two}", callback_data="2")],
    [InlineKeyboardButton(text=f"{three}", callback_data="3")]])

    return frequent_choice

def KbPay(online: str, cash: str, main: str) -> object:
    pay:object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{online}", callback_data="card")],
    [InlineKeyboardButton(text=f"{cash}", callback_data="cash")],
    [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])

    return pay

def Papara(pay: str, next: str) -> object:
    papara:object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{pay}", url="https://www.papara.com/personal/qr?karekod=7502100102120204082903122989563302730612230919141815530394954120000000000006114081020219164116304DDE3", callback_data="payment completed")],
    [InlineKeyboardButton(text=f"{next}", callback_data="Next")]])

    return papara

def GoToAdmin(main_menu: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"{main_menu}", callback_data="Main_Menu")]])

def OptionsAdmin(first: str, sec: str, third: str, fourth: str, fifth: str) -> InlineKeyboardMarkup:

    menu:object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{first}", callback_data="Games")],
    [InlineKeyboardButton(text=f"{sec}", callback_data="Clients")],
    [InlineKeyboardButton(text=f"{third}", callback_data="Activity")],
    [InlineKeyboardButton(text=f"{fourth}", callback_data="Finances")],
    [InlineKeyboardButton(text=f"{fifth}", callback_data="Settings")]])
    
    return menu


def SheduleStr(schedule_input_ws:list[tuple[int, str, int, int, int]], schedule_input:list[tuple[int, str, int, int]], lang: str) -> tuple[list[tuple[str, str, str, str, str]], list[tuple[str, str, str, str]]]:
    game_id:int = -1
    sport:str = ''
    date:int = -1
    date_str:str = ''
    time:int = -1
    time_str = -1
    schedule_output_ws:list[tuple[str, str, str, str, str]] = []
    schedule_output:list[tuple[str, str, str, str]] = []

    if schedule_input_ws != []:
        for game_id, sport, date, time, seats in schedule_input_ws:
            sport = String[lang][sport]
            date_str = CreateDateStr(date)
            time_str = CreateTimeStr(time)
            schedule_output_ws.append((str(game_id), sport, date_str, time_str, str(seats)))
    elif schedule_input != []:
        for game_id, sport, date, time in schedule_input:
            sport = String[lang][sport]
            date_str = CreateDateStr(date)
            time_str = CreateTimeStr(time)
            schedule_output.append((str(game_id), sport, date_str, time_str))

    return schedule_output_ws, schedule_output


def KeyboardWithClientsNames(names: list[tuple[int, str, str]], limit: int, launch_point: int, length: int, language: str) -> InlineKeyboardMarkup:
    user_id:int = -1
    name:str = ''
    last_name:str = ''
    keyboard:list[list[InlineKeyboardButton]] = []

    for user_id, name, last_name in names:
        if name == "no_data":
            name = String[language][name]
        if last_name == "no_data":
            last_name = String[language][last_name]
        keyboard.append([InlineKeyboardButton(text=f"{name}  {last_name} ", callback_data=f"{user_id}")])

    keyboard = Buttons(keyboard, length, limit, launch_point)
        
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def AnotherChange(yes: str, no: str) -> InlineKeyboardMarkup:

    anotherchange = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{yes}", callback_data="another data change")],
        [InlineKeyboardButton(text=f"{no}", callback_data="Main_Menu")]])

    return anotherchange


def Chats(chatinf: list[tuple[int, str]], limit: int, launch_point: int, length: int) -> InlineKeyboardMarkup:
    chatid:int = -1
    chattitle:str = ''
    keyboard:list[list[InlineKeyboardButton]] = []

    for chatid, chattitle in chatinf:
        keyboard.append([InlineKeyboardButton(text=f"{chattitle}", callback_data=f"{chatid}")])

    keyboard = Buttons(keyboard, length, limit, launch_point)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)