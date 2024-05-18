from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.get("/items/")
async def read_items():
    return [{"name": "Plumbus", "price": 3.5}, {"name": "Portal Gun", "price": 9001}]