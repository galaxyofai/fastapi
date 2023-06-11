from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"Hello":"World"}


@app.get("/fruit_count/{fruit_count}")
def get_fruit_count(fruit_count:int):
    return {"Total Fruit Count":fruit_count}

@app.put("/fruit_count_1/{fruit_count}")
def put_fruit_count(fruit_count:int):
    return {"Total Fruit Count":fruit_count}