from pydantic import BaseModel, Field
from datetime import date

class UsuarioDTOPeticion(BaseModel):
    nombre: str
    edad: int
    telefono: str
    correo: str
    contrasena: str
    fechaRegistro: date
    ciudad: str
    class Config: 
        orm_model=True

class UsuarioDTORespuesta():
    id: int
    nombre: str
    telefono: str
    ciudad: str
    class config:
        orm_model=True 


class GastoDTOPeticion(BaseModel):
    monto: int
    fecha: date
    descripcion: str
    nombre: str
    restante: str
    class config:
        orm_model=True

class GastoDTORespuesta():
    id: int
    monto: int
    fecha: date
    restante: str
    class Config:
        orm_model=True



class CategoriaDTOPeticion(BaseModel):
   
    nombreCategoria:str
    descripcion=str
    fecha:date
    fotoicono=str
    class config:
        orm_model=True

class CategoriaDTORespuesta():
    id: int
    nombreCategoria:str
    descripcion=str
    fecha:date
    class config:
        orm_model=True



class MetodoPagoDTOPeticion(BaseModel):
   
    nombreMetodo:str
    fecha:date
    descripcion:str
    Banco:str
    class config:
        orm_model=True

class MetodoPagoDTORespuesta():
    id: int
    nombreMetodo:str
    fecha:date
    Banco:str
    class config:
        orm_model=True



class FacturaDTOPeticion(BaseModel):
   
    nombre:str
    fecha:date
    monto:int
    descripcion:str
    Banco:str
    class config:
        orm_model=True

class FacturaDTORespuesta():
    id:int
    fecha:date
    monto:int
    descripcion:str
    class config:
        orm_model=True