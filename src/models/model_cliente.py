"""
Modelo de datos para los clientes del sistema.

Define la estructura de la tabla 'clientes' en la base de datos y los campos
que representan cada cliente.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

from extensions import db  # Importa la extensión de SQLAlchemy inicializada en la app


class Cliente(db.Model):
    """
    Modelo que representa un cliente en la base de datos.

    Atributos:
        codigoCliente (str): Código único del cliente (clave primaria).
        empresa (str): Nombre de la empresa del cliente.
        direccion (str): Dirección del cliente.
        poblacion (str): Ciudad o población del cliente.
        telefono (str): Teléfono de contacto del cliente.
        responsable (str): Nombre del responsable de la empresa.
        historial (str): Historial o notas adicionales del cliente.
    """
    __tablename__ = 'clientes'  # Nombre de la tabla en la base de datos

    codigoCliente = db.Column(db.String(10), primary_key=True, nullable=False)
    empresa = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=True)
    poblacion = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)
    responsable = db.Column(db.String(100), nullable=True)
    historial = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        """
        Representación legible del modelo Cliente para depuración.

        :return: Cadena representando el cliente.
        """
        return (
            f"<Cliente(codigoCliente='{self.codigoCliente}', empresa='{self.empresa}')>"
        )

