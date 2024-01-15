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

def testDataFitting(act: str, lvl: int, id: int):
    with connection:
        cursor.execute("UPDATE Admins SET action = %s, level = %s WHERE user_id = %s", (act, lvl, id,))

def testSelectLevel(id: int):
    row:Any = None
    with connection:
        cursor.execute("SELECT level FROM Admins WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            row = row[0]
        else:
            assert(False)
        return row
    
def testSelectSomthingColumn(id: int, column_name: str) -> Any:
    row:Any = None
    with connection:
        cursor.execute(f"SELECT {column_name} FROM Admins WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            row = row[0]
        else:
            assert(False)
        return row
    
def SelectGameId() -> int:
    row:Any = None
    game_id: int = -1
    with connection:
        cursor.execute("SELECT nextval('game_id_schedule')")
        row = cursor.fetchone()
        if row is not None:
            game_id = row[0] - 1
    return game_id

def testChangeOrNo(chancolumn: str, value: Any, direction: bool, user_id: int, game_id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        if direction:
            cursor.execute(f"SELECT {chancolumn} FROM Admins WHERE {chancolumn} = %s AND user_id = %s", (value, user_id))
            row = cursor.fetchone()
            if row is not None:
                result = True
        else:
            cursor.execute(f"SELECT {chancolumn} FROM Schedule WHERE game_id = %s", (game_id,))
            row = cursor.fetchone()
            if row is not None:
                result = True
        return result
    
def SelectDate(game_id: int) -> int:
    row:Any = None
    date:int = -1
    with connection:
        cursor.execute("SELECT date FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            date = row[0]
        return date
    
def ChangeDir(user_id: int):
    with connection:
        cursor.execute("UPDATE Admins SET direction = '' WHERE user_id = %s", (user_id,))

def testSelectLatAndLong(game_id: int) -> tuple[float, float]:
    row:Any = None
    lat:float = -1
    long:float = -1
    with connection:
        cursor.execute("SELECT latitude, longitude FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            lat, long = row
        else:
            assert(False)
        return lat, long
    
def SelectGameStatus(game_id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT status FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] == -1:
                result = True

        return result

def InfUserChangeOrNoDataInt(data: int, id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT phone_number FROM Users WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            a = [data, row[0]]
            print(a)
            print(data == row[0])
            if data == row[0]:
                result = True
        else:
            assert(False)
    return result

def InfUserChangeOrNoDataStr(data: str, column: str, id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute(f"SELECT {column} FROM Users WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            if data == row[0]:
                result = True
        else:
            assert(False)
    return result

def SelectNewUserId() -> int:
    row:Any = None
    userid:int = -1
    with connection:
        cursor.execute("SELECT nextval('adminuser_id')")
        row = cursor.fetchone()
        if row is not None:
            userid = row[0] + 1
        else:
            assert(False)
    return userid

def DeleteClientOrNo(id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT status FROM Users WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] == -1:
                result = True
        
        return result
    
def RemovedFromGameOrNo(userid: int, gameid: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT status FROM WatingForGamesUsers WHERE game_id = %s AND user_id = %s", (gameid, userid,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] == -1:
                result = True
        else:
            assert(False)
        return result
    
def RegedOrNo(user_id: int, game_id: int, seats: int, paymethod: str) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE user_id = %s AND game_id = %s AND seats = %s AND payment = %s", (user_id, game_id, seats, paymethod,))
        row = cursor.fetchone()
        print(row, user_id, game_id, seats, paymethod,)
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        
        return result
    
def ChangePaidOrNo(user_id: int, game_id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT status_payment FROM WatingForGamesUsers WHERE user_id = %s AND game_id = %s", (user_id, game_id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] == 1:
                result = True
        else:
            assert(False)
        return result
    
def testChangeLanguageOrNo(user_id: int, lang: str) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Admins WHERE user_id = %s AND language = %s AND custom_language = True", (user_id, lang,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result
    
def SelectChatId() -> int:
    row:Any = None
    chat_id:int = -1
    with connection:
        cursor.execute("SELECT chat_id FROM Chats")
        row = cursor.fetchone()
        if row is not None:
            chat_id = row[0]
        else:
            assert(False)
        return chat_id
    
def testUpdatedChatOrNo(chat_id: int, chat_lang: str) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT language_of_message FROM Chats WHERE chat_id = %s", (chat_id,))
        row = cursor.fetchone()
        if row is not None:
            if chat_lang == row[0]:
                result = True
        else:
            assert(False)
        return result
    
def ResetAllLaunchPoints(user_id: int):
    with connection:
        cursor.execute("UPDATE Admins SET game_launch_point = 0, client_launch_point = 0, activities_launch_point = 0 WHERE user_id = %s", (user_id,))