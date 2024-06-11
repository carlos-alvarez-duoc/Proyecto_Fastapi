"""docstring"""
# app/schemas/token.py
from pydantic import BaseModel

class Token(BaseModel):
    """docstring"""
    access_token: str
    token_type: str
