from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn, testUpdatedChatOrNo
from Admin_bot.Activities.activities_keyboard import DirectionsForChatGame, SendOrNo, LetsGO
from Admin_bot.Activities.activities_database import SelectLengthChats, SelectAllInfFromSchedule, SelectYourClients, FindChats
from Admin_bot.Settings.settings_keyboard import Language
from Admin_bot.Game.game_database import LengthOfGames, ScheduleOfGames
from Admin_bot.language_dictoinary import String as S
import language_dictionary_for_all as foralllang
import used_by_everyone as forall


class actChats:
    chat_launch_point:int
    game_launch_point:int
    chat_id:int
    game_id:int
    language:str


def StrSeats(seats: int, lang: str, users: list[tuple[str, str]]) -> str:
    i:int = 0
    paragraph:str = ''
    while i < seats:
        if i < len(users):
            space = f"{users[i][0]} {users[i][1]}"
        else:
            space = S[lang]["theseatsisfree"]
        paragraph += S[lang]["seats_counter"] % (i, space)
        i += 1
    return paragraph



def FoundChats(text: str, kbd: object, lang: str, chatinf: list[tuple[int, str]]):
    length:int = SelectLengthChats()
    assert(text == S[lang]["game_rules"] + S[lang]["foundchats"])
    assert(kbd == forall.Chats(chatinf, 7, actChats.chat_launch_point, length))
    assert(2 == testSelectLevel(738070596))

def NoChat(text: str, kbd: object, lang: str):
    assert(text == S[lang]["no_new_chats"])
    assert(kbd == DirectionsForChatGame(S[lang]["show_chats"], S[lang]["new_chat"], foralllang.String[lang]["main_menu_kb"]))
    assert(2 == testSelectLevel(738070596))
    assert('' == testSelectSomthingColumn(738070596, "activities_direction"))

def CorrectChatId(text: str, kbd: object, lang: str, launch_point: int, phrase: str):
    length:int = LengthOfGames()
    schedule_input:list[tuple[int, str, int, int]] = ScheduleOfGames(launch_point, 7)
    _schedule_, schedule_output = forall.SheduleStr([], schedule_input, lang)
    assert(text == S[lang]["choose_game_for_chatgame"])
    assert(kbd == forall.Schedule(schedule_output, 7, launch_point, '', length))
    assert(3 == testSelectLevel(738070596))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "activities_chat_id"))
    
def CorrectGameId(text: str, kbd: object, lang: str, phrase: str):
    assert(text == S[lang]["choose_language"])
    assert(kbd == Language(S[lang]["ru"], S[lang]["en"], S[lang]["tur"], foralllang.String[lang]["main_menu_kb"]))
    assert(4 == testSelectLevel(738070596))
    assert(int(phrase) == testSelectSomthingColumn(738070596, "activities_game_id"))

def SendChatGame(text: str, chattext: str, kbd: object, chatkbd: object, lang: str, chatid: int):
    sport, date, time, seats, price, currency, lat, long, nameaddress = SelectAllInfFromSchedule(actChats.game_id)
    users_from_db = SelectYourClients(actChats.game_id)
    users:list[tuple[str, str]] = []
    for name, lastname in users_from_db:
        if name == "no_data":
            name = foralllang.String[lang][name]
        elif lastname == "no_data":
            lastname = foralllang.String[lang][lastname]
        users.append((name, lastname))

    assert(text == S[lang]["chatgame_sended"] +  foralllang.String[lang]["main_menu_text"])
    assert(chattext == S[lang]["start_chatgame"] + S[lang]["sport+date+time+seats+price+currency+link+nameaddress"] % (foralllang.String[lang][sport], forall.CreateDateStr(date), forall.CreateTimeStr(time), seats, price, currency, lat, long, nameaddress) + (StrSeats(seats, lang, users)))
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert(chatkbd == LetsGO(S[lang]["participate"], actChats.game_id))
    assert(3 == testSelectLevel(738070596))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))
    assert(actChats.chat_id == chatid)
    assert(True == testUpdatedChatOrNo(actChats.chat_id, actChats.language))

def CorrectLanguage(text: str, kbd: object, lang: str, phrase: str):
    sport, date, time, seats, price, currency, lat, long, nameaddress = SelectAllInfFromSchedule(actChats.game_id)
    users_from_db = SelectYourClients(actChats.game_id)
    users:list[tuple[str, str]] = []
    for name, lastname in users_from_db:
        if name == "no_data":
            name = foralllang.String[lang][name]
        elif lastname == "no_data":
            lastname = foralllang.String[lang][lastname]
        users.append((name, lastname))

    assert(text == S[lang]["example_of_chat_game"] + S[phrase]["start_chatgame"] + S[phrase]["sport+date+time+seats+price+currency+link+nameaddress"] % (foralllang.String[phrase][sport], forall.CreateDateStr(date), forall.CreateTimeStr(time), seats, price, currency, lat, long, nameaddress) + (StrSeats(seats, phrase, users)))
    assert(kbd == SendOrNo(S[lang]["send"], foralllang.String[lang]["main_menu_kb"]))
    assert(5 == testSelectLevel(738070596))
    assert(phrase == testSelectSomthingColumn(738070596, "activities_chat_language"))

def NewChat(lang: str):
    (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, 'codeword', lang)
    if halt:
        chatinf = FindChats(7, actChats.chat_launch_point)
        FoundChats(text, kbd, lang, chatinf)
    else:
        NoChat(text, kbd, lang)
    assert(prmode == '')
    assert(spreadsheet == '')
    assert(fixed == findchats == False)
    assert(chatid == -1)
    assert(chattext == '')
    assert(chatkbd == None)

def InputDir(directions: list[str], lang: str):
    item:str = ''
    for item in directions:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            if item == "show chats":
                actChats.chat_launch_point = testSelectSomthingColumn(738070596, "activities_launch_point")
                chatinf = FindChats(7, actChats.chat_launch_point)
                if chatinf != []:
                    FoundChats(text, kbd, lang, chatinf)
                else:
                    NoChat(text, kbd, lang)
            else:
                assert(findchats == True)
                NewChat(lang)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputChatId(chatids: list[str], lang: str):
    item:str = ''
    for item in chatids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            actChats.game_launch_point = testSelectSomthingColumn(738070596, "game_launch_point")
            actChats.chat_id = int(item)
            CorrectChatId(text, kbd, lang, actChats.game_launch_point, item)
        else:
            actChats.chat_launch_point = testSelectSomthingColumn(738070596, "activities_launch_point")
            chatinf = FindChats(7, actChats.chat_launch_point)
            FoundChats(text, kbd, lang, chatinf)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputGameId(game_ids: list[str], lang: str):
    item:str = ''
    for item in game_ids:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            actChats.game_id = int(item)
            CorrectGameId(text, kbd, lang, item)
        else:
            actChats.game_launch_point = testSelectSomthingColumn(738070596, "game_launch_point")
            print("game_launch_point =", actChats.game_launch_point)
            CorrectChatId(text, kbd, lang, actChats.game_launch_point, str(actChats.chat_id))
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputLanguage(languages: list[str], lang: str):
    item:str = ''
    for item in languages:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            actChats.language = item
            CorrectLanguage(text, kbd, lang, item)
            assert(prmode == "HTML")
        else:
            CorrectGameId(text, kbd, lang, str(actChats.game_id))
        assert(chattext == '')
        assert(chatkbd == None)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)


def InputSend(sendcomm: list[str], lang: str):
    item:str = ''
    for item in sendcomm:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            SendChatGame(text, chattext, kbd, chatkbd, lang, chatid)
            assert(prmode == '')
        else:
            CorrectLanguage(text, kbd, lang, actChats.language)
            assert(prmode == 'HTML')
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)

def HeadFunc(alloflist: list[str], lang: str, level: int):
    if level == 2:
        InputChatId(alloflist, lang)
    elif level == 3:
        InputGameId(alloflist, lang)
    elif level == 4:
        InputLanguage(alloflist, lang)
    elif level == 5:
        InputSend(alloflist, lang)
    else:
        assert(False)