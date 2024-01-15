from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



def DirectionBouth(first: str, last: str, main: str):
    direction = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{first}", callback_data="loading")],
    [InlineKeyboardButton(text=f"{last}", callback_data="viewing")],
    [InlineKeyboardButton(text=f"{main}", callback_data="Main_menu")]])

    return direction

def DirectionOnce(load: str, main: str):
    direction = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{load}", callback_data="loading")],
    [InlineKeyboardButton(text=f"{main}", callback_data="Main_menu")]])
    
    return direction

def OneTimeInterval(first: str):
    onetimeinterval = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"{first}", callback_data="all_games")]])
    return onetimeinterval

def TimeInterval(first: str, last: str):
    time_interval = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{first}", callback_data="last_games")],
    [InlineKeyboardButton(text=f"{last}", callback_data="all_games")]])

    return time_interval

def GoTo(main: str):
    go_to = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])
    
    return go_to


def TryAgain(first: str, last: str):
    try_again = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{first}", callback_data="try again")],
    [InlineKeyboardButton(text=f"{last}", callback_data="MainMenu")]])

    return try_again

def EndMediaGroup(correct: str):
    end = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{correct}", callback_data="END")]])
    return end
