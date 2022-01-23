from pydantic import BaseModel, Field, validator, EmailStr
from typing import List, Optional


class RouteRequestSchema(BaseModel):
    store_id: int
    city: str
    routename: str


class StoreRequestSchema(BaseModel):
    user_id: int
    username:str


class UserBase(BaseModel):
    username: str
    email: EmailStr


class SignInRequestSchema(BaseModel):
    email: EmailStr
    password: str


class UserRequestSchema(UserBase):
    password1: str
    password2: str

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator("password1")
    def password_must_have_6_digits(cls, v):
        if len(v) < 6:
            raise ValueError("Password must have at least 6 digits")
        return v


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


class UserResponseSchema(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserSignInResponseSchema(BaseModel):
    access_token: str
    token_type: str = 'bearer'
    user_id: int
    username: str
