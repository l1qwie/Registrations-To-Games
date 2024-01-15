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

def HowMuthGamesChanged(id: int) -> list[int]:
    with connection:
        cursor.execute("SELECT game_id FROM WaitingForNotification WHERE user_id = %s AND setup <> 'DELETE'", (id,))
        game_ids = [row[0] for row in cursor.fetchall()]
        return game_ids
    
def HowKnowWhatChanged(gid: int) -> tuple[str, int, int, float, float, str]:
        
    row:Any = None
    sport:str = ''
    date:int = -1
    time:int = -1
    latitude:int = -1
    longitude:int = -1
    address:str = ''

    with connection:
        cursor.execute("""SELECT Schedule.sport, Schedule.date, Schedule.time, Schedule.latitude, Schedule.longitude, Schedule.address
                        FROM Schedule
                        WHERE Schedule.game_id = %(gid)s AND Schedule.status = 'changed'""", ({"gid": gid}))
        row = cursor.fetchone()
        if row is not None:
            sport, date, time, latitude, longitude, address = row
        return sport, date, time, latitude, longitude, address

def HowMuchIsLeft(id: int) -> int:
    row:Any = None
    howmutch:int = -1
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WaitingForNotification WHERE user_id = %s AND setup <> 'DELETE'", (id,))
        row = cursor.fetchone()
        if row is not None:
            howmutch = row[0]
        else:
            assert(False)
        return howmutch
    
    
def LeaveANote(id: int, gid: int):
    with connection:
        cursor.execute("UPDATE WatingForGamesUsers SET status = 'allright' WHERE user_id = %s AND game_id = %s", (id, gid))
        cursor.execute("UPDATE WaitingForNotification SET status = 'notified', setup = 'DELETE', user_answer = 'with us' WHERE user_id = %s AND game_id = %s", (id, gid))

def DelMyRec(id: int, gid: int):

    row:Any = None
    userseats:int = -1
    freeseats:int = -1

    with connection:
        cursor.execute("SELECT seats FROM WatingForGamesUsers WHERE user_id = %s AND game_id = %s AND status <> 'DELETE'", (id, gid,))
        row = cursor.fetchone()
        if row is not None:
            userseats = row[0]
        else:
            assert(False)
        cursor.execute("UPDATE WatingForGamesUsers SET status = 'DELETE' WHERE user_id = %s AND game_id = %s", (id, gid,))
        cursor.execute("UPDATE WaitingForNotification SET status = 'notified', setup = 'DELETE', user_answer = 'not with us' WHERE user_id = %s AND game_id = %s", (id, gid))
        
        cursor.execute("SELECT seats FROM Schedule WHERE game_id = %s", (gid,))
        row = cursor.fetchone()
        if row is not None:
            freeseats = row[0]
        else:
            assert(False)
        cursor.execute("UPDATE Schedule SET seats = %(newseats)s WHERE game_id = %(gid)s", ({"newseats": userseats+freeseats, "gid": gid}))

def CheckUsersWhoNeedNotif(gid: int):
    row:Any = None
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WaitingForNotification WHERE game_id = %s AND setup <> 'DELETE'", (gid,))
        row = cursor.fetchone()
        if row[0] == 0:
            cursor.execute("UPDATE Schedule SET status = 'get ready' WHERE game_id = %s", (gid,))