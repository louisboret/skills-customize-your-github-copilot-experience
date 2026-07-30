from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

items = [
    {"id": 1, "name": "Notebook", "description": "A ruled notebook", "price": 4.99},
    {"id": 2, "name": "Pencil", "description": "A graphite pencil", "price": 0.99},
    {"id": 3, "name": "Eraser", "description": "A soft eraser", "price": 1.49},
]

@app.get("/items", response_model=List[Item])
def read_items():
    return items

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item)
def create_item(item: Item):
    new_item = item.dict()
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for idx, existing_item in enumerate(items):
        if existing_item["id"] == item_id:
            updated_item = item.dict()
            updated_item["id"] = item_id
            items[idx] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")
