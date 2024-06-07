"""docstring"""
# app/main.py
from fastapi import FastAPI
from app.routers import producto, despacho, orden

app = FastAPI(
    title='Ferremas',
    version='2.0'
)

app.include_router(producto.router)
app.include_router(despacho.router)
app.include_router(orden.router)
