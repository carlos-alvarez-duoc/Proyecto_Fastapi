"""docstring"""
# app/crud/despacho.py
from sqlalchemy.orm import Session
from app.models.despacho import Despacho
from app.schemas.despacho import DespachoCreate, DespachoUpdate

def get_despacho(db: Session, despacho_id: int):
    """docstring"""
    return db.query(Despacho).filter(Despacho.id == despacho_id).first()

def create_despacho(db: Session, despacho: DespachoCreate):
    """docstring"""
    db_despacho = Despacho(**despacho.dict())
    db.add(db_despacho)
    db.commit()
    db.refresh(db_despacho)
    return db_despacho

def update_despacho(db: Session, despacho_id: int, despacho: DespachoUpdate):
    """docstring"""
    db_despacho = db.query(Despacho).filter(Despacho.id == despacho_id).first()
    if db_despacho:
        for key, value in despacho.dict().items():
            setattr(db_despacho, key, value)
        db.commit()
        db.refresh(db_despacho)
    return db_despacho

def delete_despacho(db: Session, despacho_id: int):
    """docstring"""
    db_despacho = db.query(Despacho).filter(Despacho.id == despacho_id).first()
    if db_despacho:
        db.delete(db_despacho)
        db.commit()
    return db_despacho
