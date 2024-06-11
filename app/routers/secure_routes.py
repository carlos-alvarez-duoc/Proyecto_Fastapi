"""docstring"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session # pylint: disable=unused-import
from app.models.database import SessionLocal # pylint: disable=unused-import
from app.schemas.user import User  # Importar User desde schemas.user
from .. import security

router = APIRouter()

@router.get("/secure-data", response_model=User)
async def read_secure_data(current_user: User = Depends(security.get_current_user)):
    """docstring"""
    return current_user
