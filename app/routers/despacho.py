"""docstring"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/despachos/")
def get_despachos():
    """docstring"""
    return {"message": "Listado de despachos"}

@router.get("/despachos/{despacho_id}")
def get_despacho(despacho_id: int):
    """docstring"""
    return {"message": f"Detalles del despacho {despacho_id}"}

@router.post("/despachos/")
def create_despacho():
    """docstring"""
    return {"message": "Despacho creado satisfactoriamente"}

@router.put("/despachos/{despacho_id}")
def update_despacho(despacho_id: int):
    """docstring"""
    return {"message": f"Despacho {despacho_id} actualizado"}

@router.delete("/despachos/{despacho_id}")
def delete_despacho(despacho_id: int):
    """docstring"""
    return {"message": f"Despacho {despacho_id} eliminado"}
