from fastapi import FastAPI,Body
from pydantic import BaseModel, Field
from typing import Annotated,Optional

app = FastAPI()

items = {
    1: {"item_id": 1, "item_name": "pc", "price": 600, "store": "Madrid", "quantity": 10, "colour": "White"},
    2: {"item_id": 2, "item_name": "car", "price": 20000, "store": "BCN", "quantity": 2, "colour": "Red"},
    3: {"item_id": 3, "item_name": "speaker", "price": 30, "store": "Cordoba", "quantity": 18, "colour": "Brown"},
    4: {"item_id": 4, "item_name": "mouse", "price": 15, "store": "Malaga", "quantity": 59, "colour": "Black"},
    5: {"item_id": 5, "item_name": "pen", "price": 2, "store": "Bilbao", "quantity": 345, "colour": "Blue"},
}

class Item(BaseModel):
    item_id: int
    item_name: str
    price: float = Field(gt=0, description="The price must be greater than zero")
    store: str
    quantity: int
    colour: Optional[str] = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results