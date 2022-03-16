from typing import Optional, List
from pydantic import BaseModel
from uuid import uuid4, UUID
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"

class Product(BaseModel):
    id: Optional[int]
    price: float
    name: str

class Cart(BaseModel):
    id: int
    products: List[Product] 

class User(BaseModel):
    id: Optional[int]
    first_name: str 
    last_name: str 
    gender: Gender
    cart: Optional[Cart]

class UpdateUser(BaseModel):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[Gender] = None
    cart: Optional[Cart] = None