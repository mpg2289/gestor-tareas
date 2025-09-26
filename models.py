import db
from sqlalchemy import Column, Integer, String, Boolean
from flask import Flask, render_template, request, redirect,url_for

class Tarea(db.Base):
    __tablename__="tarea"
    id = Column(Integer, primary_key=True)#Identificador unico de cada tarea (no puede haber dos tareas con el mismo id,
    #por eso es primary key
    contenido = Column(String(200), nullable=False)#Contenido de la tarea, un maximo de 200 caracteres
    hecha = Column(Boolean)#Booleano que indica si una tarea ha sido realizada o no
    categoria = Column(String(200), nullable=False)
    fechaLimite = Column(Integer, nullable=False)


    def __init__(self,contenido, hecha, categoria, fechaLimite):
        #Recordamos que el id no es necesario crearlo manualmente, lo añade la base de datos automaticamente
        self.contenido = contenido
        self.hecha = hecha
        self.categoria= categoria
        self.fechaLimite = fechaLimite




    def __repr__(self):
        return "Tarea {}: {} ({}) {} {}". format(self.id, self.contenido, self.hecha, self.categoria, self.fechaLimite)

    def __str__(self):
        return "Tarea {}: {} ({}) {} {}". format(self.id, self.contenido, self.hecha, self.categoria, self.fechaLimite)