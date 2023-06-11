from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def main_get():
    return {"1":"2"}


@app.put("/hello")
def main_put():
    return {"1":"2"}

if __name__ == "__main__":

    # uvicorn.run(app, host="0.0.0.0", port=8003)
    uvicorn.run(app, host="0.0.0.0", port=8000)