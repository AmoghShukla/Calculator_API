from fastapi import FastAPI, HTTPException
from routers.Operations import router as Operations_Router 

app = FastAPI(title="Basic Calculator API")

app.include_router(Operations_Router)

@app.get("/")
def Home():
    return {"Message" : "Welcome to the Basic Calculator API."}