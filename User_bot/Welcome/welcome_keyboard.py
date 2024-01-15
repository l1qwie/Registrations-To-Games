from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def Registration(phrase: str) -> object:
    reg = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"{phrase}", callback_data="GoReg")]])
    
    return reg

def Further(all_right: str) -> object:
    futher = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"{all_right}", callback_data="GoNext")]])

    return futher

def Error() -> InlineKeyboardMarkup:
    error = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="GLOBAL BOT", url="https://t.me/RegistrationToGames_bot")]])
    return error