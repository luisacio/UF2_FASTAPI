from fastapi import FastAPI
from typing import List

from ACTIVITAT_11.BASE_MODEL.base_model import Usuario,UsuarioPuntuacion
from ACTIVITAT_11.CRUD import crud_actions
from ACTIVITAT_11.SCHEMES.schemes import *

app = FastAPI()

#Endpoint per mostrar tematica
@app.get("/penjat/tematica/opcions", response_model=List[dict])
async def get_all_theme():
    return list_format_schema(crud_actions.read_all_theme())

#Endpoint per rebre la paraula aleatoria
@app.get("/penjat/tematica/{option}", response_model=List[dict])
async def get_word(option):
    return list_format_schema(crud_actions.read_word(option))

#Endpoint pel missatge "Començar partida"
@app.get("/penjat/{front_text}", response_model=List[dict])
async def get_render(front_text):
    return list_format_schema(crud_actions.get_render(front_text))

#Endpoint per crear usuari
@app.post("/penjat/insert_user")
async def post_insert_user(usuario:Usuario):
    crud_actions.post_insert_user(usuario)
    return {"msg": "Usuari creat"}

#Endpoint per crear partida
@app.post("/penjat/insert_game")
async def post_insert_game(usuario:UsuarioPuntuacion):
    crud_actions.post_insert_game(usuario)
    return {"msg": "Partida creada"}

#Endpoint per guardar intents a la partida
@app.put("/penjat/save_try")
async def post_save_try(usuario:UsuarioPuntuacion):
    crud_actions.post_save_try(usuario)
    return {"msg": "Partida guardada"}

#Endpoint per rebre el diccionari en castella, catala o neutre
@app.get("/penjat/{abc}",response_model=List[dict])
async def get_render(abc):
    return list_format_schema(crud_actions.get_render(abc))

#Endpoint per rebre les dades de la partida actual
@app.get("/penjat/id_partida/{id_partida}",response_model=List[dict])
async def get_game_data(id_partida):
    return list_format_game_schema(crud_actions.get_game_data(id_partida))

#Endpoint per rebre les dades del usuari
@app.get("/penjat/user/{user}",response_model=List[dict])
async def get_game_user(user):
    return list_format_user_schema(crud_actions.get_game_user(user))