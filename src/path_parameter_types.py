from fastapi import FastAPI

app =FastAPI()

@app.get("/")
def hello():
    return "hello"

@app.get("/{item}")
def show_item(item:int):
    return {"Items":item}