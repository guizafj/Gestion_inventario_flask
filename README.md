## Inventario Flask

Inventario Flask es una aplicación web desarrollada con Flask que permite gestionar un inventario de artículos, clientes y pedidos. La aplicación está diseñada para ser modular, escalable y fácil de mantener, utilizando buenas prácticas de desarrollo y siguiendo la guía de estilo PEP 8.

## Características

- Gestión de Artículos: Listar, buscar, editar y eliminar artículos del inventario.
- Gestión de Clientes: Listar clientes registrados en el sistema.
- Gestión de Pedidos: Listar pedidos realizados por los clientes.
- Manejo de Errores: Páginas personalizadas para errores 404 y 500.
- Modularidad: Uso de Blueprints para organizar las rutas.
- Base de Datos: Integración con MySQL utilizando SQLAlchemy como ORM.
- Migraciones: Manejo de migraciones de base de datos con Flask-Migrate.

# Requisitos

- Python 3.10 o superior.
- MySQL Server.
- Entorno virtual configurado para Python.

## Instalación

1.Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/inventario-flask.git
    cd inventario-flask
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # En Linux/Mac
    .venv\Scripts\activate     # En Windows
    ```
3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```
4. Configura las variables de entorno: Crea un archivo .env en la raíz del proyecto con las siguientes         variables:
    
    ```
    MYSQL_DB=nombre_de_tu_base_de_datos
    MYSQL_USER=tu_usuario
    MYSQL_PASSWORD=tu_contraseña
    MYSQL_HOST=localhost
    MYSQL_PORT=3306
    SECRET_KEY=tu_clave_secreta
    ```

5. Configura la base de datos:

- Crea la base de datos en MySQL.
- Ejecuta las migraciones para crear las tablas:

    ```bash
    flask db upgrade
    ```
6. Ejecuta la aplicación:

    ```bash
    python main.py
    ```
## Estructura del Proyecto

inventario_flask/
├── .venv/                     # Entorno virtual
├── config.py                  # Configuración de la aplicación
├── extensions.py              # Inicialización de extensiones (SQLAlchemy, Flask-Migrate)
├── main.py                    # Punto de entrada principal de la aplicación
├── requirements.txt           # Dependencias del proyecto
├── .env                       # Variables de entorno (no incluido en el repositorio)
├── src/
│   ├── models/                # Modelos de datos
│   │   ├── model_articulo.py  # Modelo para artículos
│   │   ├── model_cliente.py   # Modelo para clientes
│   │   └── model_pedido.py    # Modelo para pedidos
│   ├── routes/                # Rutas de la aplicación
│   │   ├── routes_articulos.py # Rutas para artículos
│   │   ├── routes_clientes.py  # Rutas para clientes
│   │   ├── routes_generales.py # Rutas generales y manejo de errores
│   │   └── routes_pedidos.py   # Rutas para pedidos
│   ├── forms/                 # Formularios de Flask-WTF
│   │   └── forms.py           # Formularios para artículos, clientes y pedidos
│   └── templates/             # Plantillas HTML
│       ├── index.html         # Página de inicio
│       ├── articulos.html     # Página para listar artículos
│       ├── clientes.html      # Página para listar clientes
│       ├── pedidos.html       # Página para listar pedidos
│       └── error.html         # Página de error personalizada
└── migrations/                # Archivos de migración de base de datos

## Tecnologías Utilizadas

- Flask: Framework web principal.
- SQLAlchemy: ORM para la base de datos.
- Flask-Migrate: Manejo de migraciones de base de datos.
- MySQL: Base de datos relacional.
- Flask-WTF: Manejo de formularios.

## Contribuciones

    1. Haz un fork del repositorio.
    2. Crea una rama para tu funcionalidad (git checkout -b nueva-funcionalidad).
    3. Realiza tus cambios y haz un commit (git commit -m "Descripción de los cambios").
    4. Haz un push a tu rama (git push origin nueva-funcionalidad).
    5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

¡Gracias por usar Inventario Flask! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en el repositorio. 😊