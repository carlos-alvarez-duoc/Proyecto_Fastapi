"""docstring"""
# app/crud/orden.py
from sqlalchemy.orm import Session
from app.models.orden import OrdenDB
from app.schemas.orden import Orden

def create_orden(db: Session, orden: Orden):
    """docstring"""
    db_orden = OrdenDB(
        id_producto=orden.id_producto,
        cantidad=orden.cantidad
    )
    db.add(db_orden)
    db.commit()
    db.refresh(db_orden)
    return db_orden
