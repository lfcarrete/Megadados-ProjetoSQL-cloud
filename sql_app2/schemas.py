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