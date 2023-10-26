from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hello World, Soy Daniel"


@app.get("/nombre")
async def root():
    return {"nombre":"Daniel"}



