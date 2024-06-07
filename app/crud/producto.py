# app/crud/producto.py
from sqlalchemy.orm import Session
from app.models.producto import ProductoDB
from app.schemas.producto import Producto

def create_producto(db: Session, producto: Producto):
    db_producto = ProductoDB(
        name=producto.name,
        price=producto.price,
        category=producto.category,
        descripcion=producto.descripcion
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto
