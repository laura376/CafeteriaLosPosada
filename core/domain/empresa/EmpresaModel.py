#Empresadomain:

from pydantic import BaseModel

##################################

class Empresa(BaseModel):
    Cafeteria: str
    Sede: str
    Vendedor: str

##################################