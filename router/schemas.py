from pydantic import BaseModel, validator, EmailStr
from typing import List


class RouteRequestSchema(BaseModel):
    store_id: int
    city: str
    routename: str

class StoreRequestSchema(BaseModel):
    user_id: int


class UserRequestSchema(BaseModel):
    email: EmailStr
    password: str


class RouteResponseSchema(RouteRequestSchema):
    store_id: int
    city: str
    routename: str

    class Config():
        orm_mode = True


class StoreResponseSchema(StoreRequestSchema):
    id: int
    user_id: int
    route_items: List[RouteResponseSchema]

    class Config():
        orm_mode = True

class StoreResponseWithRouteSchema(StoreRequestSchema):
    user_id: int
    route_items: List[RouteResponseSchema]

    class Config():
        orm_mode = True

class UserResponseSchema(UserRequestSchema):
    id: int
    email: EmailStr
    password: str

    class Config():
        orm_mode = True
