from src.modelo.declarative_base import Base, engine, session
from src.modelo.modelo import Asignatura, Estudiante

# Crear las tablas en la base de datos
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Verificamos si ya existen datos
if not session.query(Asignatura).first():
    # Asignaturas de Ingeniería de Sistemas
    asig1 = Asignatura(nombre="Estructura de Datos")
    asig2 = Asignatura(nombre="Sistemas Operativos")
    asig3 = Asignatura(nombre="Redes de Computadoras")
    asig4 = Asignatura(nombre="Construcción de software")

    # Estudiantes asignados a las asignaturas
    estudiantes = [
        Estudiante(nombre="Ana Torres", asignatura=asig1),
        Estudiante(nombre="Luis Fernández", asignatura=asig1),
        Estudiante(nombre="Carlos Mendoza", asignatura=asig2),
        Estudiante(nombre="Lucía Gómez", asignatura=asig2),
        Estudiante(nombre="Elena Ruiz", asignatura=asig3),
        Estudiante(nombre="Pedro Salas", asignatura=asig3),
        Estudiante(nombre="Pariona Inga, Logan Yoshua Leonardo", asignatura=asig4),
        Estudiante(nombre="Quispe Medina, Willy Alexander", asignatura=asig4)
    ]

    # Guardar asignaturas y estudiantes
    session.add_all([asig1, asig2, asig3, asig4])
    session.add_all(estudiantes)
    session.commit()
    print("Datos insertados correctamente.")

# Consultar y mostrar estudiantes por asignatura
asignaturas = session.query(Asignatura).all()
for asignatura in asignaturas:
    print(f"\nEstudiantes de {asignatura.nombre}:")
    for estudiante in asignatura.estudiantes:
        print(f" - {estudiante.nombre}")
