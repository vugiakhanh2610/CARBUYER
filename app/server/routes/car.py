from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import *
from server.models.car import *

router = APIRouter()


@router.post("/", response_description="Car's data added into the database")
async def add_car_data(car: CarSchema = Body(...)):
    car = jsonable_encoder(car)
    new_car = await add_car(car)
    return ResponseCarModel(new_car, "Car added successfully.")


@router.get("/", response_description="Get all cars")
async def get_cars_data():
    cars = await get_cars()
    if cars:
        return ResponseCarModel(cars, "Get all cars's data successfully")
    return ResponseCarModel(cars, "Empty list returned !")


@router.get("/{id}", response_description="Get car by id")
async def get_car_data_by_id(id):
    car = await get_car(id)
    if car:
        return ResponseCarModel(car, "Get car by id successfully")
    return ErrorResponseCarModel("An error occurred.", 404, "Car not found !")


@router.put("/{id}")
async def update_Car_data(id: str, req: UpdateCarModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_car = await update_car(id, req)
    if updated_car:
        return ResponseCarModel(
            updated_car,
            "Car updated successfully"
        )
    return ErrorResponseCarModel(
        "An error occurred",
        404,
        "There was an error updating the car's data.",
    )


@router.delete("/{id}", response_description="Car's data deleted")
async def delete_car_data(id: str):
    deleted_car = await delete_car(id)
    if deleted_car:
        return ResponseCarModel(
            deleted_car, "Car deleted successfully"
        )
    return ErrorResponseCarModel(
        "An error occurred", 404, f"Car with id {id} doesn't exist"
    )