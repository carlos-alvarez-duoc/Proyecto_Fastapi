"""docstring"""
# app/schemas/orden.py
from pydantic import BaseModel

class Orden(BaseModel):
    """docstring"""
    id_producto: int
    cantidad: int

    class Config:
        """docstring"""
        orm_mode = True
