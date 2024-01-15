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


def SelectCountClient() -> int:
    row:Any = None
    length:int = -1
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE status_payment = 0 AND status != -1")
        row = cursor.fetchone()
        if row is not None:
            length = row[0]
        else:
            assert(False)
        return length
    
def SelectClient(limit: int, launch_point: int) -> list[tuple[int, str, str]]:
    row:Any = None
    names: list[tuple[int, str, str]] = []
    with connection:
        cursor.execute(f"""
                        SELECT Users.user_id,
                        COALESCE (name, 'no_data') AS name,
                        COALESCE (last_name, 'no_data') AS last_name
                        FROM Users
                        JOIN WatingForGamesUsers ON Users.user_id = WatingForGamesUsers.user_id
                        WHERE WatingForGamesUsers.status != -1 AND Users.status != -1
                        ORDER BY 
                        name, last_name DESC 
                        LIMIT {limit} 
                        OFFSET {launch_point}""")
        row = cursor.fetchall()
        if row is not None:
            names = row
    return names

def SelectClientNickname(user_id: int) -> str:
    row:Any = None
    nickname: str = ''
    with connection:
        cursor.execute("SELECT COALESCE (name, 'no_data') FROM Users WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        if row is not None:
            nickname = row[0]
        else:
            assert(False)
        return nickname
    
def SelectCountHowManyGame(user_id: int) -> list[int]:
    row:Any = None
    game_ids:list[int] = []
    with connection:
        cursor.execute("SELECT DISTINCT(game_id) FROM WatingForGamesUsers WHERE user_id = %s AND status_payment = 0 AND status != -1", (user_id,))
        row = cursor.fetchall()
        if row is not None:
            game_ids = [item[0] for item in row]
        else:
            assert(False)
        return game_ids
    
def SelectInfAboutClientGame(game_id: int, user_id: int) -> tuple[str, int, int, int, str, int, str]:
    row:Any = None
    sport:str = ''
    date:int = -1
    time:int = -1
    price:int = -1
    currency:str = ''
    cl_seats:int = -1
    payment:str = ''
    with connection:
        cursor.execute("SELECT sport, date, time, price, currency FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            sport, date, time, price, currency = row
            cursor.execute("SELECT seats, payment FROM WatingForGamesUsers WHERE user_id = %s AND game_id = %s", (user_id, game_id,))
            row = cursor.fetchone()
            if row is not None:
                cl_seats, payment = row
            else:
                assert(False)
        else:
            assert(False)
        return (sport, date, time, price, currency, cl_seats, payment)
    
def CountClientGames(user_id: int) -> int:
    row:Any = None
    number:int = -1
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        if row is not None:
            number = row[0]
        else:
            assert(False)
        return number
    
def ScheduleOfGames(user_id: int, limit: int, launch_point: int) -> list[tuple[int, str, int, int]]:
    row:Any = None
    schedule:list[tuple[int, str, int, int]]
    with connection:
        cursor.execute(f"SELECT Schedule.game_id, sport, date, time FROM Schedule JOIN WatingForGamesUsers ON WatingForGamesUsers.user_id = %s WHERE Schedule.status != -1 ORDER BY game_id DESC LIMIT {limit} OFFSET {launch_point}", (user_id,))
        row = cursor.fetchall()
        if row is not None:
            schedule = row
        else:
            assert(False)
        
        return schedule
    
def SelecTWaitingClients(user_id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE user_id = %s AND status != -1 AND status_payment != 1", (user_id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result
    
def SelectClientBeforeGameId(user_id: int) -> int:
    row:Any = None
    game_id:int = -1
    with connection:
        cursor.execute("SELECT game_id FROM WatingForGamesUsers WHERE user_id = %s AND status_payment = 0 AND status != -1", (user_id,))
        row = cursor.fetchone()
        if row is not None:
            game_id = row[0]
        else:
            assert(False) 
        return game_id 
    
def SelectClientAfterGameId(user_id: int) -> int:
    row:Any = None
    game_id:int = -1
    with connection:
        cursor.execute("SELECT game_id FROM WatingForGamesUsers WHERE user_id = %s AND status_payment = 1 AND status != -1", (user_id,))
        row = cursor.fetchone()
        if row is not None:
            game_id = row[0]
        else:
            assert(False) 
        return game_id 

def Paid(user_id: int, game_id: int):
    with connection:
        cursor.execute("UPDATE WatingForGamesUsers SET status_payment = 1 WHERE game_id = %s AND user_id = %s", (game_id, user_id,))

def SelectWaitGameId(game_id: int, user_id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE game_id = %s AND user_id = %s AND status != -1 AND status_payment != 1", (game_id, user_id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result
    

def MoneyInf() -> list[tuple[str, int, int, int]]:
    row:Any = None
    inf:list[tuple[str, int, int, int]] = []
    with connection:
        cursor.execute("""SELECT s.currency,
                        SUM(s.price * wfgu.seats) AS expected_payment,
                        SUM(CASE WHEN wfgu.status_payment = 1 THEN s.price * wfgu.seats ELSE 0 END) AS paid_payment,
                        SUM(CASE WHEN wfgu.status_payment = 0 THEN s.price * wfgu.seats ELSE 0 END) AS unpaid_payment
                    FROM
                        Schedule s
                    JOIN
                        WatingForGamesUsers wfgu ON s.game_id = wfgu.game_id
                    GROUP BY
                        wfgu.game_id, s.currency""")
        row = cursor.fetchall()
        if row is not None:
            inf = row
        return inf