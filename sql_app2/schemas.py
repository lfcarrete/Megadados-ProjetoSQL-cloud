from typing import List, Optional

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    produto: str
    class Config:
        orm_mode = True

class User_Item(BaseModel):
    produto_id: int
    owner_id: int
    quantidade : int
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

    class Config:
        orm_mode = True