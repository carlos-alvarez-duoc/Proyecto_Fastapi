"""docstring"""
# app/schemas/despacho.py
from typing import Optional
from pydantic import BaseModel


class DespachoBase(BaseModel):
    """docstring"""
    nombre: str
    direccion: str
    telefono: str

class DespachoCreate(DespachoBase):
    """docstring"""

class DespachoUpdate(DespachoBase):
    """docstring"""
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    telefono: Optional[str] = None

class Despacho(DespachoBase):
    """docstring"""
    id: int

    class Config:
        """docstring"""
        orm_mode = True

