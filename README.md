## 📦 Gestión de Inventario con Flask

Gestion_inventario_flask es una aplicación web desarrollada con Flask que permite gestionar un inventario de artículos, clientes y pedidos. La aplicación está diseñada para ser modular, escalable y fácil de mantener, utilizando buenas prácticas de desarrollo y siguiendo la guía de estilo PEP 8.

## 🚀 Características Principales

- 🛒 Gestión de Artículos: Listar, buscar, editar y eliminar artículos del inventario.
- 👥 Gestión de Clientes: Añadir, modificar y eliminar información de clientes. (O-D)
- 📦 Gestión de Pedidos: Crear y administrar pedidos asociados a clientes y artículos. (O-D)
- 🔍 Búsqueda Avanzada: Filtrado y búsqueda eficiente de artículos y clientes. (I-I)
- 📊 Reportes: Generación de reportes de inventario y ventas. (D-P)
- 🔐 Autenticación de Usuarios: Sistema de login seguro para administradores y empleados. (O-D)
- 🎨 Interfaz Intuitiva: Diseño responsivo y amigable para facilitar la navegación.

## 🛠️ Tecnologías Utilizadas

- Backend: Flask (Python)
- Frontend: HTML5, CSS3, Bootstrap
- Base de Datos: SQLite
- ORM: SQLAlchemy
- Migraciones: Flask-Migrate
- Control de Versiones: Git

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


## Instalación

1.Clona el repositorio:

    
    git clone https://github.com/guizafj/Gestion_inventario_flask.git
    cd Gestion_inventario_flask
    

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

## 📸 Capturas de Pantalla

    Nota: Aquí se incluiran imágenes o gifs que muestren la interfaz de usuario, como el panel de administración, la gestión de artículos, clientes y pedidos, etc.


## 🤝 Contribuciones

    1. Haz un fork del repositorio.
    2. Crea una rama para tu funcionalidad (git checkout -b nueva-funcionalidad).
    3. Realiza tus cambios y haz un commit (git commit -m "Descripción de los cambios").
    4. Haz un push a tu rama (git push origin nueva-funcionalidad).
    5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

📬 Contacto

Para consultas o sugerencias:

Autor: guizafj

Correo: contacto@dguiza.dev

¡Gracias por usar Inventario Flask! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en el repositorio. 😊