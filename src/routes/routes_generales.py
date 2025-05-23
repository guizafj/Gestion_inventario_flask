"""
Rutas generales y manejo de errores para la aplicación Flask.

Este módulo define las rutas principales (inicio) y los controladores para
errores comunes como 404 y 500. Utiliza Blueprints para modularizar la
aplicación y facilitar el mantenimiento.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

import logging
from flask import Blueprint, render_template, url_for
from src.models.model_articulo import Articulo

# Definición del Blueprint para las rutas generales
generales_bp = Blueprint('generales', __name__, template_folder='templates')


@generales_bp.route('/')
def index():
    """
    Ruta principal de la aplicación (página de inicio).

    Recupera todos los artículos de la base de datos y los pasa al template
    'index.html' para su visualización, junto con el total de artículos.

    :return: Renderiza el template de inicio con la lista y el total de artículos.
    """
    articulos = Articulo.query.all()
    articulos_data = [
        {
            'codigo_articulo': articulo.codigo_articulo,
            'seccion': articulo.seccion,
            'nombre_articulo': articulo.nombre_articulo,
            'precio': articulo.precio,
        }
        for articulo in articulos
    ]
    return render_template(
        'index.html',
        articulos=articulos_data,
        total_articulos=len(articulos_data)
    )


@generales_bp.app_errorhandler(404)
def pagina_no_encontrada(error):
    """
    Maneja errores 404 (página no encontrada).

    Renderiza una página de error personalizada con breadcrumbs para mejorar
    la navegación del usuario.

    :param error: Objeto de error recibido por Flask.
    :return: Renderiza el template de error con mensaje y breadcrumbs.
    """
    breadcrumbs = [
        {'name': 'Inicio', 'url': url_for('generales.index')},
        {'name': 'Error 404', 'url': '#'}
    ]
    return render_template(
        'error.html',
        mensaje="La página solicitada no existe.",
        breadcrumbs=breadcrumbs
    ), 404


@generales_bp.app_errorhandler(500)
def error_interno_servidor(error):
    """
    Maneja errores 500 (errores internos del servidor).

    Renderiza una página de error personalizada con breadcrumbs y registra el
    error en el log para facilitar la depuración.

    :param error: Objeto de error recibido por Flask.
    :return: Renderiza el template de error con mensaje y breadcrumbs.
    """
    breadcrumbs = [
        {'name': 'Inicio', 'url': url_for('generales.index')},
        {'name': 'Error 500', 'url': '#'}
    ]
    logging.error(f"Error interno del servidor: {error}")
    return render_template(
        'error.html',
        mensaje="Ha ocurrido un error inesperado. Por favor, intenta nuevamente más tarde.",
        breadcrumbs=breadcrumbs
    ), 500