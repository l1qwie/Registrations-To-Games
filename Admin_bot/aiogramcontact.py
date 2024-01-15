from aiogram import Bot, Dispatcher, Router, types
import asyncio
from aiogram.exceptions import TelegramBadRequest
from secretdata import TOKEN #, host, user, password, db_name

from Main.main_action import UpdateExMessageFromChat, UpdateExMessageId, EvPrevMsgId, DispatchPhrase, DispatchGroups
from language_dictionary_for_all import String

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

async def SendMessage(id: int, text: str, chattext: str, kbd: types.InlineKeyboardMarkup, chatkbd: types.InlineKeyboardMarkup, prmode: str, halt: bool, spreadsheet: str, fixed: bool, findchats: bool, chatid: int):

    reply: types.Message | None = None
    if not fixed:
        if not findchats:
            if chatid == -1:
                reply = await bot.send_message(chat_id=id, text=text, parse_mode=prmode, reply_markup=kbd)
            else:
                reply = await bot.send_message(chat_id=id, text=text, parse_mode=prmode, reply_markup=kbd)
                chatreply = await bot.send_message(chat_id=chatid, text=chattext, parse_mode="HTML", reply_markup=chatkbd)
                UpdateExMessageFromChat(chatreply.message_id, chatid)
        else:
            pass
    else:
        reply = await bot.send_message(chat_id=id, text=text, reply_markup=kbd, parse_mode=prmode)
        await bot.pin_chat_message(chat_id=id, message_id=reply.message_id)
    if reply and not fixed:
        UpdateExMessageId(reply.message_id, id)
    else:
        UpdateExMessageId(-1, id)



def UpdateInfoAboutClient(aid: int, name: str, last_name: str, username: str, language: str, bot_text: str) -> int:
    prev:int = -1
    if bot_text != String[language]["ups_no_profile"]:
        prev = EvPrevMsgId(aid, name, last_name, username, language)
    return prev

#@router.errors()
#async def e():
#    print('Router oops')

@router.message()
async def InputMessage(message: types.Message):
    text:str = ''
    exmess:int = -1
    chattext:str = ''
    kbd:object = None
    chatkbd:object = None
    prmode:str = ''
    halt:bool = False
    spreadsheet:str = ''
    fixed:bool = False
    findchats:bool = False
    chatid:int = -1
    last_name:str = ''
    if message.chat.type == "private":
        if message.from_user and message.text and not message.from_user.is_bot:
            if message.from_user.username and message.from_user.language_code:
                if message.from_user.last_name:
                    last_name = message.from_user.last_name
                else:
                    last_name = ''
                (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(message.from_user.id, message.text, message.from_user.language_code)
                exmess = UpdateInfoAboutClient(message.from_user.id, message.from_user.first_name, last_name, message.from_user.username, message.from_user.language_code, text)
                if exmess != -1:
                    try:
                        await bot.delete_message(chat_id=message.from_user.id, message_id=exmess)
                    except TelegramBadRequest:
                        print("bot couldn't delete the message")
                #assert(isinstance(kbd, types.InlineKeyboardMarkup))
                #assert(isinstance(chatkbd, types.InlineKeyboardMarkup))
                await SendMessage(message.from_user.id, text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid)
        else:
            print("Admin doesn't have 'from_user' aiogram class")
    elif message.chat.type in ("group", "supergroup"):
        print("FROM USERS:", message.from_user, "TITLE OF CHAT:", message.chat.title, "CHAT ID", message.chat.id)
        if message.from_user and message.text and message.chat.title:
            (chattext, chatkbd, exmess, prmode) = DispatchGroups(message.chat.id, message.from_user.id, message.text, message.chat.title)
            if exmess != -1:
                try:
                    assert(isinstance(chatkbd, types.InlineKeyboardMarkup))
                    await bot.edit_message_text(text=chattext, chat_id=message.chat.id, message_id=exmess, parse_mode=prmode, reply_markup=chatkbd)
                except TelegramBadRequest:
                    print("bot couldn't edit the message")
    else:
        assert(False)

@router.callback_query()
async def InputCallBack(query: types.CallbackQuery):
    text:str = ''
    exmess:int = -1
    chattext:str = ''
    kbd:object = None
    chatkbd:object = None
    prmode:str = ''
    halt:bool = False
    spreadsheet:str = ''
    fixed:bool = False
    findchats:bool = False
    chatid:int = -1
    last_name:str = ''
    if query.message.chat.type == "private":
        if query.from_user and query.data and query.from_user.username and query.from_user.language_code:
            (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(query.from_user.id, query.data, query.from_user.language_code)
            exmess = UpdateInfoAboutClient(query.from_user.id, query.from_user.first_name, last_name, query.from_user.username, query.from_user.language_code, text)
            if exmess != -1:
                try:
                    await bot.delete_message(chat_id=query.from_user.id, message_id=exmess)
                except TelegramBadRequest:
                    print("Message id not found in private chat")
            await SendMessage(query.from_user.id, text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid)
        else:
            assert(False)
    elif query.message.chat.type in ("group", "supergroup"):
        if query.from_user and query.data and query.message.chat.title:
            (chattext, chatkbd, exmess, prmode) = DispatchGroups(query.message.chat.id, query.from_user.id, query.data, query.message.chat.title)
            if exmess != -1:
                try:
                    await bot.edit_message_text(text=chattext, chat_id=query.message.chat.id, message_id=exmess, parse_mode=prmode, reply_markup=chatkbd)
                except TelegramBadRequest:
                    print("Message id not found in group")
        else:
            assert(False)



































"""
@router.message()
async def VecMess(message: types.Message):
    database.ConnectTo(host, user, password, db_name)
    admin.namer = Namer
    if message.content_type == types.ContentType.TEXT:
        print(message.from_user.id, message.text)
        (text, kbd, prmode, halt, spreadsheet, fixed) = DispatchPhrase(message.from_user.id, message.text)
        if text != "Упс! Кажется, у вас отсутствует профиль для этого бота! для того чтобы начать пользоваться мной вам следует перейти к этому боту и создать спецальный профиль. t.me/RegistrationToGames_bot":
            prev = EvPrevMsgId(message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username)    # Evaluate Previous Message ID
            if prev != None:
                await bot.delete_message(chat_id=message.from_user.id, message_id=prev)
        if spreadsheet is None:
            if fixed is None:
                reply = await bot.send_message(message.from_user.id, text=text, reply_markup=kbd, parse_mode=prmode)
            else:
                reply = await bot.send_message(message.from_user.id, text=text, reply_markup=kbd, parse_mode=prmode)
                await bot.pin_chat_message(message.from_user.id, message_id=reply.message_id)
        else:
            if text is None:
                reply = await bot.send_document(message.from_user.id, BufferedInputFile(spreadsheet.encode(), 'Chart.html'), reply_markup=kbd)
            else:
                print(prmode)
                reply = await bot.send_document(message.from_user.id, BufferedInputFile(spreadsheet.encode(), 'Chart.html'), caption=text, reply_markup=kbd)
    else:
        reply = await bot.send_message(message.from_user.id, text="К сожалению, пока что я принимаю только текстовые сообщения", parse_mode=prmode)
    RetainPrevMsgId(message.from_user.id, reply.message_id)    

@router.callback_query()
async def VecCallBack(query: types.CallbackQuery):
    database.ConnectTo(host, user, password, db_name)
    admin.namer = Namer
    (text, kbd, prmode, halt, spreadsheet, fixed) = DispatchPhrase(query.from_user.id, query.data)
    prev = EvPrevMsgId(query.from_user.id, query.from_user.first_name, query.from_user.last_name, query.from_user.username)    # Evaluate Previous Message ID
    if prev != None:
        await bot.delete_message(chat_id=query.from_user.id, message_id=prev)
    if spreadsheet is None:
        if fixed is None:
            reply = await bot.send_message(query.from_user.id, text=text, reply_markup=kbd, parse_mode=prmode)
        else:
            await bot.pin_chat_message(query.from_user.id, message_id=reply.message_id, parse_mode=prmode)
    else:
        if text is None:
            reply = await bot.send_document(query.from_user.id, BufferedInputFile(spreadsheet.encode(), 'Chart.html'), reply_markup=kbd, parse_mode=prmode)
        else:
            print(prmode)
            reply = await bot.send_document(query.from_user.id, BufferedInputFile(spreadsheet.encode(), 'Chart.html'), caption=text, reply_markup=kbd, parse_mode=prmode)
    RetainPrevMsgId(query.from_user.id, reply.message_id)

async def CheskWhoSleep():
    database.ConnectTo(host, user, password, db_name)
    while True:
        await asyncio.sleep(5)  # Ждать 10 минут
        text_list, keyboards, user_ids, exmessids  = admin.BotCheskWhoSleep()
        if text_list != [] and keyboards != [] and user_ids != []:
            for id, text, exid, kbd in zip(user_ids, text_list, exmessids, keyboards):
                if exid != None:
                    await bot.delete_message(id, message_id=exid)
                reply = await bot.send_message(chat_id=id, text=text, reply_markup=kbd)
                admin.RetainPrevMsgId(id, reply.message_id)
        else:
            print("Спящих не обнаруженно!ZzZzZzZzZzZ")

async def FindGameIsOver():
    database.ConnectTo(host, user, password, db_name)
    while True:
        await asyncio.sleep(600)  # Ждать 10 минут
        admin.GameOver()
    print("haha")

async def PongonPodDelGame():
    database.ConnectTo(host, user, password, db_name)
    database.PongonPodDelGame()
"""

async def main():
    print("Запустился")
    #asyncio.create_task(PongonPodDelGame())
    #asyncio.create_task(CheskWhoSleep())
    #asyncio.create_task(FindGameIsOver())
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    print("...")
    asyncio.run(main())