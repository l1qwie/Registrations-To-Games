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

def FindSomeGames() -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE status = -1")
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result


def FindSomeMedia() -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM MediaRepository")
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result
    
def FoundSomeverInSchedule() -> bool:
    media_inf:list[int] = []
    game_ids:list[int] = []
    final:list[int] = []
    result:bool = False
    row:Any = None
    with connection:
        cursor.execute("SELECT Schedule.game_id FROM Schedule JOIN MediaRepository ON (Schedule.game_id = MediaRepository.game_id) AND (MediaRepository.counter = 20)")
        row = cursor.fetchall()
        if row != (None,):
            game_ids = [item[0] for item in row]
        cursor.execute("SELECT game_id FROM Schedule WHERE status = -1")
        row = cursor.fetchall()
        if row != (None,):
            media_inf = [item[0] for item in row]
            for element in media_inf:
                if element not in game_ids:
                    final.append(element)
            if final != []:
                result = True
        else:
            assert(False)
        return result
    
def FoundSomeverInLastGamesSchedule() -> bool:
    row:Any = None
    game_ids:list[int] = []
    media_inf:list[int] = []
    final:list[int] = []
    result:bool = False
    with connection:
        cursor.execute("SELECT Schedule.game_id FROM Schedule JOIN MediaRepository ON (Schedule.game_id = MediaRepository.game_id) AND (MediaRepository.counter = 20)")
        row = cursor.fetchone()
        if row is not None:
            game_ids = [item[0] for item in row]

        cursor.execute("""SELECT game_id, sport, date, time 
                    FROM Schedule
                    WHERE status = -1 
                        AND 
                    date >= CAST(TO_CHAR(CURRENT_DATE - INTERVAL '7 days', 'YYYYMMDD') AS int)
                        AND 
                    date <= CAST(TO_CHAR(CURRENT_DATE, 'YYYYMMDD') AS int)""")
        row = cursor.fetchall()
        if row != (None,):
            media_inf = [item[0] for item in row]
            for element in media_inf:
                if element not in game_ids:
                    final.append(element)
            if final != []:
                result = True
        else:
            assert(False)
        return result

def FoundSomePhotosInLastGamesSchedule() -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("""SELECT COUNT(*) FROM MediaRepository JOIN Schedule ON (MediaRepository.game_id = Schedule.game_id) AND
                        Schedule.date >= CAST(TO_CHAR(CURRENT_DATE - INTERVAL '7 days', 'YYYYMMDD') AS int)
                        AND 
                        Schedule.date <= CAST(TO_CHAR(CURRENT_DATE, 'YYYYMMDD') AS int)
                        WHERE MediaRepository.status = 1""")
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        return result
    
def FoundSomePhotosInSchedule() -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM MediaRepository WHERE status = 1")
        row = cursor.fetchone()
        if row is not None:
            result = True
        return result
    
def CountAllOfGamesForView() -> int:
    row:Any = None
    length:int = -1
    with connection:
        cursor.execute("SELECT COUNT(*) FROM MediaRepository WHERE status = 1")
        row = cursor.fetchone()
        if row is not None:
            length = row[0]
        else:
            assert(False)
        return length

def CountAllOfGamesForLoad() -> int:
    row:Any = None
    length:int = -1
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Schedule WHERE status = -1")
        row = cursor.fetchone()
        if row is not None:
            length = row[0]
        else:
            assert(False)
        print("length =", length)
        return length

def CreateListOfLoadGames(limit: int, launch_point: int) -> tuple[list[tuple[int, str, int, int]], int]:
    row:Any = None
    media_inf:list[tuple[int, str, int, int]] = []
    game_ids:list[int] = []
    pred_final:list[tuple[int, str, int, int]] = []
    final:list[tuple[int, str, int, int]] = []
    length:int = -1
    counter:int = -1
    i:int = -1
    with connection:
        cursor.execute("SELECT Schedule.game_id FROM Schedule JOIN MediaRepository ON (Schedule.game_id = MediaRepository.game_id) AND (MediaRepository.counter = 20)")
        row = cursor.fetchall()
        if row != (None,):
            game_ids = [item[0] for item in row]
        cursor.execute(f"SELECT game_id, sport, date, time FROM Schedule WHERE status = -1")
        row = cursor.fetchall()
        if row != (None,):
            media_inf = row
            for element in media_inf:
                if element[0] not in game_ids:
                    pred_final.append(element)

            length = len(pred_final)
            counter = len(pred_final) - launch_point
            i = 0
            while i < limit and counter != 0:
                final.append(pred_final[counter-1])
                i += 1
                counter += -1

        else:
            assert(False)
        return final, length

def CreateListOfLoadGamesForLastGames(limit: int, launch_point: int) -> tuple[list[tuple[int, str, int, int]], int]:
    row:Any = None
    game_ids:list[int] = []
    media_inf:list[tuple[int, str, int, int]] = []
    pred_final:list[tuple[int, str, int, int]] = []
    final:list[tuple[int, str, int, int]] = []
    length:int = -1
    counter:int = -1
    with connection:
        cursor.execute("SELECT Schedule.game_id FROM Schedule JOIN MediaRepository ON (Schedule.game_id = MediaRepository.game_id) AND (MediaRepository.counter = 20)")
        row = cursor.fetchone()
        if row is not None:
            game_ids = [item[0] for item in row]

        cursor.execute(f"""SELECT game_id, sport, date, time 
                    FROM Schedule
                    WHERE status = -1 
                        AND 
                    date >= CAST(TO_CHAR(CURRENT_DATE - INTERVAL '7 days', 'YYYYMMDD') AS int)
                        AND 
                    date <= CAST(TO_CHAR(CURRENT_DATE, 'YYYYMMDD') AS int)""")
        row = cursor.fetchall()
        if row != (None,):
            media_inf = row
            for element in media_inf:
                if element[0] not in game_ids:
                    pred_final.append(element)

            length = len(pred_final)
            counter = len(pred_final) - launch_point
            i = 0
            while i < limit and counter != 0:
                print("counter =", counter)
                print(pred_final)
                final.append(pred_final[counter-1])
                i += 1
                counter += -1
        else:
            assert(False)
        return final, length

def CreateListOfViewGames(limit: int, launch_point: int) -> tuple[list[tuple[int, str, int, int]], int]:
    row:Any = None
    media_inf:list[tuple[int, str, int, int]] = []
    final:list[tuple[int, str, int, int]] = []
    length:int = -1
    counter:int = -1
    i:int = -1
    with connection:
        cursor.execute(f"""SELECT DISTINCT(Schedule.game_id), sport, date, time 
                       FROM Schedule
                       JOIN MediaRepository ON Schedule.game_id = MediaRepository.game_id AND MediaRepository.status = 1""")
        row = cursor.fetchall()
        if row != (None,):
            media_inf = row
            i = 0
            counter = len(media_inf) - launch_point
            while i < limit and counter != 0:
                final.append(media_inf[counter-1])
                i += 1
                counter += -1
        else:
            assert(False)
        return final, length

def CreateListOfViewGamesForLastGames(limit: int, launch_point: int) -> tuple[list[tuple[int, str, int, int]], int]:
    row:Any = None
    media_inf:list[tuple[int, str, int, int]] = []
    final:list[tuple[int, str, int, int]] = []
    length:int = -1
    counter:int = -1
    i:int = -1
    with connection:
        cursor.execute(f"""SELECT DISTINCT(Schedule.game_id), sport, date, time 
                        FROM Schedule 
                        JOIN MediaRepository ON Schedule.game_id = MediaRepository.game_id AND 
                        Schedule.date >= CAST(TO_CHAR(CURRENT_DATE - INTERVAL '7 days', 'YYYYMMDD') AS int)
                        AND 
                        Schedule.date <= CAST(TO_CHAR(CURRENT_DATE, 'YYYYMMDD') AS int)
                        AND MediaRepository.status = 1""")
        row = cursor.fetchall()
        if row != (None,):
            media_inf = row
            i = 0
            counter = len(media_inf) - launch_point
            while i < limit and counter != 0:
                final.append(media_inf[counter-1])
                i += 1
                counter += -1
        else:
            assert(False)
        return final, length


def FoundSomever(limit: int, launch_point: int, interval: str, phrase: str) -> list[tuple[int, str, int, int]]:

    media_inf:list[tuple[int, str, int, int]] = []
    gid:int = -1
    sport:str = ''
    date:int = -1
    time:int = -1
    schedule:Any = None
    inf:tuple[int, str, int, int]

    with connection:
        cursor.execute(f"""SELECT DISTINCT(Schedule.game_id) AS gid, Schedule.sport, Schedule.date, Schedule.time 
                        FROM schedule
                        LEFT JOIN MediaRepository ON (Schedule.game_id = MediaRepository.game_id and (MediaRepository.counter < 20 or MediaRepository.counter is null))
                        JOIN Users ON 
                            ('{phrase}' = 'loading' AND 'all_games' = %s AND MediaRepository.counter < 20)
                            OR
                            ('{phrase}' = 'loading' 
                            AND 'last_games' = %s
                            AND MediaRepository.counter < 20 
                            AND date >= CAST(TO_CHAR(CURRENT_DATE - INTERVAL '7 days', 'YYYYMMDD') AS int)
                            AND date <= CAST(TO_CHAR(CURRENT_DATE, 'YYYYMMDD') AS int))
                            OR
                            ('{phrase}' = 'viewing' AND 'all_games' = %s AND MediaRepository.counter > 0)
                            OR
                            ('{phrase}' = 'viewing' 
                            AND 'last_games' = %s
                            AND MediaRepository.counter > 0
                            AND date >= CAST(TO_CHAR(CURRENT_DATE - INTERVAL '7 days', 'YYYYMMDD') AS int)
                            AND date <= CAST(TO_CHAR(CURRENT_DATE, 'YYYYMMDD') AS int))
                        WHERE Schedule.status = -1
                        ORDER BY gid DESC 
                        LIMIT {limit} OFFSET {launch_point};""", (interval, interval, interval, interval,))
        schedule = cursor.fetchall()
        if schedule is not None:
            for inf in schedule:
                gid, sport, date, time = inf
                media_inf.append((gid, sport, date, time))
        else:
            assert(False)
        return media_inf

def SelectLastGamesFRomMedia(limit: int, launch_point: int) -> tuple[list[tuple[int, str, int, int]], int]:

    media_inf:list[tuple[int, str, int, int]] = []
    row:Any = None
    gid:int = -1
    sport:str = ''
    date:int = -1
    time:int = -1
    length:int = -1

    with connection:
        media_inf = []
        cursor.execute(f"""SELECT Schedule.game_id, sport, date, time 
                        FROM Schedule
                        JOIN MediaRepository ON MediaRepository.game_id = Schedule.game_id 
                        ORDER BY MediaRepository.id DESC 
                        LIMIT {limit} OFFSET {launch_point}""")
        row = cursor.fetchone()
        if row is not None:
            gid, sport, date, time = row
            media_inf.append((gid, sport, date, time))
        else:
            assert(False)
        cursor.execute("SELECT COUNT(*) FROM MediaRepository WHERE file_id20 IS NOT NULL")
        row = cursor.fetchone()
        if row is not None:
            length = row[0]
        else:
            assert(False)
        return media_inf, length

def FindSomeGamesForView() -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM MediaRepository WHERE file_id IS NOT NULL")
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
        else:
            assert(False)
        return result
        
    
def SelectLastWeekFRomMedia2(limit: int, launch_point: int) -> list[tuple[int, str, int, int]]:
    
    media_inf:list[tuple[int, str, int, int]] = []
    row:Any = None
    gid:int = -1
    sport:str = ''
    date:int = -1
    time:int = -1

    with connection:
        cursor.execute(f"""SELECT Schedule.game_id, sport, date, time 
                        FROM Schedule
                        JOIN MediaRepository ON MediaRepository.game_id = Schedule.game_id
                        WHERE file_id20 IS NOT NULL AND date > EXTRACT(YEAR FROM CURRENT_DATE) * 10000 + EXTRACT(MONTH FROM CURRENT_DATE) * 100 + EXTRACT(DAY FROM CURRENT_DATE)
                        ORDER BY MediaRepository.id DESC 
                        LIMIT {limit} OFFSET {launch_point}""")
        row = cursor.fetchone()
        if row is not None:
            gid, sport, date, time = row
            media_inf.append((gid, sport, date, time))
        else:
            assert(False)
        return media_inf

def SelectLastWeekFRomMedia(limit: int, launch_point: int):

    media_inf:list[tuple[int, str, int, int]] = []
    row:Any = None
    gid:int = -1
    sport:str = ''
    date:int = -1
    time:int = -1

    with connection:
        cursor.execute(f"""SELECT Schedule.game_id, sport, date, time 
                        FROM Schedule
                        JOIN MediaRepository ON MediaRepository.game_id = Schedule.game_id
                        WHERE file_id20 IS NOT NULL AND date > EXTRACT(YEAR FROM CURRENT_DATE) * 10000 + EXTRACT(MONTH FROM CURRENT_DATE) * 100 + EXTRACT(DAY FROM CURRENT_DATE)
                        ORDER BY MediaRepository.id DESC 
                        LIMIT {limit} OFFSET {launch_point}""")
        row = cursor.fetchone()
        if row is not None:
            gid, sport, date, time = row
            media_inf.append((gid, sport, date, time))
        else:
            assert(False)
        return media_inf
    
def SelectLastGamesFRomMedia2(limit: int, launch_point: int) -> tuple[list[tuple[int, str, int, int]], int]:

    media_inf:list[tuple[int, str, int, int]] = []
    row:Any = None
    gid:int = -1
    sport:str = ''
    date:int = -1
    time:int = -1
    length:int = -1

    with connection:
        cursor.execute(f"""SELECT Schedule.game_id, sport, date, time 
                        FROM Schedule
                        JOIN MediaRepository ON MediaRepository.game_id = Schedule.game_id
                        WHERE file_id20 IS NOT NULL
                        ORDER BY MediaRepository.id DESC 
                        LIMIT {limit} OFFSET {launch_point}""")
        row = cursor.fetchone()
        if row is not None:
            gid, sport, date, time = row
            media_inf.append((gid, sport, date, time))
        else:
            assert(False)
        cursor.execute("SELECT COUNT(*) FROM MediaRepository WHERE file_id20 IS NOT NULL")
        row = cursor.fetchone()
        if row is not None:
            length = row[0]
        else:
            assert(False)
        return media_inf, length
    

    
def SelectGames(limit: int, launch_point: int, interval: str) -> list[tuple[int, str, int, int]]:

    media_inf:list[tuple[int, str, int, int]] = []
    gid:int = -1
    sport:str = ''
    date:int = -1
    time:int = -1
    schedule:Any = None
    inf:tuple[int, str, int, int]

    with connection:
        cursor.execute(f"""SELECT DISTINCT(Schedule.game_id) AS gid, Schedule.sport, Schedule.date, Schedule.time 
                        FROM schedule
                        LEFT JOIN MediaRepository ON (Schedule.game_id = MediaRepository.game_id and (MediaRepository.counter < 20 or MediaRepository.counter is null))
                        JOIN Users ON 
                            (Users.media_direction = 'loading' AND 'all_games' = %s AND MediaRepository.counter < 20)
                            OR
                            (Users.media_direction = 'loading' 
                            AND 'last_games' = %s
                            AND MediaRepository.counter < 20 
                            AND date >= CAST(TO_CHAR(CURRENT_DATE - INTERVAL '7 days', 'YYYYMMDD') AS int)
                            AND date <= CAST(TO_CHAR(CURRENT_DATE, 'YYYYMMDD') AS int))
                            OR
                            (Users.media_direction = 'viewing' AND 'all_games' = %s AND MediaRepository.counter > 0)
                            OR
                            (Users.media_direction = 'viewing' 
                            AND 'last_games' = %s
                            AND MediaRepository.counter > 0
                            AND date >= CAST(TO_CHAR(CURRENT_DATE - INTERVAL '7 days', 'YYYYMMDD') AS int)
                            AND date <= CAST(TO_CHAR(CURRENT_DATE, 'YYYYMMDD') AS int))
                        WHERE Schedule.status = -1
                        ORDER BY gid DESC 
                        LIMIT {limit} OFFSET {launch_point};""", (interval, interval, interval, interval,))
        schedule = cursor.fetchall()
        if schedule is not None:
            for inf in schedule:
                gid, sport, date, time = inf
                media_inf.append((gid, sport, date, time))
        else:
            assert(False)
        return media_inf

def CheckGameId(game_id: int) -> bool:
    row:Any = None
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



def SelectMediaDelGame(id: int) -> tuple[list[str], list[str]]:
    datafileid_list:list[str] = []
    datatype_list:list[str] = []
    row:Any = None
    with connection:
        cursor.execute(f"""SELECT MediaRepository.file_id, MediaRepository.typeoffile
                    FROM MediaRepository
                    JOIN Users ON MediaRepository.game_id = Users.del_game_game_id
                    WHERE Users.user_id = %s
                    AND
                        MediaRepository.file_id IS NOT NULL 
                    AND 
                        MediaRepository.typeoffile IS NOT NULL
                    AND 
                        MediaRepository.status = 1""", (id,))
        row = cursor.fetchall()
        if row is not None:
            for data in row:
                datafileid_list.append(data[0])
                datatype_list.append(data[1])
        return datafileid_list, datatype_list
    
def CoutFreeSeatsOfFile(game_id: int) -> int:

    row:Any = None
    counter:int = 0

    with connection:
        cursor.execute(f"SELECT counter FROM MediaRepository WHERE game_id = %s", (game_id,))
        row = cursor.fetchone()
        if row is not None:
            counter = row[0]
        return counter

def SaveToDatabase(quantitymedia: int, game_id: int, id: int) -> tuple[int, bool, int]:
    row:Any = None
    counter:int = -1
    halt:bool = False
    with connection:
        cursor.execute("SELECT counter FROM MediaRepository WHERE game_id = %s and (status = 1 or status = 0)", (game_id,))
        row = cursor.fetchone() 
        print(row, game_id)
        if row is not None:
            if (row[0] + quantitymedia) <= 20:
                halt = True
                cursor.execute("UPDATE MediaRepository SET status = 1 WHERE game_id = %s AND status = 0", (game_id,))
                cursor.execute("UPDATE Users SET counter_mediagroup = %s WHERE user_id = %s", ((quantitymedia + 1), id,))
                cursor.execute("UPDATE Users SET actionwithmes = 'DEL' WHERE user_id = %s", (id,))
            else:
                counter = 20 - (row[0] - quantitymedia)
        else:
            assert(False)

    return counter, halt, quantitymedia
    
def TryAgainSaveToDatbase(id: int, game_id: int) -> tuple[bool, int]:

    halt:bool = False
    row:Any = None
    freespace:int = -1

    with connection:
        cursor.execute("SELECT MediaRepository.counter, Users.counter_mediagroup FROM MediaRepository, Users WHERE MediaRepository.game_id = %s AND MediaRepository.status = 1 AND Users.user_id = %s", (game_id, id,))
        row = cursor.fetchone()
        if row is not None:
            all, user = row
            freespace = 20 - (all - user)
            if freespace > 0:
                halt = True
                print(game_id, id, freespace)
                cursor.execute("""UPDATE MediaRepository 
                               SET status = 1 
                               WHERE game_id = %s 
                               AND user_id = %s 
                               AND status = 0 
                               AND id IN (SELECT id FROM MediaRepository WHERE game_id = %s AND user_id = %s AND status = 0 LIMIT %s);

                               UPDATE Users SET counter_mediagroup = %s WHERE user_id = %s""", (game_id, id, game_id, id, freespace, freespace, id,))
                #cursor.execute("UPDATE Users SET counter_mediagroup = %s WHERE user_id = %s", (freespace, id,))
        else:
            assert(False)
    return halt, freespace

def UpdateMediaGroup(mgid: str, file_id: str, user_id: int, typeoffile: str) -> tuple[bool, int]:
    counter_mediagroup:int = -1
    id_mediagroup:str = '0'
    halt:bool = False
    row:Any = None

    with connection:
        cursor.execute("""SELECT Users.counter_mediagroup, Users.id_mediagroup, Users.del_game_game_id, MediaRepository.counter
                       FROM Users, MediaRepository 
                       WHERE Users.user_id = %s AND MediaRepository.user_id = %s AND Users.del_game_game_id = MediaRepository.game_id""", (user_id, user_id,))
        row = cursor.fetchone()
        print("row is", row)
        if row is not None:
            counter_mediagroup, id_mediagroup, game_id, counter = row
        else:
            counter_mediagroup = 0
            id_mediagroup = mgid
            counter = 0
            cursor.execute("SELECT del_game_game_id FROM Users WHERE user_id = %s", (user_id,))
            row = cursor.fetchone()
            if row is not None:
                game_id = row[0]
            else:
                assert(False)
        if counter_mediagroup <= 10 and ((id_mediagroup == '0') or (id_mediagroup == mgid)):
            halt = True
            counter_mediagroup += 1
            cursor.execute("INSERT INTO MediaRepository (game_id, user_id, file_id, typeoffile, counter) VALUES (%s, %s, %s, %s, %s)", (game_id, user_id, file_id, typeoffile, counter+1))
            cursor.execute("UPDATE MediaRepository SET counter = %s WHERE game_id = %s", (counter+1, game_id,))
        return halt, counter_mediagroup