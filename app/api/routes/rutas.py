from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends
from app.api.schemas.DTO import UsuarioDTOPeticion, UsuarioDTORespuesta, GastoDTOPeticion, GastoDTORespuesta, CategoriaDTOPeticion, CategoriaDTORespuesta, MetodoPagoDTOPeticion, MetodoPagoDTORespuesta, MetodoPagoDTORespuesta, FacturaDTOPeticion, FacturaDTORespuesta
from app.api.models.modelosApp import Usuario
from app.database.configuration import sessionLocal, engine

#para que un api funcione debe tener un archivo enrutador
rutas=APIRouter() #ENDPOINTS...


#Crear una funcion para establercer cuando yo quiera y necesite
#conexion hacia la base de datos

def getDatabase():
    basedatos=sessionLocal()
    try:
        yield basedatos
    except Exception as error: #se corto el dedo
        basedatos.rollback()
        raise error
    finally:
        basedatos.close()


#programacion de cada uno de nuestros servicios
#QUE OFRECERA NUESTRA API


#Servicio web: Son OPERACIONES en la Base de datos--> Modelos.
#Crud, guardar:post, buscar:get, modificar:put y eliminar:Delete, DATOS de un modelo.
#Buscar todos los usuarios cuantos gastan, cuanto ganan etc etc.......


#REGISTRANDO O GUARDANDO UN USUARIO EN LA BD
@rutas.post("/Usuarios")
def guardarUsuario(datosPeticion: UsuarioDTOPeticion, db:Session=Depends(getDatabase)):
    try: 
        usuario=Usuario(
            nombre=datosPeticion.nombre,
            edad=datosPeticion.edad,
            telefono=datosPeticion.telefono,
            correo=datosPeticion.correo,
            fechaRegistro=datosPeticion.fechaRegistro,
            ciudad=datosPeticion.ciudad

        )
        
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    except Exception as error:
        db.rollback()
        return HTTPException()




        
@rutas.get("/Usuarios")
def buscarUsuario():
    pass





