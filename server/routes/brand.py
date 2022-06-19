from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import *
from server.models.brand import *

router = APIRouter()


@router.post("/")
async def add_brand_data(brand: BrandSchema = Body(...)):
    brand = jsonable_encoder(brand)
    new_brand = await add_brand(brand)
    return ResponseBrandModel(new_brand, "Brand added successfully.")


@router.get("/")
async def get_brands_data():
    brands = await get_brands()
    if brands:
        return ResponseBrandModel(brands, "Get all brands successfully")
    return ResponseBrandModel(brands, "Empty list returned !")


@router.get("/{id}")
async def get_brand_data_by_id(id):
    brand = await get_brand(id)
    if brand:
        return ResponseBrandModel(brand, "Get brand by id successfully")
    return ErrorResponseBrandModel("An error occurred.", 404, f"Brand with id {id} doesn't exist")


@router.get("/search/")
async def search_brand(query: str):
    brands = await search_brand_by_keyword(query)
    return ResponseBrandModel(brands, "Get brands by keyword")


@router.put("/{id}")
async def update_brand_data(id: str, req: UpdateBrandModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    condition = await update_brand(id, req)
    if condition:
        return ResponseBrandModel(
            condition,
            "Brand updated successfully"
        )
    return ErrorResponseBrandModel(
        "An error occurred",
        404,
        "There was an error updating the brand's data.",
    )


@router.delete("/{id}")
async def delete_brand_data(id: str):
    condition = await delete_brand(id)
    if condition:
        return ResponseBrandModel(
            condition, "Brand deleted successfully"
        )
    return ErrorResponseBrandModel(
        "An error occurred", 404, f"Brand with id {id} doesn't exist"
    )
