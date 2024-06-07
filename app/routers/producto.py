"""docstring"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/productos/")
def get_productos():
    """docstring"""
    return {"message": "Listado de productos"}

@router.get("/productos/{producto_id}")
def get_producto(producto_id: int):
    """docstring"""
    return {"message": f"Detalles del producto {producto_id}"}

@router.post("/productos/")
def create_producto():
    """docstring"""
    return {"message": "Producto creado satisfactoriamente"}

@router.put("/productos/{producto_id}")
def update_producto(producto_id: int):
    """docstring"""
    return {"message": f"Producto {producto_id} actualizado"}

@router.delete("/productos/{producto_id}")
def delete_producto(producto_id: int):
    """docstring"""
    return {"message": f"Producto {producto_id} eliminado"}
