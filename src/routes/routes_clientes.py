"""
Rutas relacionadas con la gestión de clientes en la aplicación Flask.

Este módulo define las rutas para listar los clientes registrados en el sistema.
Utiliza Blueprints para modularizar la aplicación y facilitar el mantenimiento.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

from flask import Blueprint, render_template, url_for
from src.models.model_cliente import Cliente

# Definición del Blueprint para las rutas de clientes
clientes_bp = Blueprint('clientes', __name__, template_folder='templates')


@clientes_bp.route('/clientes/')
def clientes_lista():
    """
    Ruta para mostrar la lista de todos los clientes.

    Recupera todos los clientes de la base de datos y los pasa al template
    'clientes.html' para su visualización.

    :return: Renderiza el template con la lista de clientes.
    """
    clientes = Cliente.query.all()
    clientes_data = [
        {
            'codigoCliente': cliente.codigoCliente,
            'empresa': cliente.empresa,
            'direccion': cliente.direccion,
            'poblacion': cliente.poblacion,
            'telefono': cliente.telefono,
            'responsable': cliente.responsable,
            'historial': cliente.historial,
        }
        for cliente in clientes
    ]
    return render_template('clientes.html', clientes=clientes_data)