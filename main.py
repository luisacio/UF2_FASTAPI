from fastapi import FastAPI
from typing import List
from ACTIVITAT_10.CRUD import crud_actions
from ACTIVITAT_10.SHEMES.schemes import *

app = FastAPI()

@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def get_all_theme():
    return words_themes_schema(crud_actions.read_all_theme())

@app.get("/penjat/tematica/{option}", response_model=List[dict])
async def get_word(option):
    return words_themes_schema(crud_actions.read_word(option))