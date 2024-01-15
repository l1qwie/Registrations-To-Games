from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def schedule(schedule: list) -> list:
    keyboard = []
    for game_id, sport, date, time, seats in schedule:
        button = InlineKeyboardButton(text=f"{sport}  {date}  {time}  мест осталось:{seats}", callback_data=f"{game_id}")
        keyboard.append([button])
    schedulekb = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return schedulekb

def schedule_with_button_next(schedule: list):
    keyboard = []
    for game_id, sport, date, time, seats in schedule:
        button = InlineKeyboardButton(text=f"{sport}  {date}  {time}  мест осталось:{seats}", callback_data=f"{game_id}")
        keyboard.append([button])
    keyboard.append([InlineKeyboardButton(text=f">>>>>", callback_data=f"next page")])
    schedulekb = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return schedulekb
    
def schedule_with_button_back(schedule: list):
    keyboard = []
    for game_id, sport, date, time, seats in schedule:
        button = InlineKeyboardButton(text=f"{sport}  {date}  {time}  мест осталось:{seats}", callback_data=f"{game_id}")
        keyboard.append([button])
    keyboard.append([InlineKeyboardButton(text=f"<<<<<", callback_data=f"previous page")])
    schedulekb = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return schedulekb

def schedule_with_button_next_and_back(schedule: list):
    keyboard = []
    for game_id, sport, date, time, seats in schedule:
        button = InlineKeyboardButton(text=f"{sport}  {date}  {time}  мест осталось:{seats}", callback_data=f"{game_id}")
        keyboard.append([button])
    keyboard.append([InlineKeyboardButton(text=f"<<<<<", callback_data=f"previous page")], [InlineKeyboardButton(text=f">>>>>", callback_data=f"next page")])
    schedulekb = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return schedulekb


