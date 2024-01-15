from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def ActivitiesDirection(first: str, sec: str, main: str) -> InlineKeyboardMarkup:

    directions = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{first}", callback_data="create game")],
        [InlineKeyboardButton(text=f"{sec}", callback_data="active games")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])

    return directions

def DirectionsForChatGame(show_chats: str, new_chat: str, main: str) -> InlineKeyboardMarkup:

    dirforchatgame = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{show_chats}", callback_data="show chats")],
        [InlineKeyboardButton(text=f"{new_chat}", callback_data="add new chat")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    
    return dirforchatgame

def SendOrNo(yes: str, main: str) -> InlineKeyboardMarkup:

    sendorno = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{yes}", callback_data="send chat game")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    
    return sendorno

def LetsGO(part: str, game_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=f"{part}", callback_data=f"{game_id}")]])

def RemoveFromGameOrCall(remove: str, call: str, main: str, status: bool, nickname: str) -> InlineKeyboardMarkup:

    if status:
        removeorcall = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{remove}", callback_data="remove from game")],
        [InlineKeyboardButton(text=f"{call}", url = f"t.me/{nickname}")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])

    else:
        removeorcall = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{remove}", callback_data="remove from game")],
        [InlineKeyboardButton(text=f"{main}", callback_data="Main_Menu")]])
    
    return removeorcall
    