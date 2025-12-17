from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

db_file = './db/shopping_list.json'

class Item(BaseModel):
    id: int
    name: str
    quantity: int

@app.on_event("startup")
def startup():
    if not os.path.exists(db_file):
        with open(db_file, 'w') as f:
            json.dump([], f)

@app.get("/items")
def read_items():
    with open(db_file, 'r') as f:
        items = json.load(f)
    return items

@app.post("/items")
def create_item(item: Item):
    item.id = len(read_items()) + 1
    items = read_items()
    items.append(item.dict())
    with open(db_file, 'w') as f:
        json.dump(items, f)
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
