from typing import Optional, List
from pydantic import BaseModel
from uuid import uuid4, UUID
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class Product(BaseModel):
    id: Optional[UUID] = uuid4()
    price: float
    name: str

class Cart(BaseModel):
    id: Optional[UUID] = uuid4()
    products: List[Product] 

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str 
    last_name: str 
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]
    cart: Cart
