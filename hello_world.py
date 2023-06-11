

from fastapi import FastAPI

app =FastAPI()

# a and b are function parameter
def add(a,b):
    return a+b

# item is a path parameter
@app.get("/{item}")
def show_item(item:int):
    return {"Items":item}


# name and weight are query parameter
@app.get("/fruit")
def fruits(name:str,weight:str):
    return {"fruit_name":name,"fruit_weight":weight}