"""
Rutas relacionadas con la gestión de artículos en la aplicación Flask.

Este módulo define las rutas para listar, buscar, editar y eliminar artículos
del inventario. Utiliza Blueprints para modularizar la aplicación y facilita
la reutilización y el mantenimiento del código.

Autor: Francisco Diaz Guiza
Fecha: 04/2025
"""

from flask import Blueprint, flash, render_template, url_for, request, redirect
from src.models.model_articulo import Articulo
from src.forms.forms import EditarArticuloForm
from extensions import db
import logging

# Definición del Blueprint para las rutas de artículos
articulos_bp = Blueprint('articulos', __name__, template_folder='templates')


@articulos_bp.route('/articulos/')
def articulos_lista():
    """
    Ruta para mostrar la lista de todos los artículos.

    Recupera todos los artículos de la base de datos y los pasa al template
    'articulos.html' para su visualización.

    :return: Renderiza el template con la lista de artículos.
    """
    articulos = Articulo.query.all()
    articulos_data = [
        {
            'codigo_articulo': articulo.codigo_articulo,
            'seccion': articulo.seccion,
            'nombre_articulo': articulo.nombre_articulo,
            'precio': articulo.precio,
            'fecha': articulo.fecha,
            'importado': articulo.importado,
            'pais_origen': articulo.pais_origen,
        }
        for articulo in articulos
    ]
    return render_template('articulos.html', articulos=articulos_data)


@articulos_bp.route('/buscar_articulo', methods=['GET', 'POST'])
def buscar_articulo():
    """
    Ruta para buscar artículos en el inventario.

    Permite buscar artículos por cualquier campo relevante usando un término
    proporcionado por el usuario. El resultado se muestra en el mismo template
    de la lista de artículos.

    :return: Renderiza el template con los artículos filtrados y el término de búsqueda.
    """
    termino = request.args.get('termino', '').strip()
    articulos = []
    if termino:
        articulos = Articulo.query.filter(
            (Articulo.codigo_articulo.ilike(f'%{termino}%')) |
            (Articulo.seccion.ilike(f'%{termino}%')) |
            (Articulo.nombre_articulo.ilike(f'%{termino}%')) |
            (Articulo.precio.ilike(f'%{termino}%')) |
            (Articulo.importado.ilike(f'%{termino}%')) |
            (Articulo.pais_origen.ilike(f'%{termino}%'))
        ).all()
    return render_template('articulos.html', articulos=articulos, termino=termino)


@articulos_bp.route('/editar_articulo/<string:codigo_articulo>', methods=['GET', 'POST'])
def editar_articulo(codigo_articulo):
    """
    Ruta para editar un artículo existente.

    Permite cargar los datos actuales del artículo en un formulario, validar
    los cambios y guardar la actualización en la base de datos.

    :param codigo_articulo: Código único del artículo a editar.
    :return: Redirige a la lista de artículos tras editar o renderiza el formulario.
    """
    articulo = Articulo.query.get_or_404(codigo_articulo)
    form = EditarArticuloForm(codigo_articulo=articulo.codigo_articulo, obj=articulo)
    if form.validate_on_submit():
        articulo.codigo_articulo = form.codigo_articulo.data
        articulo.seccion = form.seccion.data
        articulo.nombre_articulo = form.nombre_articulo.data
        articulo.precio = form.precio.data
        articulo.importado = form.importado.data
        articulo.pais_origen = form.pais_origen.data
        db.session.commit()
        flash('Artículo editado correctamente', 'success')
        return redirect(url_for('articulos.articulos_lista'))
    return render_template('editar_articulo.html', form=form, articulo=articulo)


@articulos_bp.route('/eliminar_articulo/<string:codigo_articulo>', methods=['GET', 'POST'])
def eliminar_articulo(codigo_articulo):
    """
    Ruta para eliminar un artículo del inventario.

    Muestra una página de confirmación antes de eliminar el artículo. Si la
    confirmación es enviada por POST, elimina el artículo de la base de datos.

    :param codigo_articulo: Código único del artículo a eliminar.
    :return: Redirige a la lista de artículos tras eliminar o renderiza la confirmación.
    """
    articulo = Articulo.query.get_or_404(codigo_articulo)
    if request.method == 'POST':
        try:
            logging.info(
                f"Intentando eliminar el Articulo: {articulo.nombre_articulo} "
                f"(Codigo:{articulo.codigo_articulo})"
            )
            db.session.delete(articulo)
            db.session.commit()
            flash(f'Artículo {articulo.nombre_articulo} eliminado correctamente', 'success')
            return redirect(url_for('articulos.articulos_lista'))
        except Exception as e:
            db.session.rollback()
            logging.error(
                f"Error al eliminar el Articulo: {articulo.nombre_articulo} "
                f"(Codigo: {articulo.codigo_articulo}) - Error: {str(e)}"
            )
            flash('Error al eliminar el artículo', 'danger')
    # Renderiza el template de confirmación si el método es GET
    return render_template('eliminar_articulo.html', articulo=articulo)