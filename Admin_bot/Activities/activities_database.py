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


def FindChats(limit: int, launch_point: int) -> list[tuple[int, str]]:
    row:Any = None
    chatinf:list[tuple[int, str]] = []
    with connection:
        cursor.execute(f"SELECT chat_id, title FROM Chats ORDER BY id DESC LIMIT {limit} OFFSET {launch_point}")
        row = cursor.fetchall()
        if row is not None:
            chatinf = row
        return chatinf
    
def SelectLengthChats() -> int:
    row:Any = None
    length:int = -1
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Chats")
        row = cursor.fetchone()
        if row is not None:
            length = row[0]
        else:
            assert(False)

        return length
    
def SelectAllInfFromSchedule(game_id: int) -> tuple[str, int, int, int, int, str, float, float, str]:

    row: Any = None
    sport:str = ''
    date:int = -1
    time:int = -1
    seatsforschedule:int = -1
    seatsfromwating:int = -1
    seats:int = -1
    price: int = -1
    currency:str = ''
    lat:float = -1
    long:float = -1
    nameaddress:str = ''

    with connection:
        cursor.execute("SELECT sport, date, time, seats, price, currency, latitude, longitude, address FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            sport, date, time, seatsforschedule, price, currency, lat, long, nameaddress = row
            cursor.execute("SELECT SUM(seats) FROM WatingForGamesUsers WHERE game_id = %s AND status != -1", (game_id,))
            row = cursor.fetchone()
            if row is not None:
                seatsfromwating = row[0]
                if not seatsfromwating:
                    seatsfromwating = 0
                seats = seatsforschedule + seatsfromwating
            else:
                assert(False)
        else:
            assert(False)

        return (sport, date, time, seats, price, currency, lat, long, nameaddress)
    
def FoundChatId(chatId: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Chats WHERE chat_id = %s", (chatId,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result

def FoundGameId(game_id: int) -> bool:
    row:Any= None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result
    
def SelectActiveGames(limit: int, launch_point: int) -> list[tuple[int, str, int, int, int]]:
    row:Any = None
    schedule:list[tuple[int, str, int, int, int]] = []
    with connection:
        cursor.execute(f"""SELECT WatingForGamesUsers.game_id, SUM(WatingForGamesUsers.seats) AS total_seats, Schedule.sport, Schedule.date, Schedule.time
                        FROM WatingForGamesUsers
                        JOIN Schedule ON WatingForGamesUsers.game_id = Schedule.game_id
                        WHERE WatingForGamesUsers.status != -1
                        GROUP BY WatingForGamesUsers.game_id, Schedule.sport, Schedule.date, Schedule.time
                        ORDER BY WatingForGamesUsers.game_id DESC
                        LIMIT {limit} OFFSET {launch_point}""")
        row = cursor.fetchall()
        if row is not None:
            schedule = [(game_id, sport, date, time, total_seats) for game_id, total_seats, sport, date, time in row]
        return schedule
    
def SelectLengthOfActiveGames() -> int:
    row:Any = None
    length:int = -1
    with connection:
        cursor.execute("SELECT DISTINCT(game_id) FROM WatingForGamesUsers WHERE status != -1")
        row = cursor.fetchall()
        if row is not None:
            length = len(row)
        else:
            assert(False)
        return length
    
def SelectInfClient(user_id: int) -> tuple[str, str, str, str, str, str]:
    row:Any = None
    name:str = ''
    lastname:str = ''
    nickname:str = ''
    phone:int = -1
    fromwhere:str = ''
    language:str = ''

    with connection:
        cursor.execute("""
                        SELECT COALESCE (name, 'no_data') AS name,
                        COALESCE (last_name, 'no_data') AS last_name, 
                        COALESCE (username, 'no_data') as username,
                        COALESCE (phone_number, -1),
                        COALESCE (from_where, 'no_data'), 
                        COALESCE (language, 'no_data') 
                        FROM Users WHERE user_id = %s
                        """, (user_id,))
        row = cursor.fetchone()
        if row is not None:
            name, lastname, nickname, phone, fromwhere, language = row
        else:
            assert(False)

        return name, lastname, nickname, str(phone), fromwhere, language
    
def SelectActiveGameId(game_id: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        print("JUST CHECK",row)
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result

def SelectWaitingClients(user_id: int) -> bool:
    row:Any= None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WatingForGamesUsers WHERE user_id = %s", (user_id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result
    
def RemoveClientFormGame(user_id: int, game_id: int):
    with connection:
        cursor.execute("UPDATE WatingForGamesUsers SET status = -1 WHERE game_id = %s AND user_id = %s", (game_id, user_id,))

def UpdateInfAboutChat(chat_id: int, chat_lang: str):
    with connection:
        cursor.execute("UPDATE Chats SET language_of_message = %s WHERE chat_id = %s", (chat_lang, chat_id,))

def SelectYourClients(game_id: int) -> list[tuple[str, str]]:
    row:Any = None
    users:list[tuple[str, str]] = []
    with connection:
        cursor.execute("""SELECT 
                       COALESCE (name, 'no_data') AS name, 
                       COALESCE (last_name, 'no_data') AS last_name
                       FROM Users
                       JOIN WatingForGamesUsers ON WatingForGamesUsers.game_id = %s""", (game_id,))
        row = cursor.fetchall()
        if row is not None:
            users = row
        else:
            assert(False)
        return users
    
def FindSomeGames() -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE status != -1")
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result