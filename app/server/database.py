import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.carbuyer

car_collection = database.get_collection("car_collection")


def car_helper(car) -> dict:
    return {
        "id": str(car["_id"]),
        "name": str(car["name"]),
        "img": str(car["img"]),
        "description": str(car["description"]),
        "price": int(car["price"]),
    }

# Get all cars


async def get_cars():
    cars = []
    async for car in car_collection.find():
        cars.append(car_helper(car))
    return cars


# Add a new car
async def add_car(car_data: dict) -> dict:
    car = await car_collection.insert_one(car_data)
    new_car = await car_collection.find_one({"_id": car.inserted_id})
    return car_helper(new_car)


# Get car by id
async def get_car(id: str) -> dict:
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        return car_helper(car)


# Update a car with a matching ID
async def update_car(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        updated_car = await car_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_car:
            return True
        return False


# Delete a car by id
async def delete_car(id: str):
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        await car_collection.delete_one({"_id": ObjectId(id)})
        return True
