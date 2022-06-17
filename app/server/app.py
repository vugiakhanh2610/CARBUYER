from fastapi import FastAPI
from server.routes.car import router as CarRouter
from server.routes.brand import router as BrandRouter

app = FastAPI()

app.include_router(CarRouter, tags=["Car"], prefix="/car")
app.include_router(BrandRouter, tags=["Brand"], prefix="/brand")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
