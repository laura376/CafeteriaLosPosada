#Geografiadomain:

from pydantic import BaseModel

##################################

class Geografia(BaseModel):
    Pais: str
    Departamento: str
    Ciudad: str

##################################