from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    gender = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
    
class Carrinho(Base):
    __tablename__ = "carrinho"
    
    id_user = Column(Integer, ForeignKey("users.id"), primary_key=True, index=True)
    id_produto = Column(Integer, ForeignKey("items.id"), primary_key=True, index=True)

    quantidade = Column(Integer)
    
    #cart = relationship("User", "Item", back_populates=)