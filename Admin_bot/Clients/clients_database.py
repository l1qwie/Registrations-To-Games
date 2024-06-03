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


def SelectClient(limit: int, launch_point: int) -> list[tuple[int, str, str]]:
    row:Any = None
    names: list[tuple[int, str, str]] = []
    with connection:
        cursor.execute(f"""SELECT 
                        user_id,
                        COALESCE (name, 'no_data') AS name,
                        COALESCE (last_name, 'no_data') AS last_name
                        FROM 
                        Users
                        WHERE status != -1
                        ORDER BY 
                        name, last_name DESC 
                        LIMIT {limit} 
                        OFFSET {launch_point}""")
        row = cursor.fetchall()
        if row is not None:
            names = row
    return names


def SaveNewClient(id: int):
    row:Any = None
    with connection:
        cursor.execute("SELECT client_fromwhere, client_name, client_last_name, client_phonenum FROM Admins WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            fromwhere, name, lastname, phonenum = row
            cursor.execute("INSERT INTO Users (user_id, from_where, name, last_name, phone_number, user_admin) VALUES (nextval('adminuser_id'), %s, %s, %s, %s, True)", (fromwhere, name, lastname, phonenum,))
        else:
            assert(False)
        
def SelectAllOfUserId(user_id: int) -> bool:
    row:Any
    result:bool = False
    with connection:
        cursor.execute("SELECT user_id FROM Users WHERE status != -1")
        row = cursor.fetchall()
        if row is not None:
            row = [item[0] for item in row]
            if user_id in row:
                result = True
        else:
            assert(False)
        
        return result
    
def SelectAllInf(id: int) -> tuple[str, str, int, str, str]:
    row:Any = None
    name:str = ''
    last_name:str = ''
    phonenum:int = -1
    language:str = ''
    fromwhere:str = ''

    with connection:
        cursor.execute("""SELECT COALESCE (name, 'no_data') AS name,
                            COALESCE (last_name, 'no_data') AS last_name,
                        COALESCE (from_where, 'no_data') AS last_name,
                        COALESCE (language, 'no_data') AS last_name,
                        COALESCE(CAST(phone_number AS text), 'no_data') AS last_name
                        FROM Users WHERE user_id = %s and status != -1""", (id,))
        row = cursor.fetchone()
        if row is not None:
            name, last_name, fromwhere, language, phonenum = row
            print(name, last_name, fromwhere, language, phonenum)
        else:
            assert(False)
        return name, last_name, phonenum, fromwhere, language
    
def ChangeColumnUserInt(id: int, data: int):
    with connection:
        cursor.execute("UPDATE Users SET phone_number = %s WHERE user_id = %s", (data, id,))

def ChangeColumnUserStr(id: int, column: str, data: str):
    with connection:
        cursor.execute(f"UPDATE Users SET {column} = %s WHERE user_id = %s", (data, id,))

def RemoveClient(id: int):
    with connection:
        cursor.execute("UPDATE Users SET status = -1 WHERE user_id = %s", (id,))

def SelectLengthOfClients(game_id: int) -> int:
    row:Any = None
    length:int = -1
    with connection:
        cursor.execute("SELECT COUNT(user_id) FROM WatingForGamesUsers WHERE game_id = %s and status != -1", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            length = row[0]
        else:
            assert(False)
        return length

def SelectCountClient() -> int:
    row:Any = None
    length:int = -1
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Users WHERE status != -1")
        row = cursor.fetchone()
        if row is not None:
            length = row[0]
        
        return length
    
def SelectPriceAndCurrency(game_id: int) -> tuple[int, str]:
    row:Any = None
    price:int = -1
    currency:str = ''
    with connection:
        cursor.execute("SELECT price, currency FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            price, currency = row
        else:
            assert(False)
        return price, currency
    
def FreeSeats(seats: int, game_id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT seats FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            if (row[0] - seats) > 0:
                result = True
        else:
            assert(False)
        return result

def RegClient(user_id: int, game_id: int, seats: int, paymthod: str):
    row:Any = None
    with connection:
        cursor.execute("SELECT seats FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            cursor.execute("UPDATE Schedule SET seats = %s WHERE game_id = %s", (row[0]-seats, game_id,))
            cursor.execute("INSERT INTO WatingForGamesUsers (user_id, game_id, seats, payment) VALUES (%s, %s, %s, %s)", (user_id, game_id, seats, paymthod,))
        else:
            assert(False)