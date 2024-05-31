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

def FindUserRecords(id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE user_id = %s AND (status != -1)", (id,))
        row = cursor.fetchone()
        if row is not None:
            counter = row[0]
        else:
            assert(False)
        if counter != 0:
            result = True
        print("result =", result)
        return result

def CreateTableForUser(id: int) -> list[tuple[int, str, str, int, int]]:
    row:Any = None
    with connection:
        cursor.execute("""SELECT WatingForGamesUsers.seats, WatingForGamesUsers.payment,
                            Schedule.sport, Schedule.date, Schedule.time
                        FROM WatingForGamesUsers
                        JOIN Schedule ON Schedule.game_id = WatingForGamesUsers.game_id
                        JOIN Users ON WatingForGamesUsers.user_id = Users.user_id
                        WHERE Users.user_id = %s
                            AND (WatingForGamesUsers.status IS NULL OR WatingForGamesUsers.status != -1)
                            AND (Schedule.status != -1 OR Schedule.status != -1);""", (id,))
        row = cursor.fetchall()
        return row

def SelAllUserGames(id: int, limit: int, launch_point: int) -> list[tuple[int, str, int, int]]:
    with connection:
        cursor.execute(f"""SELECT Schedule.game_id, sport, date, time FROM Schedule
                    JOIN WatingForGamesUsers ON WatingForGamesUsers.game_id = Schedule.game_id 
                    WHERE WatingForGamesUsers.user_id = %s AND 
                    (WatingForGamesUsers.status != -1 OR WatingForGamesUsers.status != -1)
                    ORDER BY Schedule.game_id DESC LIMIT {limit} OFFSET {launch_point}""", (id,))
        return [(a, b, c, d) for (a, b, c, d) in cursor.fetchall()]
    

def ChangeLanguage(lang: str, id: int):
    with connection:
        cursor.execute("UPDATE Users SET language = %s, custom_language = True WHERE user_id = %s", (lang, id,))
    
def TryToFFindGameid(game_id: int):
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row[0] != 0:
            result = True
        print("result = ", result, game_id)
        return result
    
def InfGameUser(id: int, gid: int) -> tuple[str, int, int, float, float, str, int, str, int, str, int]:

    sport:str = ''
    date:int = -1
    time:int = -1
    latitude:float = -1
    longitude:float = -1
    address:str = ''
    price:int = -1
    currency:str = ''
    seats:int = -1
    payment:str = ''
    payment_status:int = -1

    with connection:
        cursor.execute("""SELECT sport, date, time, latitude, longitude, address, price, currency, WatingForGamesUsers.seats, payment, status_payment
                       FROM Schedule, WatingForGamesUsers
                       WHERE Schedule.game_id = %s AND WatingForGamesUsers.game_id = %s AND WatingForGamesUsers.user_id = %s""", (gid, gid, id,))
        row:Any = cursor.fetchone()
        if row is not None:
            sport, date, time, latitude, longitude, address, price, currency, seats, payment, payment_status = row
        else:
            assert(False)
        return sport, date, time, latitude, longitude, address, price, currency, seats, payment, payment_status
    
def CountUserGames(id: int) -> int:
    with connection:
        counter:int = -1
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE (status != -1) AND user_id = %s", (id,))
        row:Any = cursor.fetchone()
        if row is not None:
            counter = row[0]
        else:
            assert(False)
        return counter
    
def DeleteUserGame(id: int, game_id: int):
    row:Any = None
    with connection:
        cursor.execute("SELECT seats FROM WatingForGamesUsers WHERE user_id = %s AND game_id = %s", (id, game_id,))
        row = cursor.fetchone()
        if row is not None:
            cursor.execute("UPDATE WatingForGamesUsers SET status = -1 WHERE user_id = %s AND game_id = %s", (id, game_id,))
            cursor.execute("UPDATE Schedule SET seats = (seats + %s) WHERE game_id = %s", (row[0], game_id,))
        else:
            assert(False)

def SelectPaymentStatus(id: int, game_id: int):
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT status_payment FROM WatingForGamesUsers WHERE user_id = %s AND game_id = %s", (id, game_id,))
        row = cursor.fetchone()
        if row[0] == 0:
            result = True
        return result

def SelectSeats(game_id: int, id: int) -> tuple[int, int]:
    with connection:
        us_seats:int = -1
        global_seats:int = -1
        cursor.execute("SELECT WatingForGamesUsers.seats, Schedule.seats FROM WatingForGamesUsers, Schedule WHERE WatingForGamesUsers.game_id = %s AND Schedule.game_id = %s AND user_id = %s", (game_id, game_id, id,))
        row:Any = cursor.fetchone()
        if row is not None:
            us_seats, global_seats = row
        else:
            assert(False)
        return us_seats, global_seats

def SelectSomeData(game_id: int, uid: int) -> tuple[int, int, int, str, int]:
    with connection:
        cursor.execute("""SELECT WatingForGamesUsers.seats, Schedule.seats, Schedule.price, Schedule.currency, WatingForGamesUsers.status_payment
                       FROM WatingForGamesUsers, Schedule
                       WHERE WatingForGamesUsers.user_id = %s AND WatingForGamesUsers.game_id = %s AND Schedule.game_id = %s""", (uid, game_id, game_id,))
        row:Any = cursor.fetchone()
        if row is not None:
            user_seats, global_seats, price, currency, payment_status = row
        else:
            assert(False)
        return user_seats, global_seats, price, currency, payment_status
    
def UpdateSeats(id: int, game_id: int, new_seats: int, new_seats_user: int):
    with connection:
        print(new_seats_user, new_seats, game_id, id)
        print(cursor.mogrify("UPDATE WatingForGamesUsers SET seats = %s WHERE user_id = %s AND game_id = %s", (new_seats_user, id, game_id,)))
        cursor.execute("UPDATE WatingForGamesUsers SET seats = %s WHERE user_id = %s AND game_id = %s", (new_seats_user, id, game_id,))
        cursor.execute("UPDATE Schedule SET seats = %s WHERE game_id = %s", (new_seats, game_id,))
        print("END")
    
def SelectPaymethod(game_id: int, id: int) -> int:
    with connection:
        cursor.execute("SELECT status_payment FROM WatingForGamesUsers WHERE user_id = %s AND game_id = %s", (id, game_id,))
        row:Any = cursor.fetchone()
        if row is not None:
            result = row[0]
        else:
            assert(False)
        return result

def ChangePaymethod(game_id: int, id: int, paymethod: str):
    with connection:
        cursor.execute("UPDATE WatingForGamesUsers SET payment = %s WHERE user_id = %s AND game_id = %s", (paymethod, id, game_id,))