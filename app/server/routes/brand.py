from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import *
from server.models.brand import *

router = APIRouter()


@router.post("/", response_description="Brand's data added into the database")
async def add_brand_data(brand: BrandSchema = Body(...)):
    brand = jsonable_encoder(brand)
    new_brand = await add_brand(brand)
    return ResponseBrandModel(new_brand, "brand added successfully.")


@router.get("/", response_description="Get all brands")
async def get_brands_data():
    brands = await get_brands()
    if brands:
        return ResponseBrandModel(brands, "Get all brands's data successfully")
    return ResponseBrandModel(brands, "Empty list returned !")


@router.get("/{id}", response_description="Get brand by id")
async def get_brand_data_by_id(id):
    brand = await get_brand(id)
    if brand:
        return ResponseBrandModel(brand, "Get brand by id successfully")
    return ErrorResponseBrandModel("An error occurred.", 404, "brand not found !")


@router.put("/{id}")
async def update_brand_data(id: str, req: UpdateBrandModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_brand = await update_brand(id, req)
    if updated_brand:
        return ResponseBrandModel(
            updated_brand,
            "brand updated successfully"
        )
    return ErrorResponseBrandModel(
        "An error occurred",
        404,
        "There was an error updating the brand's data.",
    )


@router.delete("/{id}", response_description="brand's data deleted")
async def delete_brand_data(id: str):
    deleted_brand = await delete_brand(id)
    if deleted_brand:
        return ResponseBrandModel(
            deleted_brand, "brand deleted successfully"
        )
    return ErrorResponseBrandModel(
        "An error occurred", 404, f"brand with id {id} doesn't exist"
    )
