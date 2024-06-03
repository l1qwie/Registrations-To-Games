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

def ScheduleOfGames(launch_point: int, limit: int) -> list[tuple[int, str, int, int]]:
    row:Any = None
    schedule:list[tuple[int, str, int, int]]
    with connection:
        cursor.execute(f"SELECT game_id, sport, date, time FROM Schedule WHERE status != -1 ORDER BY game_id DESC LIMIT {limit} OFFSET {launch_point}")
        row = cursor.fetchall()
        if row is not None:
            schedule = row
        else:
            assert(False)
        
        return schedule
    
def ScheduleOfGamesWithSeats(launch_point: int, limit: int) -> list[tuple[int, str, int, int, int]]:
    row:Any = None
    schedule:list[tuple[int, str, int, int, int]]
    with connection:
        cursor.execute(f"SELECT game_id, sport, date, time, seats FROM Schedule WHERE status != -1 ORDER BY game_id DESC LIMIT {limit} OFFSET {launch_point}")
        row = cursor.fetchall()
        if row is not None:
            schedule = row
        else:
            assert(False)
        
        return schedule


def LengthOfGames() -> int:
    row:Any = None
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE status != -1")
        row = cursor.fetchone()
        assert(row is not None)
        return row[0]
    
def NewScheduleGame(id: int):
    row:Any = None

    with connection:
        cursor.execute("SELECT game_sport, game_date, game_time, game_seats, game_latitude, game_longitude, game_nameaddress, game_price, game_currency FROM Admins WHERE user_id = %(id)s", ({"id": id}))
        row = cursor.fetchone()
        if None not in row:
            (sport, date, time, seats, lat, long, name, price, currency) = row
            cursor.execute("""INSERT INTO Schedule (game_id, sport, date, time, seats, latitude, longitude, address, price, currency, status) 
                       VALUES (nextval('game_id_schedule'), %s, %s, %s, %s, %s, %s, %s, %s, %s, 1)""", 
                       (sport, date, time, seats, lat, long, name, price, currency))
        else:
            assert(False)

def SelectGameId(id_str: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT game_id FROM Schedule")
        row = cursor.fetchall()
        if row != 0:
            row = [i[0] for i in row]
            if id_str in row:
                result = True

        return result 
    
def ChangeColumn(column: str, data: Any, data2: float, game_id: int):
    with connection:
        if data2 != -1:
            cursor.execute("UPDATE Schedule SET latitude = %s, longitude = %s WHERE game_id = %s", (data, data2, game_id,))
        else:
            cursor.execute(f"UPDATE Schedule SET {column} = %s WHERE game_id = %s", (data, game_id,))

def ChangeColumnInt(data: int, column: str, game_id: int):
    with connection:
        cursor.execute(f"UPDATE Schedule SET {column} = %s WHERE game_id = %s", (data, game_id,))

def ChangeColumnStr(data: str, column: str, game_id: int):
    with connection:
        cursor.execute(f"UPDATE Schedule SET {column} = %s WHERE game_id = %s", (data, game_id,))

def ChangeColumnsFloat(lat: float, long: float, game_id: int):
    with connection:
        cursor.execute("UPDATE Schedule SET latitude = %s, longitude = %s WHERE game_id = %s", (lat, long, game_id,))

def SelectDataChanged(game_id: int, direction_of_change: str, typeofchange: str) -> tuple[str, int, float, float]:
    row:Any = None
    res_str:str = ''
    res_int:int = -1
    res_lat:float = -1
    res_long:float = -1
    with connection:
        if direction_of_change != "link":
            cursor.execute(f"SELECT {direction_of_change} FROM Schedule WHERE game_id = %s", (game_id,))
            row = cursor.fetchone()
            if row is not None:
                print(typeofchange)
                if typeofchange == "str":
                    res_str = row[0]
                elif typeofchange == "int":
                    res_int = row[0]
                else:
                    assert(False)
            else:
                assert(False)
        else:
            cursor.execute("SELECT latitude, longitude FROM Schedule WHERE game_id = %s", (game_id,))
            row = cursor.fetchone()
            if row is not None:
                if typeofchange == "float":
                    res_lat, res_long = row
                else:
                    assert(False)
            else:
                assert(False)
        
        return res_str, res_int, res_lat, res_long
    
def GameRemove(game_id: int):
    with connection:
        cursor.execute("UPDATE Schedule SET status = -1 WHERE game_id = %s", (game_id,))