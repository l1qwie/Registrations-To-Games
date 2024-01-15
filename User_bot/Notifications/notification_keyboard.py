from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def AgreeOrDesagree(agree:str, desagree:str) -> object:
    agreeOrdesagree = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{agree}", callback_data="leave a note")],
    [InlineKeyboardButton(text=f"{desagree}", callback_data="Del my record")]])

    return agreeOrdesagree