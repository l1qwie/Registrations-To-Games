import psycopg2
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

def CompletionOfRegistration(id: int):
    with connection:
        cursor.execute("UPDATE Users SET setup_reg = 'completed' WHERE user_id = %s", (id,))