from User_bot.Main.tests.main_database_test import testSelectSomeData, testSelectSeatsFromGame, testSelectSeatsFromWaitingUsers, testResetUser, testSelectSomthingColumn, UpdateLanguage
from User_bot.Main.tests.main_database_test import ConnectTo as mainConnectTo
from User_bot.Welcome.tests.welcome_tester import GreetingsToUser, WarningRules, GoToOptions
from User_bot.Registration.tests.registration_tester import PresentationScheduele, ChooseSeats, ChoosePay, CardPayment, BestWishes
from User_bot.secretdata import phiz_host, phiz_user, phiz_password, phiz_db_name
from User_bot.Media.tests.media_tester import FirstQuestion, ChoiceOfDirection, WhatGamesNeedToShow, StartLoading, InspectionFileId, SaveToMediaRep, CreateMediaList, TryAgainToSave
from User_bot.Settings.tests.settings_tester import ChooseDiractions, SetActions, GameSettings, SetiingsAction, IntermediateAction, TypeOfSetting
from User_bot.Settings.tests.settings_tester import ChangePaymethod as testChangePaymethod
from User_bot.Settings.settings_database import SelectSomeData
from User_bot.Settings.settings_database import ConnectTo as setConnectTo
import random
import tools

def FoundationMedia(first_message: list[str], directions: list[str], howmuthgames: list[str], lang: str):
    FirstQuestion(first_message, lang)
    ChoiceOfDirection(directions, lang)
    WhatGamesNeedToShow(howmuthgames, lang)

def ForLoading(first_message: list[str], directions: list[str], howmuthgames: list[str], lang: str,  game_id: int):

    selected_games:list[str] = ["cash", "121q23w3123", f"{game_id}"]
    endofload:list[str] = ["/asdjknhjk", "!@Q@#!", "END"]
    file_id_list:list[str] = ["AgACAgIAAxkBAAIwSWUn_HNyyQs81dTEi0FVbY-9RXuJAAJH1DEboK9BSQknLDf2cTJfAQADAgADbQADMAQ", "AgACAgIAAxkBAAIwSWUn_HNyyQs81dTEi0FVbY-9RXuJAAJH1DEboK9BSQknLDf2cTJfAQADAgADbQADMAQ", "AgACAgIAAxkBAAIwSWUn_HNyyQs81dTEi0FVbY-9RXuJAAJH1DEboK9BSQknLDf2cTJfAQADAgADbQADMAQ"]

    FoundationMedia(first_message, directions, howmuthgames, lang)
    StartLoading(selected_games, lang)
    InspectionFileId(file_id_list, lang)
    SaveToMediaRep(endofload, lang)

def ForViewing(first_message: list[str], directions: list[str], howmuthgames: list[str], lang: str,  game_id: int):
    selected_games:list[str] = ["cash", "121q23w3123", f"{game_id}"]
    FoundationMedia(first_message, directions, howmuthgames, lang)
    CreateMediaList(selected_games, lang)

def LoadingAllGames(first_message: list[str], directions: list[str], game_id: int, lang: str):
    howmuthgames:list[str] = ["112", "5", "all_games"]
    ForLoading(first_message, directions, howmuthgames, lang, game_id)

def LoadingLastGames(first_message: list[str], directions: list[str], game_id: int, lang: str):
    howmuthgames:list[str] = ["112", "5", "last_games"]
    ForLoading(first_message, directions, howmuthgames, lang, game_id)

def ViewingAllGames(first_message: list[str], directions: list[str], game_id: int, lang: str):
    howmuthgames:list[str] = ["112", "5", "all_games"]
    tools.AddANewFile(game_id)
    ForViewing(first_message, directions, howmuthgames, lang, game_id)

def ViewingLastGames(first_message: list[str], directions: list[str], game_id: int, lang: str):
    howmuthgames:list[str] = ["112", "5", "last_games"]
    tools.AddANewFile(game_id)
    ForViewing(first_message, directions, howmuthgames, lang, game_id)

def MediaLoading(lang: str):
    first_message:list[str] = ["111", "tyw2sr", "/start"]
    directions:list[str] = ["/[eessa]", "123131t", "loading"]

    game_id:int = tools.CreateEmptyRadnomMediaGame()
    LoadingAllGames(first_message, directions, game_id, lang)
    tools.DeleteGameInSchedule(game_id)

    game_id = tools.CreateEmptyGameOnTheWeek()
    LoadingLastGames(first_message, directions, game_id, lang)
    tools.DeleteGameInSchedule(game_id)

def MediaViewing(lang: str):
 
    first_message:list[str] = ["111", "tyw2sr", "/start"]
    directions:list[str] = ["/[eessa]", "123131t", "viewing"]

    game_id:int = tools.CreateEmptyRadnomMediaGame()
    ViewingAllGames(first_message, directions, game_id, lang)
    tools.DeleteGameInSchedule(game_id)

    #game_id = tools.CreateEmptyGameOnTheWeek()
    #ViewingLastGames(first_message, directions, game_id, lang)
    #tools.DeleteGameInSchedule(game_id)

def MediaLoadingTryAgain(lang: str):
    first_message:list[str] = ["111", "tyw2sr", "/start"]
    directions:list[str] = ["/[eessa]", "123131t", "loading"]
    second_try:list[str] = ["123123121a", "asdjkijle", "try again"]
    i:int = 0

    game_id:int = tools.CreateEmptyRadnomMediaGame()
    while i < 18:
        tools.AddANewFile(game_id)
        i += 1
    LoadingAllGames(first_message, directions, game_id, lang)
    TryAgainToSave(second_try, lang)
    tools.DeleteGameInSchedule(game_id)

    i = 0
    game_id:int = tools.CreateEmptyGameOnTheWeek()
    while i < 18:
        tools.AddANewFile(game_id)
        i += 1
    LoadingAllGames(first_message, directions, game_id, lang)
    TryAgainToSave(second_try, lang)
    tools.DeleteGameInSchedule(game_id)



def FoundationRegForGames(game_id: int, max_seats: int, lang: str):
    first_message:list[str] = ["/start", "111", "tyw2sr"]
    game_ids:list[str] = ["/[eessa]", "ejrerjqwe", f"{game_id}"]
    list_of_seats:list[str] = ["112", "asdasd", f"{random.randint(1, max_seats-1)}"]
    PresentationScheduele(first_message, lang)
    ChooseSeats(game_ids, lang)
    ChoosePay(list_of_seats, lang)
        
def PayCard(lang: str):
    paymenthod:list[str] = ["asdjikasd", "1231231124ax", "card"]
    CardPayment(paymenthod, lang)

def PayCash(lang: str):
    paymenthod:list[str] = ["asdjikasd", "1231231124ax", "cash"]
    CardPayment(paymenthod, lang)


def FoundationPaymthod(game_id: int, lang: str):

    directions:list[str] = ["/[eessa]", "ejrerjqwe", "seting regs"]
    chan_or_cont:list[str] = ["112", "asdasd", f"{game_id}"]
    direction_of_game:list[str] = ["cash", "121q23w3123", "change my game"]
    seats_or_payment:list[str] = ["/asdjknhjk", "12123", "change payment"]

    ChooseDiractions(directions, lang)
    SetActions(chan_or_cont, lang)
    GameSettings(direction_of_game, lang)
    SetiingsAction(seats_or_payment, lang)

def ChangeMySeats(game_id: int, max_seats: int, lang: str, us_seats: int, global_seats: int):
    directions:list[str] = ["/[eessa]", "ejrerjqwe", "seting regs"]
    chan_or_cont:list[str] = ["112", "asdasd", f"{game_id}"]
    direction_of_game:list[str] = ["cash", "121q23w3123", "change my game"]
    seats_or_payment:list[str] = ["/asdjknhjk", "12123", "change seats"]
    input_data = ["asdasdfqweq", "qweasdasdaweasf!@~!@~@", f"{random.randint(1, max_seats)}"]
    prev_global_seats, user_seats = testSelectSomeData(int(chan_or_cont[2]), 738070596)
    potential_seats_sum = (us_seats + global_seats) - int(input_data[2])
    print("DATA FROM GLOBAL TEST =", prev_global_seats, us_seats, potential_seats_sum)
    #                                       110             2           104

    ChooseDiractions(directions, lang)
    SetActions(chan_or_cont, lang)
    GameSettings(direction_of_game, lang)
    SetiingsAction(seats_or_payment, lang)
    IntermediateAction(input_data, lang, prev_global_seats, user_seats, potential_seats_sum)


def ChangeHeadOfSeats(lang: str):
    game_id:int = tools.HeadOfCreateRandomGames()
    
    tools.RegistrationUserToGames(738070596, game_id)

    schedule_seats:int = testSelectSeatsFromGame(game_id)
    user_seats:int = testSelectSeatsFromWaitingUsers(738070596, game_id)
    max_seats = schedule_seats + user_seats

    setConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    user_seats, global_seats, price, currency, payment_status = SelectSomeData(game_id, 738070596)
    #potential_seats_sum = (user_seats + global_seats) - potential_seats 
    ChangeMySeats(game_id, max_seats, lang, user_seats, global_seats)
    tools.DeleteGameInSchedule(game_id)
    print(price, currency, payment_status)


def ChangeMyPaymethodCard(game_id: int, lang: str, prev_global_seats: int, user_seats: int):
    input_data = ["asdasdfqweq", "123131", "card"]
    go_to = ["13131", "ASJKLDASJKLD", "Next"]
    _potential_seats_sum_:int = -1

    FoundationPaymthod(game_id, lang)

    IntermediateAction(input_data, lang, prev_global_seats, user_seats, _potential_seats_sum_)
    testChangePaymethod(go_to, lang)

def ChangeMyPaymethodCash(game_id: int, lang: str, prev_global_seats: int, user_seats: int):
    input_data = ["asdasdfqweq", "123131", "cash"]
    _potential_seats_sum_:int = -1
    
    FoundationPaymthod(game_id, lang)

    IntermediateAction(input_data, lang, prev_global_seats, user_seats, _potential_seats_sum_)

def ChangePaymethod(lang: str, prev_global_seats: int, user_seats: int):

    game_id:int = tools.HeadOfCreateRandomGames()
    tools.RegistrationUserToGames(738070596, game_id)
    ChangeMyPaymethodCash(game_id, lang, prev_global_seats, user_seats)
    tools.DeleteGameInSchedule(game_id)

    game_id:int = tools.HeadOfCreateRandomGames()
    tools.RegistrationUserToGames(738070596, game_id)

    ChangeMyPaymethodCard(game_id, lang, prev_global_seats, user_seats)
    tools.DeleteGameInSchedule(game_id)

def AlmostDeleteMyGame(game_id: int, lang: str):
    first_message:list[str] = ["asjklndajklsd", "1231231", "/start"]
    directions:list[str] = ["/[eessa]", "ejrerjqwe", "seting regs"] 
    chan_or_cont:list[str] = ["112", "asdasd", f"{game_id}"] 
    direction_of_game:list[str] = ["cash", "121q23w3123", "delete my game"] 

    TypeOfSetting(first_message, lang)
    ChooseDiractions(directions, lang)
    SetActions(chan_or_cont, lang)
    GameSettings(direction_of_game, lang)

def ChangeLanguage(lang: str):

    directions:list[str] = ["/[eessa]", "asds12121", "change language"]
    chan_or_cont:list[str] = ["112", "asdasd"]
    i:int = 0
    
    ChooseDiractions(directions, lang)
    while i < 3:
        lang = testSelectSomthingColumn(738070596, "language")
        if i == 0:
            chan_or_cont.append("en")
            SetActions(chan_or_cont, lang)
        elif i == 1:
            chan_or_cont.append("tur")
            SetActions(chan_or_cont, lang)
        elif i == 2:
            chan_or_cont.append("ru")
            SetActions(chan_or_cont, lang)
        i += 1

def ChangeMyGame(lang: str):

    ChangeHeadOfSeats(lang)
    ChangePaymethod(lang, 0, 0)

def DeleteMyGame(lang: str):

    game_id:int = tools.HeadOfCreateRandomGames()
    tools.RegistrationUserToGames(738070596, game_id)
    AlmostDeleteMyGame(game_id, lang)
    tools.DeleteGameInSchedule(game_id)

def ChangeMyRegistrations(lang: str):

    DeleteMyGame(lang)
    ChangeMyGame(lang)


def Welcome():
    mainConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    testResetUser(738070596)
    lang = testSelectSomthingColumn(738070596, "language")
    first_message:list[str] = ["/start", "111", "tyw2sr"]
    press_GoReg:list[str] = ["/[eessa]", "GoReg", "ejrerjqwe"]
    prees_GoNext:list[str] = ["/asdjknhjk", "12123", "GoNext"]

    GreetingsToUser(first_message, lang)
    WarningRules(press_GoReg, lang)
    GoToOptions(prees_GoNext, lang)

def RegAndPayByCash(lang: str):
    game_id:int = tools.HeadOfCreateRandomGames()
    max_seats:int = testSelectSeatsFromGame(game_id)
    FoundationRegForGames(game_id, max_seats, lang)
    PayCash(lang)
    tools.DeleteGameInSchedule(game_id)


def RegAndPayByCard(lang: str):
    Congrac_of_list:list[str] = ["/asdjknhjk", "12123", "Next"]
    game_id:int = tools.HeadOfCreateRandomGames()
    max_seats:int = testSelectSeatsFromGame(game_id)
    FoundationRegForGames(game_id, max_seats, lang)
    PayCard(lang)
    BestWishes(Congrac_of_list, lang)
    tools.DeleteGameInSchedule(game_id)

def CheckTheGameButtons(lang: str):
    game_ids:list[int] = []
    i:int = 0
    while i < 16:
        game_ids.append(tools.HeadOfCreateRandomGames())
        i += 1
    
    first_message:list[str] = ["/start", "111", "tyw2sr"]
    next:list[str] = ["/[eessa]", "ejrerjqwe", "next page"]
    previous:list[str] = ["/[eessa]", "ejrerjqwe", "previous page"]
    bouth:list[list[str]] = [next, previous]
    PresentationScheduele(first_message, lang)
    i = 0
    while i < 2:
        ChooseSeats(bouth[i], lang)
        i += 1
    
    i = 0
    while i < 16:
        tools.DeleteGameInSchedule(game_ids[i])
        i += 1


def RegForGames():
    mainConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    lang = testSelectSomthingColumn(738070596, "language")
    
    RegAndPayByCash(lang)
    RegAndPayByCard(lang)
    CheckTheGameButtons(lang)


def StartMediaOption():
    mainConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    UpdateLanguage(738070596)
    lang = testSelectSomthingColumn(738070596, "language")

    MediaLoading(lang)
    MediaViewing(lang)
    MediaLoadingTryAgain(lang)


def SeeUserRecords():
    mainConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)
    lang = testSelectSomthingColumn(738070596, "language")
    first_message:list[str] = ["/start", "111", "tyw2sr"]

    TypeOfSetting(first_message, lang)
    ChangeLanguage(lang)
    ChangeMyRegistrations(lang)

def GlobalTest():
    Welcome()
    RegForGames()
    StartMediaOption()
    SeeUserRecords()
