#Productosdomain:

from pydantic import BaseModel

##################################

class Productos(BaseModel):
    Producto: str
    TipoProducto: str
    
#################################