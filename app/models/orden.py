"""docstring"""
# app/models/orden.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class OrdenDB(Base):
    """docstring"""
    __tablename__ = "ordenes"
    id_orden = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_producto = Column(Integer, ForeignKey('productos.id_producto'))
    cantidad = Column(Integer)

    producto = relationship("ProductoDB")
