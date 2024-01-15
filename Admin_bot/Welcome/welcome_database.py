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

def Password(pas: str, aid: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT password FROM admins_password WHERE password = %s", (pas,))
        row = cursor.fetchone()
        if row is not None:
            cursor.execute("UPDATE Admins SET status = 1 WHERE user_id = %s", (aid,))
            result = True
        return result
    
def StatusReg(aid: int) -> bool:
    row:Any = None
    result:bool = False
    with connection:
        cursor.execute("SELECT status FROM Admins WHERE user_id = %s", (aid,))
        row = cursor.fetchone()
        if row is not None:
            if row[0] == 1:
                result = True
        return result
