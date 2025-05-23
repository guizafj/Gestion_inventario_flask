"""
Modelo de datos para los pedidos del sistema.

Define la estructura de la tabla 'pedidos' en la base de datos y los campos
que representan cada pedido, así como las relaciones con clientes y artículos.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

from extensions import db  # Importa la extensión de SQLAlchemy inicializada en la app


class Pedido(db.Model):
    """
    Modelo que representa un pedido en la base de datos.

    Atributos:
        id_pedido (int): Identificador único del pedido (clave primaria, autoincremental).
        codigoCliente (str): Código del cliente que realiza el pedido (clave foránea).
        codigo_articulo (str): Código del artículo solicitado (clave foránea).
        cantidad (int): Cantidad de artículos solicitados.
        fecha_pedido (date): Fecha en que se realizó el pedido.
        cliente (Cliente): Relación con el modelo Cliente.
        articulo (Articulo): Relación con el modelo Articulo.
    """
    __tablename__ = 'pedidos'  # Nombre de la tabla en la base de datos

    id_pedido = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codigoCliente = db.Column(
        db.String(10),
        db.ForeignKey('clientes.codigoCliente'),
        nullable=False
    )  # Relación con la tabla clientes

    codigo_articulo = db.Column(
        db.String(10),
        db.ForeignKey('articulos.codigo_articulo'),
        nullable=False
    )  # Relación con la tabla articulos

    cantidad = db.Column(db.Integer, nullable=False, default=1)
    fecha_pedido = db.Column(db.Date, nullable=False)

    # Relaciones con otros modelos
    cliente = db.relationship('Cliente', backref='pedidos', lazy=True)
    articulo = db.relationship('Articulo', backref='pedidos', lazy=True)

    def __repr__(self):
        """
        Representación legible del modelo Pedido para depuración.

        :return: Cadena representando el pedido.
        """
        return (
            f"<Pedido(id_pedido={self.id_pedido}, "
            f"codigoCliente='{self.codigoCliente}', "
            f"codigo_articulo='{self.codigo_articulo}', "
            f"cantidad={self.cantidad}, fecha_pedido={self.fecha_pedido})>"
        )