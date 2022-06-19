from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import *
from server.models.car import *

router = APIRouter()


@router.post("/car")
async def add_car_data(car: CarSchema = Body(...)):
    car = jsonable_encoder(car)
    new_car = await add_car(car)
    return ResponseCarModel(new_car, "Car added successfully.")


@router.get("/cars")
async def get_cars_data():
    cars = await get_cars()
    if cars:
        return ResponseCarModel(cars, "Get all cars successfully")
    return ResponseCarModel(cars, "Empty list returned !")


@router.get("/car/{id}")
async def get_car_data_by_id(id):
    car = await get_car_by_id(id)
    if car:
        return ResponseCarModel(car, "Get car by id successfully")
    return ErrorResponseCarModel("An error occurred.", 404, f"Car with id {id} doesn't exist")


@router.get("/cars/{name}")
async def get_car_data_by_brand(name):
    cars = await get_car_by_brand(name)
    if cars:
        return ResponseCarModel(cars, "Get all cars by brand's name successfully")
    return ResponseCarModel(cars, "Empty list returned !")


@router.get("/car/search/")
async def search_car(query: str):
    cars = await search_car_by_keyword(query)
    return ResponseCarModel(cars, "Get cars by keyword")


@router.put("/car/{id}")
async def update_Car_data(id: str, req: UpdateCarModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    condition = await update_car(id, req)
    if condition:
        return ResponseCarModel(
            condition,
            "Car updated successfully"
        )
    return ErrorResponseCarModel(
        "An error occurred",
        404,
        "There was an error updating the car's data.",
    )


@router.delete("/car/{id}")
async def delete_car_data(id: str):
    condition = await delete_car(id)
    if condition:
        return ResponseCarModel(
            condition, "Car deleted successfully"
        )
    return ErrorResponseCarModel(
        "An error occurred", 404, f"Car with id {id} doesn't exist"
    )
