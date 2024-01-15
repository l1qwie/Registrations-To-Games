from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def ChangeOrDel(setone: str, settwo: str, main: str) -> object:
    change_or_del =  InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{setone}", callback_data="change language")],
    [InlineKeyboardButton(text=f"{settwo}", callback_data="seting regs")],
    [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])

    return change_or_del

def ChangeLang(setlang: str, main: str) -> object:
    change_lang =  InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{setlang}", callback_data="change language")],
    [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])

    return change_lang

def Languages(first_lang: str, sec_lang: str, third_lang: str, main: str) -> object:
    languages =  InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=f"{first_lang}", callback_data="en")],
    [InlineKeyboardButton(text=f"{sec_lang}", callback_data="ru")],
    [InlineKeyboardButton(text=f"{third_lang}", callback_data="tur")],
    [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])

    return languages

def OptionGameUser(first: str, sec: str, third: str, main: str, counter: int) -> object: 
    if counter > 1:
        opt = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{first}", callback_data="delete my game")],
        [InlineKeyboardButton(text=f"{sec}", callback_data="change my game")],
        [InlineKeyboardButton(text=f"{third}", callback_data="see more games")],
        [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])
    else:
        opt = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{first}", callback_data="delete my game")],
        [InlineKeyboardButton(text=f"{sec}", callback_data="change my game")],
        [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])

    return opt

def WhatChange(seats: str, payment: str, main: str, status: bool) -> object:
    if status:
        options = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{seats}", callback_data="change seats")],
        [InlineKeyboardButton(text=f"{payment}", callback_data="change payment")],
        [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])
    else:
        options = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{seats}", callback_data="change seats")],
        [InlineKeyboardButton(text=f"{main}", callback_data="MainMenu")]])
    return options