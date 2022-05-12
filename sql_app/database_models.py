from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, unique=True, index=True)
    last_name = Column(String, unique=True, index=True)
    gender = Column(String, unique=True, index=True)
    #username = Column(String, unique=True, index=True)
    #full_name = Column(String, unique=True, index=True)
    
    items = relationship("Product", back_populates="owner")
    
# Mudar para Cart depois (fazer igual do projeto 1 entregado)
class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    tax = Column(Float, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="products")