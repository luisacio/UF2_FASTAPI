import psycopg2

def connect_to_bbdd():
    conn = psycopg2.connect(
            dbname="fastapi_bbdd",
            user="postgres",
            password="luis",
            host="localhost",
            port="5432"
        )

    cur = conn.cursor()

    return cur,conn