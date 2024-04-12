from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

name = ""


@app.get("/")
def read_root():
    return {"Hello": name}

@app.post("/")
def write_name(new_name):
        name = new_name
        return {"Hello": name}
    
@app.put("/")
def update_name(new_name):
    name = new_name
    return {"Hello": name}


@app.delete("/")
def delete_name():
    name = ""
    return {"Hello": name}


#@app.post("/items/{item_id}")
#def update_item(item_id: int, item: Item):
#   return {"item_name": item.name, "item_id": item_id}