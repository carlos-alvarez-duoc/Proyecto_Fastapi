# app/main.py
"""docstring"""
from fastapi import FastAPI, Depends
from app.routers import producto, despacho, orden, auth, secure_routes
from app.models.database import engine, Base
from app.security import get_current_user

app = FastAPI(
    title='Ferremas',
    version='2.0'
)

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

# Incluir rutas de autenticación
app.include_router(auth.router, prefix="/auth", tags=["auth"])

# Incluir rutas seguras (que requieren autenticación)
app.include_router(secure_routes.router, prefix="/secure", tags=["secure"])

# Incluir y proteger las rutas existentes
app.include_router(producto.router, dependencies=[Depends(get_current_user)])
app.include_router(despacho.router, dependencies=[Depends(get_current_user)])
app.include_router(orden.router, dependencies=[Depends(get_current_user)])
