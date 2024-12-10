from fastapi import FastAPI
from typing import List
from ACTIVITAT_11.CRUD import crud_actions
#from ACTIVITAT_11.SHEMES.schemes import Option

app = FastAPI()

@app.get("/penjat/{front_text}")
async def get_front_text(front_text):
    return crud_actions.get_front_text(front_text)

@app.get("/penjat/{user_id}")
async def get_tries_word(user_id):
    return crud_actions.get_front_text(user_id)

@app.post("/penjat/")
async def post_tries_word(front_text):
    return crud_actions.get_front_text(front_text)
'''
@app.get("/penjat/tematica/{option}", response_model=List[Option])
async def get_word(option):
    return crud_actions.read_word(option)
'''