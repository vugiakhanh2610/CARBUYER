from pickle import FALSE
import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.carbuyer


car_collection = database.get_collection("car_collection")
brand_collection = database.get_collection("brand_collection")


# Helper function
def car_helper(car) -> dict:
    return {
        "id": str(car["_id"]),
        "name": str(car["name"]),
        "img": str(car["img"]),
        "description": str(car["description"]),
        "price": int(car["price"]),
        "name_brand": str(car["name_brand"]),
    }


def brand_helper(brand) -> dict:
    return {
        "id": str(brand["_id"]),
        "name": str(brand["name"]),
        "logo": str(brand["logo"]),
        "retailer": str(brand["retailer"]),
    }


# Car
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
async def get_car_by_id(id: str) -> dict:
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        return car_helper(car)


# Get cars by brand name
async def get_car_by_brand(name: str) -> dict:
    cars = []
    async for car in car_collection.find({"name_brand": name}):
        cars.append(car_helper(car))
    return cars


# Seach cars
async def search_car_by_keyword(query: str) -> dict:
    cars = []
    async for car in car_collection.find({"$or": [{"name": {"$regex": query, '$options': 'i'}}, {"name_brand": {"$regex": query, '$options': 'i'}}]}):
        cars.append(car_helper(car))
    return cars


# Update a car with a matching id
async def update_car(id: str, data: dict):
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
    return FALSE


# Delete a car by id
async def delete_car(id: str):
    car = await car_collection.find_one({"_id": ObjectId(id)})
    if car:
        await car_collection.delete_one({"_id": ObjectId(id)})
        return True
    return False


# Brand
# Get all brands
async def get_brands():
    brands = []
    async for brand in brand_collection.find():
        brands.append(brand_helper(brand))
    return brands


# Add a new brand
async def add_brand(brand_data: dict) -> dict:
    brand = await brand_collection.insert_one(brand_data)
    new_brand = await brand_collection.find_one({"_id": brand.inserted_id})
    return brand_helper(new_brand)


# Get brand by id
async def get_brand(id: str) -> dict:
    brand = await brand_collection.find_one({"_id": ObjectId(id)})
    if brand:
        return brand_helper(brand)


# Update a brand with a matching ID
async def update_brand(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    brand = await brand_collection.find_one({"_id": ObjectId(id)})
    if brand:
        updated_brand = await brand_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_brand:
            return True
        return False
    return FALSE


# Delete a brand by id
async def delete_brand(id: str):
    brand = await brand_collection.find_one({"_id": ObjectId(id)})
    if brand:
        await brand_collection.delete_one({"_id": ObjectId(id)})
        return True
    return FALSE


# Search brand
async def search_brand_by_keyword(query: str) -> dict:
    brands = []
    async for brand in brand_collection.find({"$or": [{"name": {"$regex": query, '$options': 'i'}}, {"retailer": {"$regex": query, '$options': 'i'}}]}):
        brands.append(brand_helper(brand))
    return brands
