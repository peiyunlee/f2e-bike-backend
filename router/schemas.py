from pydantic import BaseModel, validator, EmailStr
from typing import List


class RouteRequestSchema(BaseModel):
    city: str
    cycling_length: int
    routename: str
    roadsection_start: str
    roadsection_end: str
    positions: str
    user_id: int

class UserRequestSchema(BaseModel):
    email: EmailStr
    password: str


class UserResponseSchema(UserRequestSchema):
    id: int
    email: EmailStr
    password: str

    class Config():
        orm_mode = True

class RouteResponseSchema(RouteRequestSchema):
    city: str
    cycling_length:  int
    routename: str
    roadsection_start: str
    roadsection_end: str
    positions: str
    user_id: int

    class Config():
        orm_mode = True
