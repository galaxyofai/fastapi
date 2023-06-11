from fastapi import FastAPI

app = FastAPI()

#uvicorn main:app --reload

@app.get("/")
def hello():
    return {"hello":"world"}