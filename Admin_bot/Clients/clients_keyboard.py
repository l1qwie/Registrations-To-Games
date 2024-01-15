from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ClientsDirections(first: str, sec: str, th: str, four: str, main: str) -> InlineKeyboardMarkup:

    directions = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{first}", callback_data="create client")],
        [InlineKeyboardButton(text=f"{sec}", callback_data="change client")],
        [InlineKeyboardButton(text=f"{th}", callback_data="delete client")],
        [InlineKeyboardButton(text=f"{four}", callback_data="reg client to game")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])

    return directions

def FromWhere(teldir: str, main: str) -> InlineKeyboardMarkup:

    from_where = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"Telegram", callback_data="tg")],
        [InlineKeyboardButton(text=f"WhatsApp", callback_data="wapp")],
        [InlineKeyboardButton(text=f"Viber", callback_data="vb")],
        [InlineKeyboardButton(text=f"{teldir}", callback_data="calling")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    
    return from_where

def SaveOrChange(save: str, change: str, main: str) -> InlineKeyboardMarkup:

    saveorchange = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{save}", callback_data="save")],
        [InlineKeyboardButton(text=f"{change}", callback_data="change")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    
    return saveorchange

def OptionChange(fw: str, name: str, lname: str, phonenum: str, main: str) -> InlineKeyboardMarkup:

    optchange = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{fw}", callback_data="from_where")],
        [InlineKeyboardButton(text=f"{name}", callback_data="name")],
        [InlineKeyboardButton(text=f"{lname}", callback_data="last_name")],
        [InlineKeyboardButton(text=f"{phonenum}", callback_data="phone_number")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    
    return optchange