from typing import Optional

from pydantic import BaseModel, Field


class BrandSchema(BaseModel):
    name: str = Field(...)
    logo: str = Field(...)
    retailer: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Mercedes-Benz",
                "logo": "https://ucars-bucket.s3-ap-southeast-1.amazonaws.com/images/17766641601649743680410.PNG",
                "retailer": "Cycle & Carriage Industries"
            }
        }


class UpdateBrandModel(BaseModel):
    name: Optional[str]
    logo: Optional[str]
    retailer: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Mercedes-Benz",
                "logo": "https://ucars-bucket.s3-ap-southeast-1.amazonaws.com/images/17766641601649743680410.PNG",
                "retailer": "Cycle & Carriage Industries"
            }
        }


def ResponseBrandModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseBrandModel(error, code, message):
    return {"error": error, "code": code, "message": message}
