from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def GamesOptions(change_games: str, create_games: str, delete_games: str) -> InlineKeyboardMarkup:

    options:object = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{change_games}", callback_data="change games")],
        [InlineKeyboardButton(text=f"{create_games}", callback_data="create games")],
        [InlineKeyboardButton(text=f"{delete_games}", callback_data="delete games")]])

    return options

def SaveorChange(save: str, change: str) -> InlineKeyboardMarkup:

    save_or_change = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{save}", callback_data="save")],
        [InlineKeyboardButton(text=f"{change}", callback_data="change")]])

    return save_or_change

def KindOfSport(vol: str, foot: str, main: str) -> InlineKeyboardMarkup:

    kindofsport = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{vol}", callback_data="volleyball")],
        [InlineKeyboardButton(text=f"{foot}", callback_data="football")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    
    return kindofsport

def OptionsOfChange(sport: str, date: str, time: str, seats: str, price: str, currency: str, link: str, address: str, main: str) -> InlineKeyboardMarkup:

    options = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{sport}", callback_data="sport")],
        [InlineKeyboardButton(text=f"{date}", callback_data="date")],
        [InlineKeyboardButton(text=f"{time}", callback_data="time")],
        [InlineKeyboardButton(text=f"{seats}", callback_data="seats")],
        [InlineKeyboardButton(text=f"{price}", callback_data="price")],
        [InlineKeyboardButton(text=f"{currency}", callback_data="currency")],
        [InlineKeyboardButton(text=f"{link}", callback_data="link")],
        [InlineKeyboardButton(text=f"{address}", callback_data="address")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    
    return options

def More(m: str, main: str) -> InlineKeyboardMarkup:

    more = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{m}", callback_data="more change")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    
    return more


def AnotherFunc(func1: str, func2: str, main: str) -> InlineKeyboardMarkup:

    anotherfunc = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{func1}", callback_data="change games")],
        [InlineKeyboardButton(text=f"{func2}", callback_data="create games")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])

    return anotherfunc