from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45), index=True)
    last_name = Column(String(45), index=True)
    email = Column(String(45), unique=True, index=True)
    gender = Column(String(45), index=True)



class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    produto = Column(String(45), index=True, unique = True)

    
class User_Item(Base):
    __tablename__ = "user_items"
    owner_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    produto_id = Column(Integer, ForeignKey('items.id'), primary_key=True)
    quantidade = Column(Integer)

