# src/logica/modelos.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.modelo.declarative_base import Base

class Asignatura(Base):
    __tablename__ = 'asignaturas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    estudiantes = relationship("Estudiante", back_populates="asignatura")

class Estudiante(Base):
    __tablename__ = 'estudiantes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    asignatura_id = Column(Integer, ForeignKey('asignaturas.id'))
    asignatura = relationship("Asignatura", back_populates="estudiantes")
