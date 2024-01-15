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
        cursor.execute("UPDATE Users SET action = %s, level = %s WHERE user_id = %s", (act, lvl, id,))

def UpdateLanguage(user_id: int):
    with connection:
        cursor.execute("UPDATE Users SET language = 'ru' WHERE user_id = %s", (user_id,))

def testSelectLevel(id: int):
    row:Any = None
    with connection:
        cursor.execute("SELECT level FROM Users WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            row = row[0]
        else:
            assert(False)
        return row
    
def testSelectSomthingColumn(id: int, column_name: str) -> Any:
    row:Any = None
    with connection:
        cursor.execute(f"SELECT {column_name} FROM Users WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            row = row[0]
        else:
            assert(False)
        return row

def testSelecInfAboutFile(id: int) -> tuple[int, str, str]:
    row:Any = None
    mgid:int = -1
    file_id:str = ''
    files:list[tuple[int, str, str]] = []
    typeoffile:str = ''
    i:int = 1
    with connection:

        while i <= 10:
            cursor.execute(f"SELECT id_mediagroup, file_id{i}, typeoffile{i} FROM Users WHERE file_id{i} IS NOT NULL AND user_id = %s", (id,))
            row = cursor.fetchone()
            if row is not None:
                mgid, file_id, typeoffile = row
                files.append((mgid, file_id, typeoffile))
            i += 1

        assert(files is not None)
        return files[-1]


def testCheckDelGames(id: int, game_id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE user_id = %s AND game_id = %s AND status = -1", (id, game_id,))
        row = cursor.fetchone()
        if row[0] is not None:
            result = True
            cursor.execute("UPDATE WatingForGamesUsers SET status = 1 WHERE user_id = %s AND game_id = %s AND status = -1", (id, game_id,))
        return result
    
def testChangeSeatsOrWhat(id: int, game_id: int, new_global_seats: int, new_user_seats: int) -> bool:
    row:Any = None
    result:bool = False
    global_seats:int = -1
    user_seats:int = -1
    with connection:
        cursor.execute("SELECT WatingForGamesUsers.seats, Schedule.seats FROM WatingForGamesUsers, Schedule WHERE WatingForGamesUsers.user_id = %s AND WatingForGamesUsers.game_id = %s AND Schedule.game_id = %s", (id, game_id, game_id,))
        row = cursor.fetchone()
        if row is not None:
            global_seats, user_seats = row
            if user_seats == new_user_seats and global_seats == new_global_seats:
                result = True
        return result
    
def testChangedPaymentOrWhat(id: int, game_id: int, payment: str) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE game_id = %s AND user_id = %s AND payment = %s", (game_id, id, payment,))
        row = cursor.fetchone()
        if row is not None:
            result = True
        return result
    
def testSelectSomeData(game_id: int, id: int) -> tuple[int, int]:
    row:Any = None
    global_seats:int = -1
    user_seats:int = -1
    with connection:
        cursor.execute("SELECT Schedule.seats, WatingForGamesUsers.seats FROM Schedule, WatingForGamesUsers WHERE Schedule.game_id = WatingForGamesUsers.game_id AND Schedule.game_id = %s AND user_id = %s", (game_id, id,))
        row = cursor.fetchone()
        if row is not None:
            global_seats, user_seats = row
        else:
            assert(False)
        return global_seats, user_seats
    
def testSelectCounterFiles(game_id: int) -> int:
    row:Any = None
    counter:int = -1
    with connection:
        cursor.execute("SELECT counter FROM MediaRepository WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            counter = row[0]
        else:
            assert(False)

        return counter
    
def testSelectCounterFromMedia(game_id: int) -> int:
    row:Any = None
    counter:int = -1
    with connection:
        cursor.execute("SELECT counter FROM MediaRepository WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            counter = row[0]
        else:
            assert(False)
        return counter

def testSelectSeatsFromGame(game_id: int) -> int:
    row:Any = None
    seats:int = -1
    with connection:
        cursor.execute("SELECT seats FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            seats = row[0]
        else:
            assert(False)
        return seats

def testSelectSeatsFromWaitingUsers(id: int, game_id: int) -> int:
    row:Any = None
    seats:int = -1
    with connection:
        cursor.execute("SELECT seats FROM WatingForGamesUsers WHERE game_id = %s AND user_id = %s", (game_id, id,))
        row = cursor.fetchone()
        if row is not None:
            seats = row[0]
        else:
            assert(False)
        return seats

def testResetUser(user_id: int):
    with connection:
        cursor.execute("UPDATE Users SET name = '', last_name = '', username = '', action = '', exmess = -1, level = 0 WHERE user_id = %s", (user_id,))