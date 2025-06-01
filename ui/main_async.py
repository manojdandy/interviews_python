from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

@app.get("/1")
def hello():
    print(f"hello ")
    return "hello"