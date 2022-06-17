import motor.motor_asyncio

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.carbuyer

car = database.get_collection("car")


def car_helper(car) -> dict:
    return {
        "id": str(car["_id"]),
        "name": car["name"],
        "img": car["img"],
        "description": car["description"],
        "price": car["price"],
    }
