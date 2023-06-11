from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app =FastAPI()

class Fruits(BaseModel):
    name:str
    weight :Optional[int]=None
    count:int


@app.get("/")
def hello():
    return "hello"


@app.put("/fruit")
def fruits(f:Fruits):
    return {"fruit_name":f.name,"fruit_count":f.count,"total_weight":f.weight}