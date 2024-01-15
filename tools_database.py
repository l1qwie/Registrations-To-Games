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

def ChangeSomeThing(table: str, column: str, value: Any, comparison: str, condition: Any):
    with connection:
        cursor.execute(f"UPDATE {table} SET {column} = {value} WHERE {comparison} = {condition}")


#All about Schedule
def CreateGameInSchedule(sport: str, date: int, time: int, seats: int, status: int, latitude: float, longitude: float, address: str, price: int, currency: str):
    row:Any = None
    game_id:int = -1
    with connection:
        cursor.execute("SELECT game_id FROM Schedule ORDER BY game_id DESC LIMIT 1")
        row = cursor.fetchone()
        if row is not None:
            game_id = row[0] + 1
        else:
            game_id = 1
        cursor.execute("""INSERT INTO Schedule 
                            (game_id, sport, date, time, seats, status, latitude, longitude, address, price, currency) 
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", (game_id, sport, date, time, seats, status, latitude, longitude, address, price, currency))
        return game_id

def SelectAllSchedule() -> list[tuple[int, str, int, int, int, str, float, float, str, int, str]]:
    row:Any = None
    schedule:list[tuple[int, str, int, int, int, str, float, float, str, int, str]] = []
    with connection:
        cursor.execute("SELECT * FROM Schedule")
        row = cursor.fetchall()
        if row is not None:
            schedule= row
        return schedule

def DeleteGameInSchedule(game_id: int):
    with connection:
        cursor.execute("""DELETE FROM MediaRepository
                        WHERE game_id = %s;
                       
                        DELETE FROM WatingForGamesUsers
                        WHERE game_id = %s;

                        DELETE FROM WaitingForNotification
                        WHERE game_id = %s;
                       
                        DELETE FROM Schedule
                        WHERE game_id = %s;""", (game_id, game_id, game_id, game_id,))
        
def ChangeColumnInScheduleTable(column: str, value: Any, game_id: int):
    with connection:
        cursor.execute(f"UPDATE Schdule SET {column} = {value} WHERE game_id = %s", (game_id,))

def DeleleAllGamesInSchedule():
    with connection:
        cursor.execute("DELETE FROM Schedule")


#Users
def SelectAllUsers() -> list[tuple[int, str, str, str, str, str, str, bool]]:
    row:Any = None
    users:list[tuple[int, str, str, str, str, str, str, bool]] = []
    with connection:
        cursor.execute("SELECT user_id, name, last_name, username, from_where, language, phone_number, user_admin FROM Users")
        row = cursor.fetchall()
        if row is not None:
            users = row
        return users
    
def ChangeColumnInUsersTable(column: str, value: str, user_id: int):
    with connection:
        cursor.execute(f"UPDATE Users SET {column} = {value} WHERE user_id = %s", (id,))

def CreateUser(name: str, last_name: str, phone: int, from_where: str) -> int:
    row:Any = None
    user_id :int = -1
    with connection:
        cursor.execute("SELECT nextval('adminuser_id')")
        row = cursor.fetchone()
        if row is not None:
            user_id = row[0]
            cursor.execute("INSERT INTO Users (user_id, name, last_name, phone_number, from_where, user_admin) VALUES (%s, %s, %s, %s, %s, True)", (user_id, name, last_name, phone, from_where,))
        return user_id
    
def DeleteUser(user_id: int):
    with connection:
        cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
    
def DeleteAllUsers():
    with connection:
        cursor.execute("DELETE FROM Users")

#RegForGames
def ShowAllRegistrtions() -> list[tuple[int, int, int, str, bool]]:
    row:Any = None
    schedule:list[tuple[int, int, int, str, bool]] = []
    with connection:
        cursor.execute("SELECT user_id, game_id, seats, payment, status_payment FROM WatingForGamesUsers WHERE status = 1")
        row = cursor.fetchone()
        if row is not None:
            schedule = row
        else:
            assert(False)
        return schedule


def RegistrationUserForGames(game_id: int, free_seats:int, seats: int, payment: str, id: int):
    with connection:
        cursor.execute("INSERT INTO WatingFOrGamesUsers (user_id, game_id, seats, payment, status, status_payment) VALUES (%s, %s, %s, %s, 1, 0)", (id, game_id, seats, payment,))
        cursor.execute("UPDATE Schedule SET seats = %s", (free_seats-seats,))

def SelectId() -> int:
    row:Any = None
    id:int = -1
    with connection:
        cursor.execute("SELECT user_id FROM Users WHERE user_admin = True AND status = 1")
        row = cursor.fetchone()
        if row is not None:
            id = row[0]
        else:
            assert(False)
        return id

def SelectSeats(game_id: int) -> int:
    row:Any = None
    free_seats: int = -1
    with connection:
        cursor.execute("SELECT seats FROM Schedule WHERE status != -1 AND seats != 0 AND game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            free_seats = row[0]
        else:
            assert(False)
        return free_seats

def UnRegistrationUserToGames(id: int, game_id: int):
    with connection:
        cursor.execute("UPDATE WatingForGamesUsers SET status = -1 WHERE user_id = %s AND game_id = %s", (id, game_id,))

def ChangeRegistrationUserToGames(column: str, value:str, user_id: int, game_id: int):
    with connection:
        cursor.execute(f"UPDATE WatingForGamesUsers SET {column} = {value} WHERE game_id = %s AND user_id = %s", (game_id, user_id))

#Media
def ShowAllGamesInMediaRepository() -> list[tuple[int, int, int, str, str, bool]]:
    row:Any = None
    schedule:list[tuple[int, int, int, str, str, bool]] = []
    with connection:
        cursor.execute("SELECT * FROM MediaRepository")
        row = cursor.fetchall()
        if row is not None:
            schedule = row
        else:
            assert(False)
        return schedule
    
def ShowAllMediaFromOneGames(game_id: int) -> list[tuple[int, int, int, str, str, bool]]:
    row:Any = None
    schedule:list[tuple[int, int, int, str, str, bool]] = []
    with connection:
        cursor.execute("SELECT * FROM MediaRepository WHERE game_id = %s", (game_id,))
        row = cursor.fetchall()
        if row is not None:
            schedule = row
        else:
            assert(False)
        return schedule
    
def AddANewFile(file_id: str, typeoffile: str, game_id: int):
    row:Any = None
    schedule:Any = None
    with connection:
        cursor.execute("SELECT COUNT(*) FROM MediaRepository WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            if 0 <= row[0] < 20:
                cursor.execute("INSERT INTO MediaRepository (game_id, user_id, file_id, typeoffile, status) VALUES (%s, 738070596, %s, %s, 1)", (game_id, file_id, typeoffile,))
                cursor.execute("UPDATE MediaRepository SET counter = %s WHERE game_id = %s", (row[0]+1, game_id,))
                cursor.execute("SELECT * FROM MediaRepository WHERE game_id = %s AND user_id = 738070596", (game_id,))
                schedule = cursor.fetchall()
                if schedule is not None:
                        print("File created")
                else:
                    assert(False)
            else:
                print("We don't have any free place for you")
        else:
            assert(False)

def RandomDeleteAFile(media_id: int):
    with connection:
        cursor.execute("UPDATE MediaRepository SET status = False WHERE id = %s", (media_id,))

def DeleteGameForMedia(game_id: int):
    with connection:
        cursor.execute("UPDATE Schedule SET status = -1 WHERE game_id = %s", (game_id,))

#Admins
def ResetAdmin(id: int):
    with connection:
        cursor.execute("""UPDATE Admins SET name = NULL, last_name = NULL, action = NULL, level = NULL WHERE user_id = %s""", (id,))
        
def ChangeAdminStr(id: int, column: str, value: str):
    with connection:
        cursor.execute(f"UPDATE Admins SET {column} = %s WHERE user_id = %s", (value, id,))

def ChangeAdminInt(id: int, column: str, value: int):
    with connection:
        cursor.execute(f"UPDATE Admins SET {column} = %s WHERE user_id = %s", (value, id,))



#Create Games
def ResetForCreateGame(id: int):
    with connection:
        cursor.execute("UPDATE Admins SET level = 0, direction = '', game_launch_point = 0, game_sport = '', game_date = -1, game_time = -1, game_seats = -1, game_price = -1, game_currency = '', game_latitude = -1, game_longitude = -1, game_nameaddress = '' WHERE user_id = %s", (id,))


#Chats
def DeleteAllChats():
    with connection:
        cursor.execute("DELETE FROM Chats")

def AddSomeChats(chatid: int, title: str):
    with connection:
        cursor.execute("INSERT INTO Chats (chat_id, title) VALUES (%s, %s)", (chatid, title,))
    
def DeleteChat(chat_id: int):
    with connection:
        cursor.execute("DELETE FROM Chats WHERE chat_id = %s", (chat_id,))

#Delete all wait games
def DeleteAllWaitGames():
    with connection:
        cursor.execute("DELETE FROM WatingForGamesUsers")

def DeleteWaitGame(game_id: int, user_id: int):
    with connection:
        cursor.execute("DELETE FROM WatingForGamesUsers WHERE game_id = %s AND user_id = %s", (game_id, user_id,))

def Paid(user_id: int, game_id: int):
    with connection:
        cursor.execute("UPDATE WatingForGamesUsers SET status_payment = 1 WHERE game_id = %s AND user_id = %s", (game_id, user_id,))

