from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    produto: str
    quant: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    gender : str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True

class UpdateUser(UserBase):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    #cart: Optional[Cart] = None