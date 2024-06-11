"""docstring"""
from fastapi import APIRouter, Depends
from app.security import get_current_user
from app.schemas.user import User

router = APIRouter()

@router.get("/productos/", dependencies=[Depends(get_current_user)])
def get_productos(current_user: User = Depends(get_current_user)):
    """docstring"""
    return {"message": "Listado de productos"}

@router.get("/productos/{producto_id}", dependencies=[Depends(get_current_user)])
def get_producto(producto_id: int, current_user: User = Depends(get_current_user)):
    """docstring"""
    return {"message": f"Detalles del producto {producto_id}"}

@router.post("/productos/", dependencies=[Depends(get_current_user)])
def create_producto(current_user: User = Depends(get_current_user)):
    """docstring"""
    return {"message": "Producto creado satisfactoriamente"}

@router.put("/productos/{producto_id}", dependencies=[Depends(get_current_user)])
def update_producto(producto_id: int, current_user: User = Depends(get_current_user)):
    """docstring"""
    return {"message": f"Producto {producto_id} actualizado"}

@router.delete("/productos/{producto_id}", dependencies=[Depends(get_current_user)])
def delete_producto(producto_id: int, current_user: User = Depends(get_current_user)):
    """docstring"""
    return {"message": f"Producto {producto_id} eliminado"}
