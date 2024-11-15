from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from main import main

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/querry/{querryString}")
def get_querry_rag(querryString: str):
    return main(querryString)

