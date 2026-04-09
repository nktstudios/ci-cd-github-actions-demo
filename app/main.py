from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Hello Github Actions Demo from version 1!"
        }

@app.get("/sum/{a}/{b}")
def sum_numbers(a: int, b: int):
    return {
        "result": a + b + b
        }