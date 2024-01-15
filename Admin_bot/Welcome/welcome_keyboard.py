from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def ComStartReg(hello: str) -> InlineKeyboardMarkup:
    first_kb:object = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{hello}", callback_data="start reg")]])

    return first_kb
