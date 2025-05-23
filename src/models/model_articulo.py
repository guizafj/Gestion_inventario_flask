"""
Modelo de datos para los artículos del inventario.

Define la estructura de la tabla 'articulos' en la base de datos y los campos
que representan cada artículo.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

from extensions import db  # Importa la extensión de SQLAlchemy inicializada en la app


class Articulo(db.Model):
    """
    Modelo que representa un artículo en la base de datos.

    Atributos:
        codigo_articulo (str): Código único del artículo (clave primaria).
        seccion (str): Sección a la que pertenece el artículo.
        nombre_articulo (str): Nombre descriptivo del artículo.
        precio (float): Precio del artículo.
        fecha (date): Fecha de alta del artículo.
        importado (int): Indica si el artículo es importado (1) o no (0).
        pais_origen (str): País de origen del artículo.
        foto (str): Ruta o nombre del archivo de la foto del artículo (opcional).
    """
    __tablename__ = 'articulos'  # Nombre de la tabla en la base de datos

    codigo_articulo = db.Column(db.String(10), primary_key=True, nullable=False)
    seccion = db.Column(db.String(50), nullable=False)
    nombre_articulo = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    importado = db.Column(db.Integer, nullable=False)
    pais_origen = db.Column(db.String(50), nullable=False)
    foto = db.Column(db.String(100), nullable=True)  # Campo opcional para la foto

    def __repr__(self):
        """
        Representación legible del modelo Articulo para depuración.

        :return: Cadena representando el artículo.
        """
        return (
            f"<Articulo(codigo_articulo='{self.codigo_articulo}', "
            f"nombre_articulo='{self.nombre_articulo}', precio={self.precio})>"
        )