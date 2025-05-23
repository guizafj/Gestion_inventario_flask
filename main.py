"""
Módulo principal para la inicialización y ejecución de la aplicación Flask.

Este archivo configura la aplicación, inicializa las extensiones, registra los blueprints
y define utilidades globales para las plantillas. Además, verifica la conexión a la base
de datos antes de iniciar el servidor.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

from flask import Flask, render_template, url_for  # Flask y utilidades para plantillas y URLs
from flask_migrate import Migrate  # Extensión para migraciones de base de datos
from config import Config  # Configuración de la aplicación
from extensions import db  # Instancia global de SQLAlchemy
from src.routes.routes_generales import generales_bp  # Blueprint de rutas generales
from src.routes.routes_articulos import articulos_bp  # Blueprint de rutas de artículos
from src.routes.routes_pedidos import pedidos_bp  # Blueprint de rutas de pedidos
from src.routes.routes_clientes import clientes_bp  # Blueprint de rutas de clientes
import urllib.parse  # Utilidad estándar para manejo de URLs
from sqlalchemy import text  # Utilidad para ejecutar SQL en SQLAlchemy


def create_app():
    """
    Crea e inicializa una instancia de la aplicación Flask.

    - Configura la aplicación con los valores definidos en `Config`.
    - Inicializa las extensiones necesarias.
    - Registra los blueprints para modularizar las rutas.
    - Devuelve la instancia de la aplicación Flask.
    """
    app = Flask(__name__)  # Crea la instancia de la aplicación Flask
    app.config.from_object(Config)  # Carga la configuración desde el archivo `Config`

    initialize_extensions(app)  # Inicializa las extensiones de Flask (base de datos, migraciones)

    # Registra los blueprints para organizar las rutas de la aplicación
    app.register_blueprint(generales_bp)  # Rutas generales
    app.register_blueprint(articulos_bp, url_prefix='/articulos')  # Rutas de artículos
    app.register_blueprint(pedidos_bp, url_prefix='/pedidos')  # Rutas de pedidos
    app.register_blueprint(clientes_bp, url_prefix='/clientes')  # Rutas de clientes

    return app  # Devuelve la instancia de la aplicación


def initialize_extensions(app):
    """
    Inicializa las extensiones de Flask necesarias para la aplicación.

    - Inicializa la base de datos con SQLAlchemy.
    - Configura Flask-Migrate para manejar migraciones de la base de datos.

    :param app: Instancia de la aplicación Flask.
    """
    db.init_app(app)  # Asocia la base de datos con la aplicación Flask
    migrate = Migrate(app, db)  # Configura Flask-Migrate para manejar migraciones


# Llama a `create_app` para crear la instancia de la aplicación
app = create_app()


@app.context_processor
def utility_processor():
    """
    Define una función auxiliar para limpiar URLs en las plantillas.

    - `get_clean_url`: Elimina caracteres codificados en las URLs generadas por `url_for`.
    - Esta función estará disponible en todas las plantillas de la aplicación.

    :return: Un diccionario con la función `get_clean_url`.
    """
    def get_clean_url(endpoint, **kwargs):
        """
        Genera una URL limpia (sin caracteres codificados) para un endpoint dado.

        :param endpoint: Nombre del endpoint de Flask.
        :param kwargs: Argumentos para la función url_for.
        :return: URL decodificada.
        """
        url = url_for(endpoint, **kwargs)  # Genera la URL para el endpoint especificado
        return urllib.parse.unquote(url)  # Decodifica caracteres especiales en la URL
    return dict(get_clean_url=get_clean_url)  # Hace que la función esté disponible en las plantillas


if __name__ == '__main__':
    """
    Punto de entrada principal de la aplicación.

    - Verifica la conexión a la base de datos antes de iniciar el servidor.
    - Inicia el servidor Flask en modo de depuración.
    """
    with app.app_context():  # Crea un contexto de aplicación para acceder a las extensiones
        try:
            # Verifica la conexión a la base de datos usando un contexto explícito
            with db.engine.connect() as connection:
                connection.execute(text('SELECT 1'))  # Ejecuta una consulta simple para verificar la conexión
            print("Conexión a la base de datos exitosa.")  # Mensaje si la conexión es exitosa
        except Exception as e:
            # Captura y muestra cualquier error relacionado con la conexión a la base de datos
            print(f"Error al conectar a la base de datos: {e}")

    # Inicia el servidor Flask en modo de depuración
    app.run(debug=True)