from fastapi import FastAPI
from typing import List
from ACTIVITAT_9.CRUD import crud_actions

app = FastAPI()

@app.get("/users", response_model=List[dict])
async def get_all_users():
    return crud_actions.read_all_users()