from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Usuario(BaseModel):
    nombre: str
    partidas_total: int
    partidas_ganadas: int
    punt_record: int

class UsuarioPuntuacion(BaseModel):
    id_partida: int
    num_intents: int
    punt_actual: int
    part_abierta: bool
    palabra:str
    fecha_fin: Optional[datetime] = None

class GameWords(BaseModel):
    word: str
    theme: str

class InfoRender(BaseModel):
    code: str
    render: str