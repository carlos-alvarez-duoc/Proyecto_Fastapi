"""docstring"""
# app/models/despacho.py
from sqlalchemy import Column, Integer, String
from app.models.database import Base

class Despacho(Base):
    """docstring"""
    __tablename__ = "despachos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    direccion = Column(String, index=True)
    telefono = Column(String, index=True)

