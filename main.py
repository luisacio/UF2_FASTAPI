from fastapi import FastAPI
from typing import List
from ACTIVITAT_9.CRUD import crud_actions
from ACTIVITAT_9.SCHEMAS import user_schema

app = FastAPI()

@app.get("/users", response_model=List[dict])
async def get_all_users():
    return user_schema.users_schema(crud_actions.read_users())
