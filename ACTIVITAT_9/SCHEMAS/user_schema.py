from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: int = Field()
    name: Optional[str] = None