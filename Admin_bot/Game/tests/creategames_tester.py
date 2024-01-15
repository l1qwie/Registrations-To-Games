from Admin_bot.Main.tests.main_database_test import testSelectLevel, testSelectSomthingColumn
from Admin_bot.Main.main_action import DispatchPhrase
from Admin_bot.language_dictoinary import String as S
from Admin_bot.Game.game_keyboard import GamesOptions, SaveorChange
import language_dictionary_for_all as foralllang
import used_by_everyone as forall



class CreateGame:
    sport:str
    date:str
    time:str
    seats:int
    price:int
    currency:str
    latitude:float
    longitude:float
    address:str

#action functions
def CorrectPhrase(text: str, kbd: object, lang: str):
    assert(text == S[lang]["start_create_game"])
    assert(2 == testSelectLevel(738070596))
    assert("create games" == testSelectSomthingColumn(738070596, "direction"))

def Directions(text: str, kbd: object, lang: str):
    assert(text == S[lang]["games_directions"])
    assert(kbd == GamesOptions(S[lang]["change_games"], S[lang]["create_games"], S[lang]["delete_games"]))
    assert(1 == testSelectLevel(738070596))

def CorrectSport(text: str, kbd: object, lang: str, prmode: str):
    assert(text == S[lang]["onlysport"] % (CreateGame.sport) + S[lang]["writedate"])
    assert(3 == testSelectLevel(738070596))
    assert(kbd == forall.GoToAdmin(foralllang.String[lang]["main_menu_kb"]))
    assert(prmode == 'HTML')

def CorrectDate(text: str, kbd: object, lang: str,  prmode: str):
    assert(text == S[lang]["sport+date"] % (CreateGame.sport, CreateGame.date) + S[lang]["whitetime"])
    assert(kbd == forall.GoToAdmin(foralllang.String[lang]["main_menu_kb"]))
    assert(4 == testSelectLevel(738070596))
    assert(prmode == 'HTML')

def CorrectTime(text: str, kbd: object, lang: str, prmode: str):
    assert(text == S[lang]["sport+date+time"] % (CreateGame.sport, CreateGame.date, CreateGame.time) + S[lang]["writeseats"])
    assert(kbd == forall.GoToAdmin(foralllang.String[lang]["main_menu_kb"]))
    assert(5 == testSelectLevel(738070596))
    assert(prmode == 'HTML')

def CorrectSeats(text: str, kbd: object, lang: str, prmode: str):
    assert(text == S[lang]["sport+date+time+seats"] % (CreateGame.sport, CreateGame.date, CreateGame.time, CreateGame.seats) + S[lang]["writeprice"])
    assert(kbd == forall.GoToAdmin(foralllang.String[lang]["main_menu_kb"]))
    assert(6 == testSelectLevel(738070596))
    assert(prmode == 'HTML')

def CorrectPrice(text: str, kbd: object, lang: str, prmode: str):
    assert(text == S[lang]["sport+date+time+seats"] % (CreateGame.sport, CreateGame.date, CreateGame.time, CreateGame.seats) + S[lang]["writecurrency"])
    assert(kbd == forall.GoToAdmin(foralllang.String[lang]["main_menu_kb"]))
    assert(7 == testSelectLevel(738070596))
    assert(prmode == 'HTML')

def SaveCurrency(text: str, kbd: object, lang: str, prmode: str):
    assert(text == S[lang]["sport+date+time+seats+price+currency"] % (CreateGame.sport, CreateGame.date, CreateGame.time, CreateGame.seats, CreateGame.price, CreateGame.currency) + S[lang]["writelink"])
    assert(kbd == forall.GoToAdmin(foralllang.String[lang]["main_menu_kb"]))
    assert(8 == testSelectLevel(738070596))
    assert(prmode == 'HTML')

def CorrectLink(text: str, kbd: object, lang: str, prmode: str):
    assert(text == S[lang]["sport+date+time+seats+price+currency+link"] % (CreateGame.sport, CreateGame.date, CreateGame.time, CreateGame.seats, CreateGame.price, CreateGame.currency, CreateGame.latitude, CreateGame.longitude) + S[lang]["writeaddress"])
    assert(kbd == forall.GoToAdmin(foralllang.String[lang]["main_menu_kb"]))
    assert(9 == testSelectLevel(738070596))
    assert(prmode == 'HTML')

def CorrectAddress(text: str, kbd: object, lang: str, prmode: str):
    assert(text == S[lang]["sport+date+time+seats+price+currency+link+nameaddress"] % (CreateGame.sport, CreateGame.date, CreateGame.time, CreateGame.seats, CreateGame.price, CreateGame.currency, CreateGame.latitude, CreateGame.longitude, CreateGame.address) + S[lang]["clarification"])
    assert(kbd == SaveorChange(S[lang]["savegame"], S[lang]["changegame"]))
    assert(10 == testSelectLevel(738070596))
    assert(prmode == 'HTML')

def Save(text: str, kbd: object, lang: str):
    assert(text == foralllang.String[lang]["gamewassave"] + foralllang.String[lang]["main_menu_text"])
    assert(kbd == forall.OptionsAdmin(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"], S[lang]["fifth_option"]))
    assert("divarication" == testSelectSomthingColumn(738070596, "action"))
    assert(3 == testSelectLevel(738070596))

#Header finctions
def ChooseSport(phrases: list[str], lang: str):
    item:str = ''
    for item in phrases:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CorrectPhrase(text, kbd, lang)
        else:
            Directions(text, kbd, lang)
        assert(prmode == '')
        assert(spreadsheet == '')
        assert(fixed == '')
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputSport(sports: list[str], lang: str):
    item:str = ''
    for item in sports:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CreateGame.sport = item
            CorrectSport(text, kbd, lang, prmode)
        else:
            CorrectPhrase(text, kbd, lang)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputDate(date_list: list[str], lang: str):
    item:str = ''
    for item in date_list:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CreateGame.date = forall.CreateDateStr(testSelectSomthingColumn(738070596, "game_date"))
            CorrectDate(text, kbd, lang, prmode)
        else:
            CorrectSport(text, kbd, lang, prmode)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputTime(time_list: list[str], lang: str):
    item:str = ''
    for item in time_list:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CreateGame.time = forall.CreateTimeStr(testSelectSomthingColumn(738070596, "game_time"))
            CorrectTime(text, kbd, lang, prmode)
        else:
            CorrectDate(text, kbd, lang, prmode)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputSeats(seats: list[str], lang: str):
    item:str = ''
    for item in seats:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CreateGame.seats = int(item)
            CorrectSeats(text, kbd, lang, prmode)
        else:
            CorrectTime(text, kbd, lang, prmode)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputPrice(prices: list[str], lang: str):
    item:str = ''
    for item in prices:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CreateGame.price = int(item)
            CorrectPrice(text, kbd, lang, prmode)
        else:
            CorrectSeats(text, kbd, lang, prmode)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputCurrecny(currecnes: list[str], lang: str):
    item:str = ''
    for item in currecnes:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        CreateGame.currency = item
        SaveCurrency(text, kbd, lang, prmode)
        assert(halt == False)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputLink(addreses: list[str], lang: str):
    item:str = ''
    for item in addreses:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        if halt:
            CreateGame.latitude = testSelectSomthingColumn(738070596, "game_latitude")
            CreateGame.longitude = testSelectSomthingColumn(738070596, "game_longitude")
            CorrectLink(text, kbd, lang, prmode)
        else:
            SaveCurrency(text, kbd, lang, prmode)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid  == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def InputAddress(addresses: list[str], lang: str):
    item:str = ''
    for item in addresses:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid) = DispatchPhrase(738070596, item, lang)
        CreateGame.address = item
        CorrectAddress(text, kbd, lang, prmode)
        assert(halt == False)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)

def SaveOrChange(save_or_change: list[str], lang: str):
    item:str = ''
    for item in save_or_change:
        (text, chattext, kbd, chatkbd, prmode, halt, spreadsheet, fixed, findchats, chatid)= DispatchPhrase(738070596, item, lang)
        if halt:
            Save(text, kbd, lang)
        else:
            #Change()
            pass
        print(prmode)
        assert(spreadsheet == '')
        assert(fixed == False)
        assert(findchats == False)
        assert(chatid == -1)
        assert(chattext == '')
        assert(chatkbd == None)
        

#Other Head Function
def CreateDiraction(infaboutnewgame:list[str], lang: str, level: int):
    if level == 2:
        InputSport(infaboutnewgame, lang)
    elif level == 3:
        InputDate(infaboutnewgame, lang)
    elif level == 4:
        InputTime(infaboutnewgame, lang)
    elif level == 5:
        InputSeats(infaboutnewgame, lang)
    elif level == 6:
        InputPrice(infaboutnewgame, lang)
    elif level == 7:
        InputCurrecny(infaboutnewgame, lang)
    elif level == 8:
        InputLink(infaboutnewgame, lang)
    elif level == 9:
        InputAddress(infaboutnewgame, lang)
    elif level == 10:
        SaveOrChange(infaboutnewgame, lang)
