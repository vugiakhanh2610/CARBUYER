from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.car import router as CarRouter
from server.routes.brand import router as BrandRouter

app = FastAPI()
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(CarRouter, tags=["Car"])
app.include_router(BrandRouter, tags=["Brand"], prefix="/brand")
