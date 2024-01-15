from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def GoTo(main:str) -> object:

    goto = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])
    return goto
