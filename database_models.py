# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:45:42 2022

@author: theob
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, unique=True, index=True)
    
    items = relationship("Item", back_populates="owner")
    

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    tax = Column(Float, index=True)
    #owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="items")