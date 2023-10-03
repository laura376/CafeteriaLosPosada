#Clientesdomain:

from pydantic import BaseModel

##################################

class Clientes(BaseModel):
    Cliente: str
    Genero: str

##################################