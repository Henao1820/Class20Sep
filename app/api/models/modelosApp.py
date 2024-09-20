from sqlalchemy import Column,Integer, String, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()

#Listado de modelos de la APLICACION
#USUARIO
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(120))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contrasena=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))

#GASTO
class Gasto(Base):
    _tablename_="Gastos"
    id=Column(Integer, primary_key=True, autoincrement=True)
    monto=Column(Integer)
    fecha=Column(Date)
    descripcion=Column(String(100))
    nombre=Column(String(120))
    restante=Column(Integer)

#CATEGORIA
class Categoria(Base):
    _tablename_="Categoria"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(80))
    descripcion=Column(String(80))
    fecha=Column(Date)
    fotoicono=Column(String(80))

#METODOS DE PAGO
class MetodoPago(Base):
    _tablename_="MetodosPago"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(80))
    fecha=Column(Date)
    descripcion=Column(String(80))
    Banco=Column(String(80))


#FACTURA
class Factura(Base):
    _tablename_="Factura"
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(120))
    fecha=Column(Date)
    monto=Column(Integer)
    descripcion=Column(String(80))
    Banco=Column(String(80))


