from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api")
async def hello_world():
    return JSONResponse(content={"message": "Hello World"})

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to FastAPI on Vercel"})
