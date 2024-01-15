from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def DirectionsOfMoney(stat: str, paid_act: str, main: str) -> InlineKeyboardMarkup:

    directions:object = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{stat}", callback_data="see stat")],
        [InlineKeyboardButton(text=f"{paid_act}", callback_data="paid action")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])

    return directions

def OnlyTwoWays(debtor: str, paided: str, main: str) -> InlineKeyboardMarkup:
    
    twoways:object = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{debtor}", callback_data="see debtors")],
        [InlineKeyboardButton(text=f"{paided}", callback_data="paided")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])

    return twoways

def CallOrConfirm(call: str, paided: str, main: str, nickname: str) -> InlineKeyboardMarkup:

    if nickname !="no_data":
        callorconfirm = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f"{call}", url=f"t.me/{nickname}")],
            [InlineKeyboardButton(text=f"{paided}", callback_data="paided")],
            [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    else:
        callorconfirm = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=f"{paided}", callback_data="paided")],
            [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
        
    return callorconfirm