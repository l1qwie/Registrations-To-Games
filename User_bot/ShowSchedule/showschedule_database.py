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


def CreateTable() -> list[tuple[str, int, int, int, str]]:
    data:Any = None
    with connection:
        cursor.execute("SELECT sport, date, time, seats, address FROM Schedule WHERE status != -1 ")
        data = cursor.fetchall()
        return data