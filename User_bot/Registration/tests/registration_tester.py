from User_bot.Main.tests.main_database_test import testSelectSomthingColumn, testSelectLevel, testDataFitting
from User_bot.Main.main_action import DispatchPhrase
from User_bot.Registration.registration_database import SelectAllScheduleData, WhatAboutMoney, SelectSport, SelectDate, SelectTime, SelectAdressGame
from User_bot.language_dictionary import Strings as S
import used_by_everyone as forall
import language_dictionary_for_all


text:str = ''
kbd:object = None
halt:bool = False
prmode:str = ''
address:list[float] = []
img:str = ''
edit:bool = False
files_id:list[str] = []
typeoffile:list[str] = []


#action functions
def ShowScheedule(text: str, kbd: object, lang: str):
    
    game_id:int = -1
    sport:str = ''
    date:int = 0
    date_str:str = ''
    time:int = 0
    time_str:str = ''
    seats:int = 0
    schedule:list[tuple[str, str, str, str, str]] = []
    launch_point = testSelectSomthingColumn(738070596, "launch_point_reg_to_game")
    print("launch_point_reg_to_game =", launch_point)

    schedule_data:list[tuple[int, str, int, int, int]] = SelectAllScheduleData(7, launch_point)
    for game_id, sport, date, time, seats in schedule_data:
        sport = S[lang][sport]
        date_str = forall.CreateDateStr(date)
        time_str = forall.CreateTimeStr(time)
        schedule.append((str(game_id), sport, date_str, time_str, str(seats)))

    assert(text == S[lang]["what_interesing"])
    assert(kbd == forall.Schedule(schedule, 7, launch_point, S[lang]["free_seats"], 0))
    assert(1 == testSelectLevel(738070596))

def AdoptionGameId(text: str, kbd: object, lang: str, phrase: str):

    money:int = -1
    currency:str = ''

    assert(int(phrase) == testSelectSomthingColumn(738070596, "game_id_reg_to_game"))
    money, currency = WhatAboutMoney(int(phrase))
    assert(text == S[lang]["discussion_seats"] % (money, currency))
    assert(kbd ==forall.FrequentChoice(S[lang]["alone"], S[lang]["with_two"], S[lang]["with_three"]) )
    assert(2 == testSelectLevel(738070596))

def AdoptionSeats(text: str, kbd: object, lang: str, phrase: str):
    assert(int(phrase) == testSelectSomthingColumn(738070596, "seats_reg_to_game"))
    assert(text == S[lang]["choose_payment"])
    assert(kbd == forall.KbPay(S[lang]["pay_online"], S[lang]["pay_cash"], language_dictionary_for_all.String[lang]["main_menu_kb"]))
    assert(3 == testSelectLevel(738070596))

def WrongSeats(text: str, kbd: object, lang: str):
    assert(text == S[lang]["wrond_number"])
    assert(kbd == forall.FrequentChoice(S[lang]["alone"], S[lang]["with_two"], S[lang]["with_three"]))
    assert(2 == testSelectLevel(738070596))

def AdoptionPayment(text: str, kbd: object, lang: str, img: str):

    money:int = -1
    currency:str = ''
    price:int = -1
    game_id:int = testSelectSomthingColumn(738070596, "game_id_reg_to_game")
    seats:int = testSelectSomthingColumn(738070596, "seats_reg_to_game")

    money, currency = WhatAboutMoney(game_id)
    price = money * seats
    assert(text ==S[lang]["online_oplata"] % (price, currency))
    assert(kbd == forall.Papara(S[lang]["pay"], S[lang]["next"]))
    assert(img == 'qr.jpg')
    assert(4 == testSelectLevel(738070596))

def Congratulations(text: str, kbd: object, lang: str, prmode: str, address: list[float]):

    date:str = ''
    time:str = ''
    payment:str = ''
    money:int = -1
    currency:str = ''
    finalyprice:int = -1

    game_id:int = testSelectSomthingColumn(738070596, "game_id_reg_to_game")
    seats:int = testSelectSomthingColumn(738070596, "seats_reg_to_game")
    sport:str = SelectSport(game_id)
    payment:str = testSelectSomthingColumn(738070596, "payment_reg_to_game")


    sport = S[lang][sport] 
    payment = S[lang][payment]
    date = forall.CreateDateStr(SelectDate(game_id))
    time = forall.CreateTimeStr(SelectTime(game_id))
    money, currency = WhatAboutMoney(game_id)
    finalyprice = money * seats

    assert(address == SelectAdressGame(game_id))
    print(S[lang]["grac_to_reg"] % (sport, date, time, seats, payment, finalyprice, currency, address[0], address[1]))
    assert(text ==  S[lang]["grac_to_reg"] % (sport, date, time, seats, payment, finalyprice, currency, address[0], address[1]))
    assert(kbd == forall.Options(S[lang]["first_option"], S[lang]["second_option"], S[lang]["third_option"], S[lang]["fourth_option"]))
    assert(prmode == 'HTML')
    assert(3 == testSelectLevel(738070596))


#header functions
def PresentationScheduele(first_message: list[str], lang: str):
    item:str = ''
    for item in first_message:
        testDataFitting("reg to games", 0, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        ShowScheedule(text, kbd, lang)
        assert(halt == False)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])

def ChooseSeats(game_ids: list[str], lang: str):
    item:str = ''
    for item in game_ids:
        testDataFitting("reg to games", 1, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if item in ("next page", "previous page") or not halt:
            ShowScheedule(text, kbd, lang)
        elif halt:
            AdoptionGameId(text, kbd, lang, item)
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])

def ChoosePay(list_of_seats: list[str], lang: str):
    item:str = ''
    for item in list_of_seats:
        testDataFitting("reg to games", 2, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if forall.IntCheck(item):
            print("HALT", halt)
            if halt:
                AdoptionSeats(text, kbd, lang, item)
            else:
                WrongSeats(text, kbd, lang)
        else:
            game_id:int = testSelectSomthingColumn(738070596, "game_id_reg_to_game")
            AdoptionGameId(text, kbd, lang, str(game_id))
        assert(prmode == '')
        assert(address == [])
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])

def CardPayment(payments: list[str], lang: str):
    item:str = ''
    for item in payments:
        testDataFitting("reg to games", 3, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        if halt:
            assert(item == testSelectSomthingColumn(738070596, "payment_reg_to_game"))
            if item == "card":
                AdoptionPayment(text, kbd, lang, img)
                assert(address == [])
                assert(prmode == '')
            else:
                Congratulations(text, kbd, lang, prmode, address)
                assert(img == '')
        else:
            seats:int = testSelectSomthingColumn(738070596, "seats_reg_to_game")
            AdoptionSeats(text, kbd, lang, str(seats))
            assert(img == '')
            assert(address == [])
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])

def BestWishes(Congrac_of_list: list[str], lang: str):
    item:str = ''
    for item in Congrac_of_list:
        testDataFitting("reg to games", 4, 738070596)
        (text, kbd, halt, prmode, address, img, files_id, typeoffile, edit) = DispatchPhrase(738070596, item, lang)
        Congratulations(text, kbd, lang, prmode, address)
        assert(halt == False)
        assert(img == '')
        assert(edit == False)
        assert(files_id == [])
        assert(typeoffile == [])