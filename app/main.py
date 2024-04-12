from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

name = None


@app.get("/")
def read_root():
    return {"Hello": name}

if name is None:
    @app.post("/")
    def write_name(name):
        name = name
        return {"Hello": name}
    
@app.put("/")
def update_name(name):
    name = name
    return {"Hello": name}



@app.delete("/")
def delete_name(name):
    name = name
    return {"Hello": name}


#@app.post("/items/{item_id}")
#def update_item(item_id: int, item: Item):
#   return {"item_name": item.name, "item_id": item_id}