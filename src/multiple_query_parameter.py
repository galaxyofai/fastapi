from fastapi import FastAPI
from typing import Optional
app =FastAPI()

@app.get("/")
def hello():
    return "hello"

# @app.get("/fruit/{fruit_name}/count/{fruit_count}")
# def fruits(fruit_name:str,fruit_count:int):
#     return {"fruit_name":fruit_name,"fruit_count":fruit_count}

# @app.get("/fruit/{fruit_name}/count/{fruit_count}")
# def fruits(total_weight:int,fruit_name:str,fruit_count:int=45):
#     return {"fruit_name":fruit_name,"fruit_count":fruit_count,"total_weight":total_weight}



@app.get("/fruit/{fruit_name}/count/{fruit_count}")
def fruits(fruit_name:str,fruit_count:int=45,total_weight:Optional[int]=5):
    return {"fruit_name":fruit_name,"fruit_count":fruit_count,"total_weight":total_weight}
