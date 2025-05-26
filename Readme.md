# ORM: Asignatura - Estudiante

Este proyecto implementa un ejemplo de relación **uno a muchos** usando **SQLAlchemy** entre las entidades `Asignatura` y `Estudiante`. Una asignatura puede tener muchos estudiantes matriculados.

## 👥 Integrantes

| Nro. | Integrantes                         |
|------|-------------------------------------|
| 1    | Pariona Inga, Logan Yoshua Leonardo |
| 2    | Quispe Medina, Willy Alexander      |

## ✨ Ficha técnica

- 🐍 Lenguaje: Python 3.11+
- 🧱 ORM: SQLAlchemy
- 🛢️ Base de datos: SQLite
- 📁 Arquitectura por módulos (`logica`, `vista`, `tests`)
- 📦 Entorno virtual con `venv`


## 🛠️ Instalación y ejecución

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/cs-orm-one-many.git
cd cs-orm-one-many
```
2. Crea y activa un entorno virtual:
```bash
python -m venv .venv

.venv\Scripts\activate
```
3. Instala dependencias:
```bash
pip install -r requirements.txt
```
4. Ejecuta el script principal:
```bash
python src/vista/app_v2.py
```