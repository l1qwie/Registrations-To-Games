from aiogram import Bot, Dispatcher, Router, types
import asyncio
from User_bot.language_dictionary import Strings
from aiogram.exceptions import TelegramBadRequest
from aiogram.types.input_media_photo import InputMediaPhoto as AiPhoto
from aiogram.types.input_media_video import InputMediaVideo as AiVideo
from aiogram.types.input_media_audio import InputMediaAudio as AiAudio
from aiogram.types.input_media_document import InputMediaDocument as AiDocument
from User_bot.Main.main_action import DispatchPhrase, DispatchMedia, DispatchMisstakes, EvPrevMsgId, RetainPrevMsgId, BotCheskWhoSleep, WhoNeedNotification
from User_bot.secretdata import TOKEN
import typing


bot:object = Bot(token=TOKEN)
dp:object = Dispatcher()
router:object = Router()


queue:list[types.Message] = []
processor = None
monitor:bool = False

def CreateMyMediaGroup(typeoffile: list[str], file_ids: list[str]) -> list[AiAudio | AiDocument | AiPhoto | AiVideo]:
    media_group:list[AiAudio | AiDocument | AiPhoto | AiVideo] = []
    for type, fileid in zip(typeoffile, file_ids):
        if type == "photo":
            media_group.append(types.input_media_photo.InputMediaPhoto(type=type, media=fileid))
        elif type == "video":
            media_group.append(types.input_media_video.InputMediaVideo(type=type, media=fileid))
    return media_group

async def SendMediaGroup(file_ids:list[str], typeoffiles:list[str], from_user: types.User, text: str, prmode: str | None, kbd: types.InlineKeyboardMarkup) -> types.Message | None:

    reply: types.Message | None = None
    media_group:list[AiAudio | AiDocument | AiPhoto | AiVideo]

    if len(file_ids) < 10 and len(file_ids) > 1:
        media_group = CreateMyMediaGroup(typeoffiles, file_ids)
        await bot.send_media_group(from_user.id, media=media_group)
    elif len(file_ids) == 1:
        if typeoffiles[0] == "photo":
            reply = await bot.send_photo(from_user.id, photo=file_ids[0], caption=text, parse_mode=prmode, reply_markup=kbd)
        else:
            reply = await bot.send_video(from_user.id, video=file_ids[0], caption=text, parse_mode=prmode, reply_markup=kbd)
    else:
        lessthan10id:list[str] = file_ids[:10]
        lessthan10typesnames:list[str] = typeoffiles[:10]
        morethan10id:list[str] = file_ids[10:]
        morethan10typesnames:list[str] = typeoffiles[10:]
        if len(morethan10id) == 1:
            media_group = []
            if morethan10id[0] == "photo":
                await bot.send_photo(from_user.id, photo=morethan10id[0], caption=text, parse_mode=prmode, reply_markup=kbd)
            else:
                await bot.send_video(from_user.id, video=morethan10id[0], caption=text, parse_mode=prmode, reply_markup=kbd)
            media_group = CreateMyMediaGroup(lessthan10typesnames, lessthan10id)
            await bot.send_media_group(from_user.id, media=media_group)
            reply = await bot.send_message(from_user.id, text=text, parse_mode=prmode, reply_markup=kbd)
        else:
            i:int = 0
            while i < 2:
                if i == 0:
                    media_group = CreateMyMediaGroup(lessthan10typesnames, lessthan10id)
                    await bot.send_media_group(from_user.id, media=media_group)
                else:
                    media_group = CreateMyMediaGroup(morethan10typesnames, morethan10id)
                    await bot.send_media_group(from_user.id, media=media_group)
                i += 1
            reply = await bot.send_message(from_user.id, text=text, parse_mode=prmode, reply_markup=kbd)

    return reply

def InputSelection(content_type: str, from_user: types.User, file_id: list[str], media_group_id: str | None, mes_text: str | None) -> tuple[str, types.InlineKeyboardMarkup, bool, str, list[float], str, list[str], list[str], bool, bool]:

    text:str = ''
    kbd:object = None
    halt:bool = False
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    file_ids:list[str] = []
    edit:bool = False
    typecorrect:bool = False
    typeoffiles: list[str] = []
    mgid:str = '-1'

    if from_user:
        if from_user.language_code:
            if content_type in (types.ContentType.PHOTO, types.ContentType.VIDEO, types.ContentType.TEXT):
                typecorrect = True
                if content_type == types.ContentType.PHOTO or content_type == types.ContentType.VIDEO:
                    if file_id:
                        if media_group_id:
                            mgid = media_group_id
                        if content_type == types.ContentType.PHOTO:
                            (text, kbd, halt, prmode, address, img, file_ids, edit) = DispatchMedia(from_user.id, file_id[0], mgid, content_type, from_user.language_code)
                        else:
                            (text, kbd, halt, prmode, address, img, file_ids, edit) = DispatchMedia(from_user.id, file_id[1], mgid, content_type, from_user.language_code)
                elif content_type == types.ContentType.TEXT:
                    if mes_text:
                        (text, kbd, halt, prmode, address, img, file_ids, typeoffiles, edit) = DispatchPhrase(from_user.id, mes_text, from_user.language_code)
            else:
                (text, kbd) = DispatchMisstakes(from_user.language_code, 'content_type')
        else:
            (text, kbd) = DispatchMisstakes(from_user.language_code, 'language')
    else:
        print("User doesn't have 'from_user' class")
        assert(False)
    #assert(isinstance(kbd, types.InlineKeyboardMarkup))
    return text, kbd, halt, prmode, address, img, file_ids, typeoffiles, edit, typecorrect

def UpdateInfoAboutClient(from_user: types.User, bot_text: str):

    prev:int = -1
    action:str = ''
    lastname:str = ''
    username:str = ''

    if from_user.last_name:
        lastname = from_user.last_name
    if from_user.username:
        username = from_user.username

    if from_user.language_code:
        if bot_text != Strings[from_user.language_code]["ups_no_profile"]:
            prev, action = EvPrevMsgId(from_user.id, from_user.first_name, lastname, username, from_user.language_code)
    return prev, action


async def SendAMessage(text: str, kbd: types.InlineKeyboardMarkup, prmode: str, address: list[float], img: str, file_ids: list[str], edit: bool, typecorrect: bool, typeoffiles: list[str], from_user: types.User, media_group_id: str | None, pre_id: int):
    rmid:int = -1
    reply: types.Message | None
    mgid:str = ''
    if typecorrect:
        if img == '':
            if address == []:
                if not edit:
                    if file_ids == []:
                        reply = await bot.send_message(from_user.id, text=text, parse_mode=prmode, reply_markup=kbd)
                    else:
                        reply = await SendMediaGroup(file_ids, typeoffiles, from_user, text, prmode, kbd)
                    if reply is not None:
                        rmid = reply.message_id
                    else:
                        rmid = -1
                else:
                    await bot.edit_message_text(text=text, chat_id=from_user.id, message_id=pre_id, reply_markup=kbd)
                    rmid = pre_id
            else:
                reply = await bot.send_message(from_user.id, text=text, parse_mode=prmode, reply_markup=kbd)
                rmid = reply.message_id
                await bot.send_location(from_user.id, latitude=address[0], longitude=address[1])
        else:
            photo_ai = types.FSInputFile(img)
            reply = await bot.send_photo(chat_id=from_user.id, photo=photo_ai, caption=text, parse_mode=prmode, reply_markup=kbd)
            rmid = reply.message_id
    else:
        reply = await bot.send_message(from_user.id, text="К сожалению, пока что я принимаю только текстовые сообщения и иногда фото и видео.")
        rmid = reply.message_id
    
    if media_group_id:
        mgid = media_group_id
    RetainPrevMsgId(from_user.id, rmid, mgid) 



@router.message()
async def all_mes(message: types.Message):
    global processor
    queue.append(message)
    if processor == None or processor.done() == True:
        processor = asyncio.create_task(Process())

async def Process():
    while 0 < len(queue):
        message = queue[0]
        del queue[0]
        await VecMess2(message)

async def VecMess2(message: types.Message):

    message.message_id

    text:str = ''
    kbd:types.InlineKeyboardMarkup
    halt:bool = False
    exmess:int = -1
    mes_act:str = ''
    prmode:str = ''
    address:list[float] = []
    img:str = ''
    file_ids:list[str] = []
    edit:bool = False
    typecorrect:bool = False
    typeoffiles: list[str] = []
    photo_id:str = ''
    video_id:str = ''

    if message.photo:
        photo_id = message.photo[1].file_id
    elif message.video:
        video_id = message.video.file_id

    file_id:list[str] = [photo_id, video_id]

    #namer = Namer
    if message.from_user:
        (text, kbd, halt, prmode, address, img, file_ids, typeoffiles, edit, typecorrect) = InputSelection(message.content_type, message.from_user, file_id, message.media_group_id, message.text)
        exmess, mes_act = UpdateInfoAboutClient(message.from_user, text)
        if (mes_act == 'DEL') and (exmess != -1):
            try:
                chat = message.from_user.id 
                print(chat, exmess)
                await bot.delete_message(chat_id=chat, message_id=exmess)
            except TelegramBadRequest:
                print("bot couldn't delete the message")
        print(message.media_group_id)
        await SendAMessage(text, kbd, prmode, address, img, file_ids, edit, typecorrect, typeoffiles, message.from_user, message.media_group_id, exmess)
    else:
        print("User doesn't have 'from_user' aiogram class")
        assert(False)

@router.callback_query()
async def VecCallBack(query: types.CallbackQuery):
    exmess:int = -1
    mes_act:str = ''
#    namer = Namer
    (text, kbd, halt, prmode, address, img, file_ids, typeoffiles, edit, typecorrect) = InputSelection('text', query.from_user, [], None, query.data)
    exmess, mes_act = UpdateInfoAboutClient(query.from_user, text)
    if mes_act == 'DEL' and exmess != -1:
        try:
            chat = query.from_user.id 
            print(chat, exmess)
            await bot.delete_message(chat_id=chat, message_id=exmess)
        except TelegramBadRequest:
            print("bot couldn't delete the message")
    await SendAMessage(text, kbd, prmode, address, img, file_ids, edit, typecorrect, typeoffiles, query.from_user, None, exmess)

async def main():
    print("Запустился")
    #asyncio.create_task(CheskWhoSleep("check who sleep"))
    #asyncio.create_task(CheskWhoSleep("who need notif"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)


async def CheskWhoSleep(task: str):
    global monitor
   # db.ConnectTo(host, user, password, db_name)
    print("hello")
    print(monitor)
    while True:
        await asyncio.sleep(5)  # Ждать 10 минут
       # while monitor == True:
           # await asyncio.sleep(2)
       #assert(monitor == False)
        #monitor = True
        if task == "check who sleep":
            print("started")
            text_list, keyboards, user_ids, exmessids  = BotCheskWhoSleep()
        else:
            print("notifstarted")
            text_list, keyboards, user_ids, exmessids  = WhoNeedNotification()
        if text_list != [] and keyboards != [] and user_ids != []:
            for id, text, exid, kbd in zip(user_ids, text_list, exmessids, keyboards):
                if exid != -1:
                    try:
                        await bot.delete_message(id, message_id=exid)
                    except TelegramBadRequest:
                        print("bot couldn't delete the message")
                reply = await bot.send_message(chat_id=id, text=text, reply_markup=typing.cast(types.InlineKeyboardMarkup, kbd))
                RetainPrevMsgId(id, reply.message_id, '')
        else:
            print("Спящих не обнаруженно!ZzZzZzZzZzZ")

if __name__ == "__main__":
    print("...")
    asyncio.run(main())
   