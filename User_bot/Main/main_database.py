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

def FindNamedb(id: int) -> str:
    row:Any = None
    db_name:str = ''
    with connection:
        cursor.execute("SELECT db_name FROM clients WHERE user_id = %s AND status = 'ACTIVE'", (id,))
        row = cursor.fetchone()
        if row is not None:
            db_name = row[0]
            cursor.execute("UPDATE clients SET connection = 'connected' WHERE user_id = %s AND status = 'ACTIVE'", (id,))
        return db_name

def FindUser(id: int, language: str) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Users WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] != 0:
                result = True
            else:
                cursor.execute("INSERT INTO Users (user_id, action, language, level) VALUES (%s, 'registration', %s, %s)", (id, language, 0,))
        else:
            assert(False)
        return result
    
def ResetAllInf(id: int):
    with connection:
        cursor.execute("""UPDATE Users SET
                       name = NULL, last_name = NULL, username = NULL, actionwithmes = NULL,
                       game_id_reg_to_game = NULL, sport_reg_to_game = NULL, date_reg_to_game = NULL, time_reg_to_game = NULL, seats_reg_to_game = NULL, payment_reg_to_game = NULL, payment_status_reg_to_game = NULL,
                       media_time_interval = NULL, media_direction = NULL, media_limit = NULL, media_launch_point = NULL, del_game_game_id = NULL,
                       counter_mediagroup = NULL, id_mediagroup = NULL,
                       user_records_action = NULL, user_records_sport = NULL, user_records_date = NULL, user_records_time = NULL, user_records_what_change = NULL, user_records_newseats = NULL, user_records_changpayeorwhat = NULL, user_records_deleteorwhat = NULL,
                       notifgameid = NULL,
                       action = NULL WHERE user_id = %s""", (id,))

def FindAllDb() -> list[str]:
    res:Any = None
    finalres:list[str] = []
    with connection:
        cursor.execute("SELECT db_name FROM clients WHERE status = 'ACTIVE'")
        res = cursor.fetchall()
        if res is not None:
            finalres = [row[0] for row in res]
        else:
            finalres = []
        return finalres

def WhoSleep() -> tuple[list[int], list[int], list[str]]:
    row:Any = None
    row2:Any = None
    user_ids:list[int] = []
    exmessid:list[int] = []
    user_langs:list[str] = []
    with connection:
        exmessid = []
        cursor.execute("""SELECT user_id
                        FROM Users
                        WHERE NOT (level = 3 AND action = 'divarication')
                        AND NOT (level = 5 AND action = 'photos&videos' AND media_direction = 'viewing')
                        AND NOT (level = 6 AND action = 'photos&videos' AND media_direction = 'loading')
                        AND (CURRENT_TIMESTAMP - last_time_use) > INTERVAL '1 hour'
                        AND username IS NOT NULL
                        AND action NOT IN ('registration', 'see schedule')
                        AND level <> 0;
                        """)
        row = cursor.fetchall()
        if row is not None and row != []:
            user_ids = [i[0] for i in row]
            for id in user_ids:
                cursor.execute("SELECT CURRENT_TIMESTAMP")
                row = cursor.fetchone()
                if row is not None:
                    cursor.execute("UPDATE Users SET last_time_use = %s WHERE user_id = %s", (row[0], id,))
                    cursor.execute("SELECT language, exmess FROM Users WHERE user_id = %s", (id,))
                    row2 = cursor.fetchone()
                    if row2 is not None:
                        exmessid.append(row2[0])
                        user_langs.append(row2[1])
                    else:
                        assert(False)
                else:
                    assert(False)
        return user_ids, exmessid, user_langs

def IsItFirsTime() -> int:
    row:Any = None
    count:int = -1
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WaitingForNotification WHERE status = 'waiting' AND (setup IS NULL OR setup <> 'DELETE') AND whonotif = 'bot' AND last_time_notif IS NULL")
        row = cursor.fetchone()
        if row is not None:
            count = row[0]
        else:
            assert(False)
        return count

def WhoNeedNotifFirstTime() -> tuple[list[int], list[int], list[int], list[str]]:

    row:Any = None
    users_id:list[int] = []
    exmessids:list[int] = []
    uids:list[int] = []
    game_id:list[int] = []
    languages:list[str] = []

    with connection:
        cursor.execute("SELECT user_id FROM WaitingForNotification WHERE status = 'waiting' AND (setup IS NULL OR setup <> 'DELETE') AND whonotif = 'bot' AND last_time_notif IS NULL")    
        users_id = [row[0] for row in cursor.fetchall()]
        for id in users_id:
            if id not in uids:
                uids.append(id)
                cursor.execute("SELECT language, exmess FROM Users WHERE user_id = %s", (id,))
                row = cursor.fetchone()
                if row is not None:
                    languages.append(row[0])
                    exmessids.append(row[1])
                else:
                    assert(False)
                cursor.execute("SELECT game_id FROM WaitingForNotification WHERE status = 'waiting' AND (setup IS NULL OR setup <> 'DELETE') AND whonotif = 'bot' AND last_time_notif IS NULL AND user_id = %s", (id,))
                row = cursor.fetchone()
                if row is not None:
                    game_id.append(row[0])
                else:
                    assert(False)
        return uids, exmessids, game_id, languages

def RecordingTimeNotif(id: int, game_id: int):
    row:Any = None
    with connection:
        cursor.execute("SELECT counter_notif FROM WaitingForNotification WHERE user_id = %s AND game_id = %s AND setup <> 'DELETE'", (id, game_id))
        row = cursor.fetchone()
        if row is not None:
            cursor.execute("UPDATE WaitingForNotification SET last_time_notif = CURRENT_TIMESTAMP, counter_notif = %s WHERE user_id = %s AND game_id = %s AND (setup IS NULL OR setup <> 'DELETE')", (row[0]+1, id, game_id))
        else:
            assert(False)

def IsItNotFirstTime() -> int:
    row:Any = None
    count:int = -1
    with connection:
        cursor.execute("SELECT COUNT(*) FROM WaitingForNotification WHERE status = 'waiting' AND (setup IS NULL OR setup <> 'DELETE') AND whonotif = 'bot' AND last_time_notif IS NOT NULL")
        row = cursor.fetchone()
        if row is not None:
            count = row[0]
        else:
            assert(False)
        return count
    
def WhoNeedNotifNotInTheFirstTime() -> tuple[list[int], list[int], list[int], list[int], list[str]]:

    languages:list[str] = []
    row:Any = None
    users_id:list[int] = []
    game_id:list[int] = []
    counternotifs:list[int] = []
    exmessids:list[int] = []
    uids:list[int] = []
    results:Any = None

    with connection:
        cursor.execute("""SELECT WaitingForNotification.user_id, WaitingForNotification.game_id, Users.language
                        FROM WaitingForNotification, Users
                        WHERE WaitingForNotification.status = 'waiting'
                        AND (WaitingForNotification.setup IS NULL OR WaitingForNotification.setup <> 'DELETE')
                        AND WaitingForNotification.whonotif = 'bot'
                        AND (CURRENT_TIMESTAMP - WaitingForNotification.last_time_notif) > INTERVAL '1 hour'
                    """)
        results = cursor.fetchall()
        if results:
            users_id = [row[0] for row in results]
            game_id = [row[1] for row in results]
            languages = [row[2] for row in results]
        for id, gid in zip(users_id, game_id):
            if id not in uids:
                uids.append(id)
                cursor.execute("SELECT exmess FROM Users WHERE user_id = %s", (id,))
                row = cursor.fetchone()
                if row is not None:
                    exmessids.append(row[0])
                else:
                    assert(False)
                cursor.execute("SELECT counter_notif FROM WaitingForNotification WHERE user_id = %s AND game_id = %s AND (setup IS NULL OR setup <> 'DELETE')", (id, gid,))
                row = cursor.fetchone()
                if row is not None:
                    counternotifs.append(row[0])
                else:
                    assert(False)
        return uids, exmessids, game_id, counternotifs, languages

def DeleteRecordOfUser(id: int, gid: int):
    row:Any = None
    with connection:
        cursor.execute("UPDATE WaitingForNotification SET status = 'notified', setup = 'DELETE' WHERE user_id = %s AND game_id = %s", (id, gid,))
        cursor.execute("SELECT seats FROM WatingForGamesUsers WHERE user_id = %s AND game_id = %s", (id, gid,))
        row = cursor.fetchone()
        if row is not None:
            cursor.execute("UPDATE WatingForGamesUsers SET status = 'DELETE' WHERE user_id = %s AND game_id = %s", (id, gid,))
            cursor.execute("UPDATE Schedule SET seats = %s WHERE game_id = %s", (row[0], gid,))
        else:
            assert(False)

def RecallUser(id: int, 
                language: str, 
                game_id_reg_to_game: int, launch_point_reg_to_game: int, sport_reg_to_game: str, seats_reg_to_game: int, payment_reg_to_game: str, 
                media_time_interval: str, media_direction: str, media_limit:int, media_launch_point:int, del_game_game_id:int, id_mediagroup: str,
                counter_mediagroup:int,
                us_set_lanuch_point:int, us_set_what_set:str, us_set_game_id:int, us_set_act_game:str, us_set_what_we_will_change:str, us_set_new_pay:str,
                notifgameid:int,
                action:str, level: int) -> tuple[int, str, int, int, str, int, str, str, str, int, int, int, str, int, int, str, int, str, str, str, int, str, int]:

    row:Any = None
    with connection:
        cursor.execute("""SELECT user_id, 
                    language,
                    game_id_reg_to_game, launch_point_reg_to_game, sport_reg_to_game, seats_reg_to_game, payment_reg_to_game,
                    media_time_interval, media_direction, media_limit, media_launch_point, del_game_game_id, id_mediagroup,
                    counter_mediagroup,
                    us_set_lanuch_point, us_set_what_set, us_set_game_id, us_set_act_game, us_set_what_we_will_change, us_set_new_pay,
                    notifgameid,
                    action, level FROM Users WHERE user_id = %s""", (id,))
        row = cursor.fetchone()
        if row is not None:
            (id, 
            language,
            game_id_reg_to_game, launch_point_reg_to_game, sport_reg_to_game, seats_reg_to_game, payment_reg_to_game,
            media_time_interval, media_direction, media_limit, media_launch_point, del_game_game_id, id_mediagroup,
            counter_mediagroup,
            us_set_lanuch_point, us_set_what_set, us_set_game_id, us_set_act_game, us_set_what_we_will_change, us_set_new_pay,
            notifgameid,
            action, level) = row
        else:
            assert(False)
        cursor.execute("UPDATE Users SET last_time_use = CURRENT_TIMESTAMP WHERE user_id = %s", (id,))
        return (id, 
                language,
                game_id_reg_to_game, launch_point_reg_to_game, sport_reg_to_game, seats_reg_to_game, payment_reg_to_game,
                media_time_interval, media_direction, media_limit, media_launch_point, del_game_game_id, id_mediagroup,
                counter_mediagroup,
                us_set_lanuch_point, us_set_what_set, us_set_game_id, us_set_act_game, us_set_what_we_will_change, us_set_new_pay,
                notifgameid,
                action, level)

def RetainUser(user_id:int, 
            language:str,
            game_id_reg_to_game:int, launch_point_reg_to_game:int, sport_reg_to_game:str, seats_reg_to_game:int, payment_reg_to_game:str,
            media_time_interval:str, media_direction:str, media_limit:int, media_launch_point:int, del_game_game_id:int, id_mediagroup: str,
            counter_mediagroup:int,
            us_set_lanuch_point:int, us_set_what_set:str, us_set_game_id:int, us_set_act_game:str, us_set_what_we_will_change:str, us_set_new_pay:str,
            notifgameid:int,
            action:str, level:int):
    with connection:
        cursor.execute("""UPDATE Users SET user_id = %s, 
                    language = %s,
                    game_id_reg_to_game = %s, launch_point_reg_to_game = %s, sport_reg_to_game = %s, seats_reg_to_game = %s, payment_reg_to_game = %s,
                    media_time_interval = %s, media_direction = %s, media_limit = %s, media_launch_point = %s, del_game_game_id = %s, id_mediagroup = %s,
                    counter_mediagroup = %s,
                    us_set_lanuch_point = %s, us_set_what_set = %s, us_set_game_id = %s, us_set_act_game = %s, us_set_what_we_will_change = %s, us_set_new_pay = %s,
                    notifgameid = %s,
                    action = %s, level = %s WHERE user_id = %s""",
                        (user_id, 
                        language,
                        game_id_reg_to_game, launch_point_reg_to_game, sport_reg_to_game, seats_reg_to_game, payment_reg_to_game,
                        media_time_interval, media_direction, media_limit, media_launch_point, del_game_game_id, id_mediagroup,
                        counter_mediagroup,
                        us_set_lanuch_point, us_set_what_set, us_set_game_id, us_set_act_game, us_set_what_we_will_change, us_set_new_pay,
                        notifgameid,
                        action, level, user_id))

#Del Mes
def RecognizeExMesID(id: int, n: str, ln: str, un: str, lan: str) -> tuple[int, str]:
    row:Any = None
    search:int = -1
    exmesid:int = -1
    act:str = ''
    with connection:
        cursor.execute("SELECT COUNT(*) FROM Users WHERE user_id = %s", (id,))
        row = cursor.fetchone()
        if row is not None:
            search = row[0]
            if search != 0:
                cursor.execute("SELECT exmess, actionwithmes FROM Users WHERE user_id = %(id)s", ({"id": id}))
                row = cursor.fetchone()
                if row is not None:
                    exmesid, act = row
                    if exmesid != -1:
                        cursor.execute("SELECT custom_language FROM Users WHERE user_id = %s", (id,))
                        row = cursor.fetchone()
                        if row is not None:
                            if row:
                                cursor.execute("UPDATE Users SET name = %(n)s, last_name = %(ln)s, username = %(un)s, from_where = 'tg' WHERE user_id = %(id)s", ({"n": n, "ln": ln, "un": un, "lan": lan, "id": id}))
                            else:
                                cursor.execute("UPDATE Users SET name = %(n)s, last_name = %(ln)s, username = %(un)s, language = %(lan)s, from_where = 'tg' WHERE user_id = %(id)s", ({"n": n, "ln": ln, "un": un, "lan": lan, "id": id}))
                        else:
                            assert(False)
                else:
                    assert(False)
        else:
            assert(False)
        return exmesid, act
    
def AddNewMesID(id: int, mid: int, mgid: str):
    with connection:
        if mgid == '':
            cursor.execute("UPDATE Users SET actionwithmes = 'DEL', exmess = %(mid)s WHERE user_id = %(id)s", ({"mid": mid, "id": id}))
        else:
            cursor.execute("UPDATE Users SET actionwithmes = 'EDIT', exmess = %(mid)s WHERE user_id = %(id)s", ({"id": id, "mid": mid}))
            print("SHALOM!")


