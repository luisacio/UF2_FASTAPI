import psycopg2
from psycopg2 import OperationalError

def connect_to_bbdd():
    try:
        conn = psycopg2.connect(
                dbname="fastapi_bbdd",
                user="postgres",
                password="luis",
                host="localhost",
                port="5432"
            )

        cur = conn.cursor()
        res = [cur,conn]
    except OperationalError as e:
        res = ["ERROR",e]
    return res