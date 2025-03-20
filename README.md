# Proyecto Flask Login

## Descripción
Este proyecto implementa un sistema de autenticación de usuarios con Flask-Login. Los usuarios deben iniciar sesión para acceder a secciones protegidas de la aplicación. El diseño está optimizado con Tailwind CSS y Flowbite para una interfaz moderna y receptiva.

## Tecnologías Utilizadas
blinker==1.7.0
click==8.1.7
colorama==0.4.6
dnspython==2.5.0
email-validator==2.1.0.post1
Flask==3.0.1
Flask-Login==0.6.2
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.1
greenlet==3.0.3
idna==3.6
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.4
PyMySQL==1.1.0
SQLAlchemy==2.0.27
typing_extensions==4.9.0
Werkzeug==3.0.1
WTForms==3.1.2

## Instalación y Configuración
1. Clona este repositorio:

2. Entra en la carpeta del proyecto:

3. Crea y activa un entorno virtual:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
4. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

## Ejecución
1. Configura las variables de entorno necesarias (por ejemplo, la clave secreta y la base de datos en un archivo `.env`).
2. Ejecuta la aplicación:
3. Accede a la aplicación en `http://127.0.0.1:5000`.

## Funcionalidades
- **Inicio de sesión seguro** con Flask-Login.
- **Protección de rutas**, redirigiendo a los usuarios no autenticados a la página de login.
- **Diseño atractivo y responsivo** con Tailwind CSS y Flowbite.
- **Base de datos con SQLAlchemy**, compatible con MySQL.



Autor: Jose Israel Cervera Burrola 

