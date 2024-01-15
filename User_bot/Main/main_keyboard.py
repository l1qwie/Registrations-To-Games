from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def Notif(cont: str, main: str) -> object:
    notif = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{cont}", callback_data="continue")],
    [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])
    return notif

def WhatHappend(what_hap: str) -> object:
    what_happend = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{what_hap}", callback_data="what happend")]])
    return what_happend

def GoTo(main: str) -> object:
    go_to = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="В главное меню", callback_data="MainMenu")]])
    return go_to
