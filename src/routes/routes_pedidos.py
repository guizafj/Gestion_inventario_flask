"""
Rutas relacionadas con la gestión de pedidos en la aplicación Flask.

Este módulo define las rutas para listar los pedidos registrados en el sistema.
Utiliza Blueprints para modularizar la aplicación y facilitar el mantenimiento.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

from flask import Blueprint, render_template, url_for
from src.models.model_pedido import Pedido

# Definición del Blueprint para las rutas de pedidos
pedidos_bp = Blueprint('pedidos', __name__, template_folder='templates')


@pedidos_bp.route('/pedidos/')
def pedidos_lista():
    """
    Ruta para mostrar la lista de todos los pedidos.

    Recupera todos los pedidos de la base de datos y los pasa al template
    'pedidos.html' para su visualización.

    :return: Renderiza el template con la lista de pedidos.
    """
    pedidos = Pedido.query.all()
    pedidos_data = [
        {
            'id_pedido': pedido.id_pedido,
            'codigoCliente': pedido.codigoCliente,
            'codigo_articulo': pedido.codigo_articulo,
            'cantidad': pedido.cantidad,
            'fecha_pedido': pedido.fecha_pedido,
        }
        for pedido in pedidos
    ]
    return render_template('pedidos.html', pedidos=pedidos_data)