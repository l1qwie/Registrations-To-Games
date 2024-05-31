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




def SelectAllScheduleData(limit: int, launch_point: int) -> list[tuple[int, str, int, int, int]]:
    row:Any = None
    with connection:
        cursor.execute(f"SELECT game_id, sport, date, time, seats FROM Schedule WHERE (status != -1) ORDER BY Schedule DESC LIMIT {limit} OFFSET {launch_point}")
        row = cursor.fetchall()
        print(row)
        return row

def SelectAllGId(game_id: str) -> list[bool]:
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE status != -1 AND game_id = %s", (game_id,))
        row = cursor.fetchone()
        assert(row[0] is not None)
        return row[0]

def WhatAboutMoney(game_id: int) -> tuple[int, str]:
    row:Any = None
    price:int = -1
    currency:str = ''
    with connection:
        cursor.execute("SELECT price, currency FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        print(row)
        if row is not None:
            price, currency = row
        else:
            assert(False)
        return price, currency

def SelectSport(gid: int) -> str:
    with connection:
        cursor.execute("SELECT sport FROM Schedule WHERE game_id = %s", (gid,))
        sport:Any = cursor.fetchone()
        assert(sport[0] is not None)
        return sport[0]

def SelectDate(game_id: int) -> int:
    with connection:
        cursor.execute("SELECT date FROM Schedule WHERE game_id = %s", (game_id,))
        date:Any = cursor.fetchone()
        assert(date[0] is not None)
        return date[0]
    
def SelectTime(game_id: int) -> int:
    with connection:
        cursor.execute("SELECT time FROM Schedule WHERE game_id = %s", (game_id,))
        time:Any = cursor.fetchone()
        assert(time[0] is not None)
        return time[0]

def SelectAdressGame(game_id: int) -> list[float]:
    with connection:
        cursor.execute("""SELECT latitude, longitude 
                       FROM Schedule
                       WHERE game_id = %s""", (game_id,))
        address:list[float] = []
        row:Any = cursor.fetchone()
        if row is not None:
            address = row
        else:
            assert(False)
        return address
    
def HowMutchSeats(id: int) -> int:
    seats:Any = None
    with connection:
        cursor.execute("""SELECT seats
                            FROM Schedule
                            JOIN Users ON Users.game_id_reg_to_game = Schedule.game_id
                            WHERE Users.user_id = %s AND Schedule.status != -1""", (id,))
        seats = cursor.fetchone()
        assert(seats[0] is not None)
        return seats[0]
    
def ComNewRegGameUser(id: int):
    with connection:
        gid:int = -1
        seat:int = -1
        pay: str = ''
        cursor.execute("""SELECT game_id_reg_to_game, seats_reg_to_game, payment_reg_to_game
                        FROM Users
                        WHERE user_id = %s""", (id,))
        row:Any = cursor.fetchone()
        if row:
            gid, seat, pay = row
        cursor.execute("INSERT INTO WatingForGamesUsers (user_id, game_id, seats, payment) VALUES (%s, %s, %s, %s)", (id, gid, seat, pay,))

def BalanceOfTheUniverse(seat: int, id: int):
    with connection:
        cursor.execute("""
            UPDATE Schedule
            SET seats = %(st)s
            WHERE EXISTS (
                SELECT 1
                FROM Users
                WHERE Users.game_id_reg_to_game = Schedule.game_id
                AND Users.user_id = %(id)s
            )
        """, {"st": seat, "id": id})


    