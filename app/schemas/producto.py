"""docstring"""
# app/schemas/producto.py
from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    """docstring"""
    name: str
    price: float
    category: str
    descripcion: Optional[str] = None

    class Config:
        """docstring"""
        orm_mode = True
