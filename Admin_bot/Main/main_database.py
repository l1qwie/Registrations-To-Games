import psycopg2
from typing import Any

connection: psycopg2.extensions.connection
cursor: psycopg2.extensions.cursor

#Routine
def ConnectTo(host: str, user: str, password: str, db_name: str):

    global connection, cursor


    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cursor = connection.cursor()

def FindNamedb(id: int) -> str:
    row:Any = None
    name_of_db:str = ''
    with connection:
        cursor.execute("SELECT db_name FROM clients WHERE user_id = %s AND status = 'ACTIVE'", (id,))
        row = cursor.fetchone()
        if row is not None:
            name_of_db = row[0]
            cursor.execute("UPDATE clients SET connection = 'connected' WHERE user_id = %s AND status = 'ACTIVE'", (id,))
        return name_of_db

def FindAdmin(id: int, language: str) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Admins WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
            else:
                cursor.execute("INSERT INTO Admins (user_id, action, language, level) VALUES (%s, 'registration', %s, %s)", (id, language, 0,))
        else:
            assert(False)
        return result

def RecallAdmin(user_id: int, name: str, last_name:str, language: str, action: str, direction: str,
                game_launch_point: int, game_sport: str, game_date: int, game_time: int, game_seats: int, game_price: int, game_currency: str, game_latitude: float, game_longitude: float, game_nameaddress: str, game_change_direction: str, game_game_id: int, game_change_create: bool, game_typeofchange: str,
                client_fromwhere: str, client_name: str, client_last_name: str, client_phonenum: int, client_user_id: int, client_change_option:str, client_launch_point: int, client_changeddata_str: str, client_changeddata_int: int, client_game_id: int, client_seats: int, client_paymethod: str, client_changedata_str: str, client_changedata_int: int,
                activities_actwithchats: str, activities_launch_point: int, activities_chat_id: int, activities_game_id: int, activities_chat_language: str,
                finances_user_id: int,
                level: int) -> tuple[int, str, str, str, str, str,
                                    int, str, int, int, int, int, str, float, float, str, str, int, bool, str,
                                    str, str, str, int, int, str, int, str, int, int, int, str, str, int,
                                    str, int, int, int, str,
                                    int,
                                    int]:
    row:Any = None
    with connection:
        cursor.execute("""SELECT user_id, name, last_name, language, action, direction,
                    game_launch_point, game_sport, game_date, game_time, game_seats, game_price, game_currency, game_latitude, game_longitude, game_nameaddress, game_change_direction, game_game_id, game_change_create, game_typeofchange,
                    client_fromwhere, client_name, client_last_name, client_phonenum, client_user_id, client_change_option, client_launch_point, client_changeddata_str, client_changeddata_int, client_game_id, client_seats, client_paymethod, client_changedata_str, client_changedata_int,
                    activities_actwithchats, activities_launch_point, activities_chat_id, activities_game_id, activities_chat_language,
                    finances_user_id,  
                    level 
                    FROM Admins WHERE user_id = %s""", (user_id,))
        row = cursor.fetchone()
        if row is not None:
            (user_id, name, last_name, language, action, direction,
            game_launch_point, game_sport, game_date, game_time, game_seats, game_price, game_currency, game_latitude, game_longitude, game_nameaddress, game_change_direction, game_game_id, game_change_create, game_typeofchange,
            client_fromwhere, client_name, client_last_name, client_phonenum, client_user_id, client_change_option, client_launch_point, client_changeddata_str, client_changeddata_int, client_game_id, client_seats, client_paymethod, client_changedata_str, client_changedata_int,
            activities_actwithchats, activities_launch_point, activities_chat_id, activities_game_id, activities_chat_language,
            finances_user_id,
            level) = row
        else:
            assert(False)
        return (user_id, name,  last_name, language, action, direction,
                game_launch_point, game_sport, game_date, game_time, game_seats, game_price, game_currency, game_latitude, game_longitude, game_nameaddress, game_change_direction, game_game_id, game_change_create, game_typeofchange,
                client_fromwhere, client_name, client_last_name, client_phonenum, client_user_id, client_change_option, client_launch_point, client_changeddata_str, client_changeddata_int, client_game_id, client_seats, client_paymethod, client_changedata_str, client_changedata_int,
                activities_actwithchats, activities_launch_point, activities_chat_id, activities_game_id, activities_chat_language,
                finances_user_id, 
                level)

def RetainAdmin(id: int, name: str, last_name: str, language: str, action: str, direction: str,
                game_launch_point: int, game_sport: str, game_date: int, game_time: int, game_seats: int, game_price: int, game_currency: str, game_latitude: float, game_longitude: float, game_nameaddress: str, game_change_direction: str, game_game_id: int, game_change_create: bool, game_typeofchange: str,
                client_fromwhere: str, client_name: str, client_last_name: str, client_phonenum: int, client_user_id: int, client_change_option:str, client_launch_point: int, client_changeddata_str: str, client_changeddata_int: int, client_game_id: int, client_seats: int, client_paymethod: str, client_changedata_str: str, client_changedata_int: int,
                activities_actwithchats: str, activities_launch_point: int, activities_chat_id: int, activities_game_id: int, activities_chat_language: str,
                finances_user_id: int,
                level: int):
    with connection:
        cursor.execute("""UPDATE Admins SET user_id = %s, name = %s, last_name = %s, language = %s, action = %s, direction = %s,
                       game_launch_point = %s, game_sport = %s, game_date = %s, game_time = %s, game_seats = %s, game_price = %s, game_currency = %s, game_latitude = %s, game_longitude = %s, game_nameaddress = %s, game_change_direction = %s, game_game_id = %s, game_change_create = %s, game_typeofchange = %s,
                       client_fromwhere = %s, client_name = %s, client_last_name = %s, client_phonenum = %s, client_user_id = %s, client_change_option = %s, client_launch_point = %s, client_changeddata_str = %s, client_changeddata_int = %s, client_game_id = %s, client_seats = %s, client_paymethod = %s, client_changedata_str = %s, client_changedata_int = %s,
                       activities_actwithchats = %s, activities_launch_point = %s, activities_chat_id = %s, activities_game_id = %s, activities_chat_language = %s,
                       finances_user_id = %s,  
                       level = %s WHERE user_id = %s""", 
                        (id, name,  last_name, language, action, direction,
                        game_launch_point, game_sport, game_date, game_time, game_seats, game_price, game_currency, game_latitude, game_longitude, game_nameaddress, game_change_direction, game_game_id, game_change_create, game_typeofchange,
                        client_fromwhere, client_name, client_last_name, client_phonenum, client_user_id, client_change_option, client_launch_point, client_changeddata_str, client_changeddata_int, client_game_id, client_seats, client_paymethod, client_changedata_str, client_changedata_int,
                        activities_actwithchats, activities_launch_point, activities_chat_id, activities_game_id, activities_chat_language,
                        finances_user_id,  
                        level, id))
        
def SelectDataFromSchedule(game_id: int) -> tuple[str, int, int, int, int, str, float, float, str]:
    row:Any = None
    sport:str = ''; date:int = -1; time:int = -1; seats:int = -1; price:int = -1; currency:str = ''; lat:float = -1; long:float = -1; address:str = ''
    with connection:
        cursor.execute("SELECT * FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            _game_id_, sport, date, time, seats, lat, long, address,  price, currency, _status_ = row
        else:
            assert(False)

        return sport, date, time, seats, price, currency, lat, long, address
    
def ChatsInfo(chatsinf: list[tuple[int, str]], aid: int):
    row:Any = None
    databasechats:list[int] = []
    outputchatinf:list[tuple[int, str]] = []
    inputchatinf:tuple[int, str] = (-1, '')
    chatid:int = -1
    chattitle:str = ''
    with connection:
        cursor.execute("SELECT Users.user_id, Admins.user_id FROM Users, Admins")
        row = cursor.fetchall
        if row is not None:
            databasechats = [item[0] for item in row]
            for inputchatinf, chatids in zip(chatsinf, databasechats):
                if inputchatinf[0] != chatids:
                    outputchatinf.append(inputchatinf)

            if outputchatinf != []:
                cursor.execute("UPDATE Admins SET newchats = %s WHERE user_id = %s", (True, aid,))
                for chatid, chattitle in outputchatinf:
                    cursor.execute("INSERT INTO Chats (chat_id, title) VALUES (%s, %s)", (chatid, chattitle,))

        else:
            assert(False)

def InfUpdate(user_id: int, name: str, lastname:str, username: str, language: str):
    row:Any = None
    message_id:int = -1
    custom_language:bool = False
    with connection:
        cursor.execute("SELECT custom_language, exmess FROM Admins WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        if row is not None:
            custom_language, message_id = row
            if custom_language:
                cursor.execute("UPDATE Admins SET user_id = %s, name = %s, last_name = %s, username = %sWHERE user_id = %s", (user_id, name, lastname, username, user_id))
            else:
                cursor.execute("UPDATE Admins SET user_id = %s, name = %s, last_name = %s, username = %s, language = %s WHERE user_id = %s", (user_id, name, lastname, username, language, user_id))
        else:
            assert(False)
        return message_id
    
def AddNewChat(chatid: int, chatname: str):
    with connection:
        cursor.execute("INSERT INTO Chats (chat_id, title) VALUES (%s, %s)", (chatid, chatname,))

def FindChats(chatid: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Chats WHERE chat_id = %s", (chatid,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result

def FindGameIds(game_id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE game_id = %s AND status != -1", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] > 0:
                result = True
        else:
            assert(False)
        return result

def RegistrtionClientToGame(game_id: int, id: int):
    row:Any = None
    seats:int = -1
    with connection:
        cursor.execute("SELECT seats FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            seats = row[0]
            cursor.execute("UPDATE Schedule SET seats = %s WHERE game_id = %s", (seats-1, game_id,))
            cursor.execute("INSERT INTO WatingForGamesUsers (user_id, game_id, seats, payment) VALUES (%s, %s, 1, 'cash')", (id, game_id,))
        else:
            assert(False)

def SelectChatLang(chatid: int) -> tuple[str, int]:
    row:Any = None
    lang:str = ''
    exmess:int = -1
    with connection:
        cursor.execute("SELECT language_of_message, message_id FROM Chats WHERE chat_id = %s", (chatid,))
        row = cursor.fetchone()
        if row is not None:
            lang, exmess = row
        else:
            assert(False)
        return lang, exmess
    
def UpdateExMessageIdDB(message_id: int, user_id: int):
    with connection:
        cursor.execute("UPDATE Admins SET exmess = %s WHERE user_id = %s", (message_id, user_id,))

def Reupdate(user_id: int):
    with connection:
        cursor.execute("UPDATE Admins SET direction = '', level = 0, game_launch_point = 0, client_launch_point = 0, activities_launch_point = 0 WHERE user_id = %s", (user_id,))

def ReupdateGames(user_id: int):
    with connection:
        cursor.execute("UPDATE Admins SET game_launch_point = 0, game_sport = '', game_date = -1, game_time = -1, game_seats = -1, game_price = -1, game_currency = -1, game_latitude = -1, game_longitude = -1, game_nameaddress = '' WHERE user_id = %s", (user_id,))

def ReupdateClients(user_id: int):
    with connection:
        cursor.execute("UPDATE Admins SET client_fromwhere = '', client_name = '', client_last_name = '', client_phonenum = -1, client_user_id = -1, client_change_option = '', client_changedata_str = '', client_changedata_int = -1, client_launch_point = 0, client_game_id = -1, client_seats = -1, client_paymethod = '' WHERE user_id = %s", (user_id,))

def ReupdateActivities(user_id: int):
    with connection:
        cursor.execute("UPDATE Admins SET activities_actwithchats = '', activities_launch_point = 0, activities_chat_id = -1, activities_game_id = -1, activities_chat_language = '' WHERE user_id = %s", (user_id,))

def ReupdateFinances(user_id: int):
    with connection:
        cursor.execute("UPDATE Admins SET finances_user_id = -1 WHERE user_id = %s", (user_id,))

def UpdateExMessageFromChatDB(message_id: int, chat_id: int):
    with connection:
        cursor.execute("UPDATE Chats SET message_id = %s WHERE chat_id = %s", (message_id, chat_id,))