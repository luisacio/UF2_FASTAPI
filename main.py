from fastapi import FastAPI
from typing import List

from ACTIVITAT_12.BASE_MODEL.base_model import User,UserScore,GameWord,CodeRender
from ACTIVITAT_12.CRUD import crud_actions
from ACTIVITAT_12.SCHEMES.schemes import *

app = FastAPI()

#------------------------TAULA GAME_WORDS-------------------------#
#Endpoint per mostrar tematica
@app.get("/penjat/theme/options", response_model=List[dict])
async def get_theme():
    return list_format_schema(crud_actions.select_theme())

#Endpoint per rebre la paraula aleatoria
@app.get("/penjat/theme/{option}", response_model=List[dict])
async def get_word(option):
    return list_format_schema(crud_actions.select_word(option))

#Endpoint per INSERTAR la paraula aleatoria i el seu tema
@app.post("/penjat/insert_word")
async def post_word(game_word:GameWord):
    crud_actions.insert_word(game_word)
    return {"msg": "Word saved"}

#Endpoint per ACTUALITZAR la paraula aleatoria i el seu tema
@app.put("/penjat/update_word")
async def put_word(game_word:GameWord):
    crud_actions.update_word(game_word)
    return {"msg": "Word updated"}

#Endpoint per ESBORRAR la paraula aleatoria i el seu tema
@app.delete("/penjat/delete_word")
async def delete_word(game_word:GameWord):
    crud_actions.delete_word(game_word)
    return {"msg": "Word deleted"}

#------------------------TAULA INFO_RENDER-------------------------#
#Endpoint per cualsevol missatge simple del joc, inclos l´abecedari
@app.get("/penjat/{code}", response_model=List[dict])
async def get_render(code):
    return list_format_schema(crud_actions.select_render(code))

#Endpoint per INSERTAR un render
@app.post("/penjat/insert_render")
async def post_render(render:CodeRender):
    crud_actions.insert_render(render)
    return {"msg": "Render inserted"}

#Endpoint per ACTUALITZAR un render
@app.put("/penjat/update_render")
async def put_render(render:CodeRender):
    crud_actions.update_render(render)
    return {"msg": "Render updated"}

#Endpoint per ESBORRAR un render
@app.delete("/penjat/delete_render")
async def delete_render(render:CodeRender):
    crud_actions.delete_render(render)
    return {"msg": "Render deleted"}

#------------------------TAULA USUARIO-------------------------#
#Endpoint per rebre les dades del usuari
@app.get("/penjat/user/{user}",response_model=List[dict])
async def get_user(user):
    return list_format_user_schema(crud_actions.select_user(user))

#Endpoint per INSERTAR usuari
@app.post("/penjat/insert_user")
async def post_user(user:User):
    crud_actions.insert_user(user)
    return {"msg": "New user done"}

#Endpoint per ACTUALITZAR un usuari
@app.put("/penjat/update_user")
async def put_user(user:User):
    crud_actions.update_user(user)
    return {"msg": "User updated"}

#Endpoint per ESBORRAR un usuari
@app.delete("/penjat/delete_user")
async def delete_user(user:User):
    crud_actions.delete_user(user)
    return {"msg": "User deleted"}

#------------------------TAULA USUARIO_PUNTUACION-------------------------#
#Endpoint per rebre les dades de la partida actual
@app.get("/penjat/id_partida/{id_game}",response_model=List[dict])
async def get_user_score(id_game):
    return list_format_game_schema(crud_actions.select_user_score(id_game))

#Endpoint per INSERTAR partida
@app.post("/penjat/insert_game")
async def post_user_score(user_score:UserScore):
    crud_actions.insert_user_score(user_score)
    return {"msg": "Game inserted"}

#Endpoint per ACTUALITZAR dades de la partida
@app.put("/penjat/save_game")
async def put_user_score(user_score:UserScore):
    crud_actions.update_user_score(user_score)
    return {"msg": "Game saved"}

#Endpoint per ESBORRAR dades de la partida
@app.delete("/penjat/delete_game")
async def delete_user_score(user_score:UserScore):
    crud_actions.delete_user_score(user_score)
    return {"msg": "Game deleted"}

