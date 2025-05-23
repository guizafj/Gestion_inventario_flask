"""
Módulo de formularios para la gestión de artículos en la aplicación Flask.

Contiene clases de formularios basadas en Flask-WTF y WTForms para buscar,
editar y agregar artículos al inventario.

Autor: Francisco Diaz Guiza 
Fecha: 04/2025
"""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields import DateField

class BuscarArticuloForm(FlaskForm):
    """
    Formulario para buscar artículos en el inventario.

    Atributos:
        termino (StringField): Campo de texto para ingresar el término de búsqueda.
        submit (SubmitField): Botón para enviar el formulario.
    """
    termino = StringField(
        'Buscar',
        validators=[DataRequired(), Length(min=1, max=100)]
    )
    submit = SubmitField('Buscar')


class EditarArticuloForm(FlaskForm):
    """
    Formulario para editar los datos de un artículo existente.

    Atributos:
        codigo_articulo (StringField): Código único del artículo.
        seccion (StringField): Sección a la que pertenece el artículo.
        nombre_articulo (StringField): Nombre descriptivo del artículo.
        precio (FloatField): Precio del artículo.
        importado (IntegerField): Indica si el artículo es importado (1) o no (0).
        pais_origen (StringField): País de origen del artículo.
        submit (SubmitField): Botón para guardar los cambios.
    """
    codigo_articulo = StringField(
        'Código Artículo',
        validators=[DataRequired(), Length(min=1, max=10)]
    )
    seccion = StringField(
        'Sección',
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    nombre_articulo = StringField(
        'Nombre Artículo',
        validators=[DataRequired(), Length(min=1, max=100)]
    )
    precio = FloatField(
        'Precio',
        validators=[DataRequired()]
    )
    importado = IntegerField('Importado')
    pais_origen = StringField(
        'País de Origen',
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    submit = SubmitField('Guardar Cambios')


class AgregarArticuloForm(FlaskForm):
    """
    Formulario para agregar un nuevo artículo al inventario.

    Atributos:
        codigo_articulo (StringField): Código único del artículo.
        seccion (StringField): Sección a la que pertenece el artículo.
        nombre_articulo (StringField): Nombre descriptivo del artículo.
        precio (FloatField): Precio del artículo.
        importado (IntegerField): Indica si el artículo es importado (1) o no (0).
        pais_origen (StringField): País de origen del artículo.
        fecha (DateField): Fecha de alta del artículo (formato YYYY-MM-DD).
        submit (SubmitField): Botón para agregar el artículo.
    """
    codigo_articulo = StringField(
        'Código Artículo',
        validators=[DataRequired(), Length(min=1, max=10)]
    )
    seccion = StringField(
        'Sección',
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    nombre_articulo = StringField(
        'Nombre Artículo',
        validators=[DataRequired(), Length(min=1, max=100)]
    )
    precio = FloatField(
        'Precio',
        validators=[DataRequired()]
    )
    importado = IntegerField('Importado')
    pais_origen = StringField(
        'País de Origen',
        validators=[DataRequired(), Length(min=1, max=50)]
    )
    fecha = DateField(
        'Fecha',
        format='%Y-%m-%d',
        validators=[DataRequired()]
    )  # Uso del formato YYYY-MM-DD
    submit = SubmitField('Agregar Artículo')
