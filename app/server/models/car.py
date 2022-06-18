from typing import Optional

from pydantic import BaseModel, Field


class CarSchema(BaseModel):
    name: str = Field(...)
    img: str = Field(...)
    description: str = Field(...)
    price: int = Field(...)
    name_brand: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Mercedes-Benz GLA-Class GLA180 Urban Edition [2019] (A)",
                "img": "https://assets.ucars.sg/image/upload/c_fit,f_auto,w_400/v1/s3/images/17036899401655374905899_wm.png",
                "description": "1 Owner, C&C Unit, Under Warranty, Low Mileage With Fully Agent Maintain Record. Electric Seat.",
                "price": 124_800,
                "name_brand": "Mercedes-Benz"
            }
        }


class UpdateCarModel(BaseModel):
    name: Optional[str]
    img: Optional[str]
    description: Optional[str]
    price: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "name": "Mercedes-Benz GLA-Class GLA180 Urban Edition [2019] (A)",
                "img": "https://assets.ucars.sg/image/upload/c_fit,f_auto,w_400/v1/s3/images/17036899401655374905899_wm.png",
                "description": "1 Owner, C&C Unit, Under Warranty, Low Mileage With Fully Agent Maintain Record. Electric Seat.",
                "price": 124_800,
                "name_brand": "Mercedes-Benz"
            }
        }


def ResponseCarModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseCarModel(error, code, message):
    return {"error": error, "code": code, "message": message}
