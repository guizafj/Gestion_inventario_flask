"""
Inicialización de extensiones para la aplicación Flask.

Este módulo centraliza la creación de instancias de extensiones que serán
utilizadas en toda la aplicación, como SQLAlchemy para la base de datos y
Flask-Migrate para el manejo de migraciones.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

from flask_sqlalchemy import SQLAlchemy  # ORM para manejo de base de datos
from flask_migrate import Migrate        # Extensión para migraciones de base de datos

# Instancia global de SQLAlchemy para ser utilizada en los modelos
db = SQLAlchemy()

# Instancia global de Migrate para manejar migraciones de la base de datos
migrate = Migrate()