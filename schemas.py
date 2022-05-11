# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:33:41 2022

@author: theob
"""

from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    

class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    full_name: str
    

class UserCreate(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    
    class Config:
        orm_mode = True
    