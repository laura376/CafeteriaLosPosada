#GTransaccional domain:

from pydantic import BaseModel

##################################

class Transaccional(BaseModel):
    Factura: str
    TipoFactura: str

##################################