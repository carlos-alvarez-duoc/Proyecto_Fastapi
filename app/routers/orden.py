"""docstring"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/ordenes/")
def get_ordenes():
    """docstring"""
    return {"message": "Listado de órdenes"}

@router.get("/ordenes/{orden_id}")
def get_orden(orden_id: int):
    """docstring"""
    return {"message": f"Detalles de la orden {orden_id}"}

@router.post("/ordenes/")
def create_orden():
    """docstring"""
    return {"message": "Orden creada satisfactoriamente"}

@router.put("/ordenes/{orden_id}")
def update_orden(orden_id: int):
    """docstring"""
    return {"message": f"Orden {orden_id} actualizada"}

@router.delete("/ordenes/{orden_id}")
def delete_orden(orden_id: int):
    """docstring"""
    return {"message": f"Orden {orden_id} eliminada"}
