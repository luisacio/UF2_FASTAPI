from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    game_total: int
    game_win: int
    score_record: int

class UserScore(BaseModel):
    id_game: int
    num_try: int
    current_score: int
    open_game: bool
    word:str

class GameWord(BaseModel):
    word: str
    new_word: Optional[str] = None
    theme: str

class CodeRender(BaseModel):
    code: str
    render: str