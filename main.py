"""docstring"""
#from typing import Union
from fastapi import FastAPI, Body
#from pydantic import BaseModel
#from fastapi.responses import HTMLResponse

# AQUÍ SE INSTANCIA LA API
app = FastAPI(
    title= 'Ferremas',
    version= '2.0'
)

productos = [
    {
        'id': 1,
        'nombre_producto': 'Taladro',
        'categoria': 'electricas'
    }
]


"""class Producto(BaseModel):
    """"""
    name: str
    price: float
    category:str
    stock: Union[bool, None] = None
"""
@app.get("/", tags=["Inicio"])
def read_root():
    """docstring"""
    return {"Hello": "World"}

@app.get('/productos', tags=['Productos'])
def get_productos():
    """docstring"""
    return productos

# PARAMETRO DE RUTA
@app.get('/producto/{id}', tags=['Productos'])
def get_producto(id_producto: int):
    """Busca el producto por su Id"""
    for item in productos:
        if item["id"] == id_producto:
            return item
    return[]

# PARAMETROS QUERY
@app.get('/productos/', tags=['Productos'])
def get_productos_por_categoria(categoria: str):
    """Busca por categoría"""
    return categoria

@app.post('/productos', tags=['Productos'])
def create_producto(
    id_producto: int = Body(),
    nombre_producto: str = Body(),
    categoria: str = Body(),
):
    """Crear producto""" 
    productos.append({
        'id': id_producto,
        'nombre_producto': nombre_producto,
        'categoria': categoria
    })
    print(productos)
    return nombre_producto
