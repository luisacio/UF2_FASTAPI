#Import List
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

items = {
    1: {"id": 1, "item_name": "pc", "price": 600, "store": "Madrid", "quantity": 10, "colour": "White"},
    2: {"id": 2, "item_name": "car", "price": 20000, "store": "BCN", "quantity": 2, "colour": "Red"},
    3: {"id": 3, "item_name": "speaker", "price": 30, "store": "Cordoba", "quantity": 18, "colour": "Brown"},
    4: {"id": 4, "item_name": "mouse", "price": 15, "store": "Malaga", "quantity": 59, "colour": "Black"},
    5: {"id": 5, "item_name": "pen", "price": 2, "store": "Bilbao", "quantity": 345, "colour": "Blue"},
}

class Item(BaseModel):
    id: int
    item_name: str
    price: float
    store: str
    quantity: int
    colour: Optional[str] = None

'''
#response??
@app.get("/itemssss/{item_id}")
def get_item(id: int,response:Response):
    if Response == 404:
        return {"msg":"Error"}
        #raise HTTPException(status_code=404, detail="Item error")
    return {"Item id": id}

'''
@app.get("/items/{id}")
def get_item(id: int):
    if id not in items:
        raise HTTPException(status_code=404, detail="Item error")
    return {"Item id": id}

@app.post("/items/")
def create_item(item: Item):
    #Crear item en arxiu o bbdd
    #Crear validacio si existeix previament l item.
    #items = {item.id:{"item_name":item.item_name,"price":item.price,"store":item.store,"quantity":item.quantity,"colour":item.colour}}

    return {
        "id": item.id,
        "item_name": item.item_name,
        "price": item.price,
        "store": item.store,
        "quantity": item.quantity,
        "colour": item.colour
    }