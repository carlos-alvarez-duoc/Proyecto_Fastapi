# app/models/producto.py
from sqlalchemy import Column, Integer, String, Float, Text
from .database import Base

class ProductoDB(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    price = Column(Float)
    category = Column(String)
    descripcion = Column(Text, nullable=True)
