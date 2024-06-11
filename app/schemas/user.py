"""docstring"""
from pydantic import BaseModel

class UserBase(BaseModel):
    """docstring"""
    username: str
    email: str

class UserCreate(UserBase):
    """docstring"""
    password: str

class User(UserBase):
    """docstring"""
    id: int

    class Config:
        """docstring"""
        orm_mode = True
