from fastapi import FastAPI
from fastapi.responses import JSONResponse
from mangum import Mangum

app = FastAPI()

@app.get("/api")
async def hello_world():
    return JSONResponse(content={"message": "Hello World"})

@app.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to FastAPI on Vercel"})

# Mangum handler to wrap the FastAPI app
handler = Mangum(app)
