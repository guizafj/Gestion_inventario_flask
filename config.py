"""
Configuración principal de la aplicación Flask.

Este módulo carga las variables de entorno necesarias para la conexión a la base de datos,
configura SQLAlchemy y proporciona utilidades para el manejo de un pool de conexiones
MySQL utilizando mysql-connector-python.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

from dotenv import load_dotenv
import os
from mysql.connector import pooling, Error

class Config:
    """
    Clase de configuración para la aplicación Flask.

    - Carga variables de entorno para la base de datos y la clave secreta.
    - Configura la URI de SQLAlchemy.
    - Proporciona métodos para obtener y liberar conexiones usando un pool.
    """
    load_dotenv()  # Carga las variables de entorno desde un archivo .env

    # Variables de entorno para la base de datos
    DATABASE = os.getenv('MYSQL_DB')  # Nombre de la base de datos
    USERNAME = os.getenv('MYSQL_USER')  # Usuario de la base de datos
    PASSWORD = os.getenv('MYSQL_PASSWORD')  # Contraseña del usuario
    DB_PORT = os.getenv('MYSQL_PORT', 3306)  # Puerto de la base de datos (por defecto 3306)
    HOST = os.getenv('MYSQL_HOST', 'localhost')  # Host de la base de datos

    # Clave secreta para la aplicación Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'defaultsecretkey')

    # Configuración de SQLAlchemy para Flask
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{DB_PORT}/{DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de modificaciones

    # Configuración del pool de conexiones MySQL
    POOL_SIZE = int(os.getenv('POOL_SIZE', 5))  # Tamaño del pool de conexiones
    POOL_NAME = os.getenv('POOL_NAME', 'default_pool')  # Nombre del pool
    pool = None  # Instancia del pool de conexiones

    @classmethod
    def obtener_pool(cls):
        """
        Crea un pool de conexiones a la base de datos si no existe.

        :return: Instancia del pool de conexiones.
        :raises Exception: Si ocurre un error al crear el pool.
        """
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                )
                return cls.pool
            except Error as e:
                raise Exception(f'Error al obtener el pool de conexiones: {e}')
        return cls.pool

    @classmethod
    def obtener_conexion(cls):
        """
        Obtiene una conexión del pool de conexiones.

        :return: Conexión activa a la base de datos.
        """
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        """
        Libera una conexión del pool de conexiones.

        :param conexion: Conexión a liberar.
        """
        if conexion.is_connected():
            conexion.close()


if __name__ == '__main__':
    # Prueba de la clase Config
    try:
        config = Config()
        pool = config.obtener_pool()
        print(f'Pool de conexiones creado: {pool}')

        conexion = config.obtener_conexion()
        print(f'Conexión obtenida: {conexion}')

        config.liberar_conexion(conexion)
        print('Conexión liberada')
    except Exception as e:
        print(f'Error: {e}')

