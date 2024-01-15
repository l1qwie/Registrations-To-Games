import tools_database
import random
from typing import Any
from datetime import datetime, timedelta
from secretdata import phiz_host, phiz_user, phiz_password, phiz_db_name

tools_database.ConnectTo(phiz_host, phiz_user, phiz_password, phiz_db_name)

def ChangeSomeThing(table: str, column: str, value: Any, comparison: str, condition: Any):
    tools_database.ChangeSomeThing(table, column, value, comparison, condition)

#Tools
#All About Schedule
def DateOnTheWeek() -> int:
    current_date = datetime.now()
    random_offset = random.randint(1, 6)
    new_date = current_date - timedelta(days=random_offset)
    return int(new_date.strftime("%Y%m%d"))

def RandomDate() -> int:
    year = random.randint(2023, 2024)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return int(f"{year:04d}{month:02d}{day:02d}")

def RandomFutureDate() -> int:
    year = random.randint(2024, 2025)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return int(f"{year:04d}{month:02d}{day:02d}")

def CreateRandomGameInSchedule() -> tuple[str, int, int, int, float, float, str, int, str]:
    sport:str = ''
    time:int = -1 
    seats:int = -1
    status:int = 1
    latitude:float = -1
    longitude:float = -1
    address:str = ''
    price:int = -1
    currency:str = ''
    random_index:int = -1

    sport_list:list[str] = ["volleyball", "football"]
    address_list:list[str] = ["Пристань на берегу моря", "Какое то место", "Дом"]
    currency_list:list[str] = ["USD", "EURO", "TL", "RUB", "PESO"]

    random_index = random.randint(0, 1)
    sport = sport_list[random_index]
    random_index = random.randint(0, 2)
    address = address_list[random_index]
    random_index = random.randint(0, 4)
    currency = currency_list[random_index]
    seats = random.randint(55, 122)    
    price = random.randint(10, 150)

    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    time = int(f"{hour:02d}{minute:02d}")

    latitude = round(random.uniform(-90.000000, 90.000000), 6)
    longitude = round(random.uniform(-180.000000, 180.000000), 6)

    return (sport, time, seats, status, latitude, longitude, address, price, currency)


def HeadOfCreateRandomGames() -> int:
    date:int = RandomDate()
    sport, time, seats, status, latitude, longitude, address, price, currency = CreateRandomGameInSchedule()
    game_id = tools_database.CreateGameInSchedule(sport, date, time, seats, status, latitude, longitude, address, price, currency)
    print(f"Game with game_id = {game_id} have been create")
    return game_id

def HeadOfCreateOnTheWeekGames() -> int:
    date:int = DateOnTheWeek()
    sport, time, seats, status, latitude, longitude, address, price, currency = CreateRandomGameInSchedule()
    game_id = tools_database.CreateGameInSchedule(sport, date, time, seats, status, latitude, longitude, address, price, currency)
    print(f"Game with game_id = {game_id} have been create")
    return game_id

def HeadOfCreateFutureGames() -> int:
    date = RandomFutureDate()
    sport, time, seats, status, latitude, longitude, address, price, currency = CreateRandomGameInSchedule()
    game_id = tools_database.CreateGameInSchedule(sport, date, time, seats, status, latitude, longitude, address, price, currency)
    print(f"Game with game_id = {game_id} have been create")
    return game_id

def ShowAllSchedule():
    schedule:list[tuple[int, str, int, int, int, str, float, float, str, int, str]] = tools_database.SelectAllSchedule()
    string:tuple[int, str, int, int, int, str, float, float, str, int, str]

    for string in schedule:
        print(string)

def DeleteGameInSchedule(game_id: int):
    tools_database.DeleteGameInSchedule(game_id)
    print(f"Game with game_id = {game_id} removed")

def ChangeColumnInScheduleTable(column: str, value: Any, game_id: int):
    tools_database.ChangeColumnInScheduleTable(column, value, game_id)
    print(f"Column {column} in table Schedule chenged")

def DeleleAllGamesInSchedule():
    tools_database.DeleleAllGamesInSchedule()
    print("All games in schedule has been delete")


#All About Users
def ShowAllUsers():
    users:list[tuple[int, str, str, str, str, str, str, bool]] = tools_database.SelectAllUsers()
    string:tuple[int, str, str, str, str, str, str, bool]

    for string in users:
        print(string)

def ChangeUsers(column: str, value:Any, user_id: int):
    tools_database.ChangeColumnInUsersTable(column, value, user_id)
    print(f"Column {column} in table Users chenged")
 
def CreateInfUser() -> tuple[str, str, int, str]:
    names = ["Васлий", "Егор", "Ahmet", "Jhon", "Moisha"]
    last_names = ["Дмитриев", "Егоров", "Yılmaz", "Jhonson", "Evreevich"]

    from_where = ["tg", "wapp", "calling", "vb"]

    random_index = random.randint(0, 4)
    name = names[random_index]
    last_name = last_names[random_index]

    random_index = random.randint(0, 3)
    phone = random.randint(10**10, 10**11 - 1)
    fw = from_where[random_index]

    return name, last_name, phone, fw

def CreateUser() -> int:
    name, last_name, phone, fw = CreateInfUser()
    user_id:int = tools_database.CreateUser(name, last_name, phone, fw)
    print(f"You created a new user with data: {name}, {last_name}, {phone}, {fw}")

    return user_id

def DeleteUsers(user_id: int):
    tools_database.DeleteUser(user_id)
    print(f"User with user_id {user_id} has been delete")

def DeleteAllUsers():
    tools_database.DeleteAllUsers()
    print("We deleted all users")



#RegToGames
def ShowAllRegistrtions():
    schedule:list[tuple[int, int, int, str, bool]] = tools_database.ShowAllRegistrtions()
    string:tuple[int, int, int, str, bool]

    for string in schedule:
        print(string)

def RegistrationUserToGames(user_id: int, game_id: int):
    print("??")

    freeseats:int = -1
    paymmethods:list[str] = ["card", "cash"]

    freeseats = tools_database.SelectSeats(game_id)
    seats = random.randint(1, 3)
    payment = paymmethods[random.randint(0, 1)]

    tools_database.RegistrationUserForGames(game_id, freeseats, seats, payment, user_id)
    print(f"User with id: {user_id} has been register for game with game_id {game_id} with seats {seats} and paymethod is {payment}")

def UnRegistrationUserToGames(user_id: int, game_id: int):
    tools_database.UnRegistrationUserToGames(user_id, game_id)
    print("User was unregister")
    
def ChangeRegistrationUserToGames(column: str, value:str, user_id: int, game_id: int):
    tools_database.ChangeRegistrationUserToGames(column, value, user_id, game_id)
    print("User registration has been change")

#Media
def ShowAllGamesInMediaRepository():
    schedule:list[tuple[int, int, int, str, str, bool]] = tools_database.ShowAllGamesInMediaRepository()
    string:tuple[int, int, int, str, str, bool]

    for string in schedule:
        print(string)

def ShowAllMediaFromOneGames(game_id: int) -> int:
    schedule:list[tuple[int, int, int, str, str, bool]] = tools_database.ShowAllMediaFromOneGames(game_id)
    string:tuple[int, int, int, str, str, bool]
    for string in schedule:
        print(string)
    return len(schedule)

def AddANewFile(game_id: int):
    file_ids:list[str] = ["AgACAgIAAxkBAAIwSWUn_HNyyQs81dTEi0FVbY-9RXuJAAJH1DEboK9BSQknLDf2cTJfAQADAgADbQADMAQ", "AgACAgIAAxkBAAIwSmUn_HMmgUano2BRbIm7Un87swbMAAJI1DEboK9BSQVlSUlgbRjqAQADAgADbQADMAQ", "AgACAgIAAxkBAAIwS2Un_HOmj_tW54wY902G1ZJrarT6AAJJ1DEboK9BSbAR6W9wxw4xAQADAgADbQADMAQ"]
    typeoffiles:list[str] = ["photo"]

    file_id:str = file_ids[random.randint(0, 2)]
    typeoffile:str = typeoffiles[0] # this is a temporary measure

    tools_database.AddANewFile(file_id, typeoffile, game_id)

def RandomDeleteAFile(game_id: int):
    schedule:list[tuple[int, int, int, str, str, bool]] = tools_database.ShowAllGamesInMediaRepository()
    media_id = random.choice(schedule)[0]
    tools_database.RandomDeleteAFile(media_id)

def CreateEmptyRadnomMediaGame() -> int:
    game_id:int = HeadOfCreateRandomGames()
    tools_database.DeleteGameForMedia(game_id)
    #AddANewFile(game_id)
    return game_id

def CreateEmptyGameOnTheWeek() -> int:
    game_id:int = HeadOfCreateOnTheWeekGames()
    tools_database.DeleteGameForMedia(game_id)
    AddANewFile(game_id)
    return game_id

#Admins
def ResetAdmin(id: int):
    tools_database.ResetAdmin(id)
    print(f"Admin with id {id} has been reset")

def ChangeAdmin(id: int, column: str, value: Any, type: str):
    if type == "str":
        tools_database.ChangeAdminStr(id, column, str(value))
    elif type == "int":
        tools_database.ChangeAdminInt(id, column, int(value))
    print(f"Admin with id {id} has been change. Change column {column} to {value}")


#Create Game
def ResetForCreateGame(id: int):
    tools_database.ResetForCreateGame(id)

#Chats
def DeleteAllChats():
    tools_database.DeleteAllChats()

def AddSomeChats() -> int:
    i:int = 0
    chatid:int = -1
    titles:list[str] = ['Дождь', 'Воллейбол стамбул', 'кирокор поет', 'Ну и еще что то']
    how_mutch = random.randint(0, 9)

    while i < how_mutch:
        chatid = random.randint(12313, 323445)
        title = titles[random.randint(0, 3)]
        tools_database.AddSomeChats(chatid, title)
        i += 1
        
    return chatid

def CreateChat() -> int:
    chatid:int = random.randint(12313, 323445)
    titles:list[str] = ['Дождь', 'Воллейбол стамбул', 'кирокор поет', 'Ну и еще что то']
    title = titles[random.randint(0, 3)]
    tools_database.AddSomeChats(chatid, title)
    return chatid

def DeleteChat(chat_id: int):
    tools_database.DeleteChat(chat_id)


#Delete all wait games
def DeleteAllWaitGames():
    tools_database.DeleteAllWaitGames()

def DeleteWaitGame(game_id: int, user_id: int):
    tools_database.DeleteWaitGame(game_id, user_id)

#Paid
def Paid(user_id: int, game_id: int):
    tools_database.Paid(user_id, game_id)