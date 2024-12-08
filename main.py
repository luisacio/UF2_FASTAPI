from fastapi import FastAPI,Body
from pydantic import BaseModel, Field
from typing import Annotated,Optional, List
import psycopg2
import json

app = FastAPI()

class User(BaseModel):
    id: int = Field()
    name: Optional[str] = None

@app.get("/users", response_model=List[dict])
async def get_all_users():

    conn = psycopg2.connect(
        dbname="fastapi_bbdd",
        user="postgres",
        password="luis",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    cur.execute("""SELECT ID,NAME FROM public.users ORDER BY id ASC  """)
    users = cur.fetchall()

    users_dicc = [{"id": item[0], "name": item[1]} for item in users]

    cur.close()
    conn.close()
    return users_dicc