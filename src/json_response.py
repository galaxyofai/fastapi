from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return {"Hello":"World"}


@app.get("/next/{items_no}")
def main_2(items_no:int):
    return {"Hello":items_no}
