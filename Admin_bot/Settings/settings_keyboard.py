from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def DirectionOfSettings(changelang: str, main: str) -> InlineKeyboardMarkup:

    direction = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{changelang}", callback_data="change language")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    return direction

def Language(rus: str, engl: str, tur: str, main: str) -> InlineKeyboardMarkup:

    languages = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{rus}", callback_data="ru")],
        [InlineKeyboardButton(text=f"{engl}", callback_data="en")],
        [InlineKeyboardButton(text=f"{tur}", callback_data="tur")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    return languages