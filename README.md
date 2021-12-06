
 
# TECNOINVENTARIOS
https://github.com/haldanas/tecnoInventario/tree/developer

### setting environment variables
First install python3 , pip, and virtualenv. Run:
folder is a virtual envirotment por libs by python3
`virtualenv venv folder`
or
`python -m venv .env`
after
`pip install -r requeriments.txt`

check the django settings: 

`python3 manage.py migrate`.
`python3 manage.py makemigrations`.

run server
`python3 manage.py runserver`.

for add a new app
`django-admin startapp [name app]`.

Glosario
ORM: Object-relational mapping. Es el encargado de permitir
el acceso y control de una base de datos relacional a través de
una abstracción a clases y objetos.

Templates: Archivos HTML que permiten la inclusión y ejecución
de lógica especial para la presentación de datos.

Modelo: Parte de un proyecto de Django que se encarga de estructurar
las tablas y propiedades de la base de datos a través de clases de Python.

Vista: Parte de un proyecto de Django que se encarga de la
lógica de negocio y es la conexión entre el template y el modelo.

App: Conjunto de código que se encarga de resolver una parte
muy específica del proyecto, contiene sus modelos, vistas, urls, etc.

Patrón de diseño: Solución común a un problema particular.

