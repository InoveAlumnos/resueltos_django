![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---
# Tarea: Django - Modelos y Administrador

Al realizar esta tarea pondremos en práctica los conocimientos adquiridos en clase.
Una vez finalizada, el alumno debe subir el enlace a su repositorio "forkeado" el foro de tarea correspondiente -NO SE ADMITE LA DEVOLUCIÓN POR OTRO CANAL SALVO SE ESPECIFIQUE LO CONTRARIO- 

Recuerde que no debe subir la base de datos al sistema, para ello se encuentra el archivo .gitignore que especifica los archivos y directorios omitidos.

---

### 1. Utilizar el proyecto de "Marvel" visto en clase.
Inicializar el contenedor de docker, compilar la imagen del repositorio con:
**$** `docker-compose up`

### 2. Realizar las migraciones del sistema.
Recuerde que para poder comenzar a utilizar el Django Admin, es necesario que el sistema se encuentre alineado con la base de datos. Para ello debemos realizar las migraciones de la aplicación y crear un nuevo superusuario.
Los comandos necesarios se encuentran detallados en el archivo README.md

### 3. Personalice el administrador de Django.
Familiarícese con la aplicación, personalice el administrador de Django utilizando los atributos de admin.py.

### 4. Genere una nueva entidad en models.py 
Diseñe una nueva entidad en models.py, llamada "WishList" y agréguele los campos (columnas en la tabla resultante):
* id
* user (Este campo debe ser un Foreign Key relacionando con el modelo **User** que ofrece Django).
* comic (Este campo debe ser un Foreign Key relacionando con el Modelo **Comic**).
* favorite
* cart
* wished_qty
* bought_qty 

Debe basarse en el siguiente diseño de entidades:

![Entidades](/entidades.png)

Tip:
El atributo "comic" del modelo es un campo de tipo FK, para poder implementarlo utilizaremos:

```
comic = models.ForeignKey(
    Comic,
    verbose_name='Comic',
    on_delete=models.CASCADE,
    default=1,
    blank=True
)
```
Cuyos argumentos son:

* Comic --> El nombre de la clase (modelo) que hace referencia a la entidad "comic".
* on_delete=models.CASCADE --> Hace que al borrar un registro, se borren sus relacionados.
    - Links de Interés:
      - [Documentación de Django](https://docs.djangoproject.com/en/3.2/ref/models/fields/#arguments)
      - [Stack Overflow](https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models)
* default --> Valor por defecto si no se le agrega ninguno.
* blank --> Permite que se inserte un registro con este campo vacío.

### 5. Realizar las migraciones del sistema.
Recuerde hacer el `makekigartions` y el `migrate`.

### 6. Nueva entidad en Django Admin.
Haga que la nueva entidad aparezca en el administrador de Django, recuerde realizar las migraciones previamente y lo trabajado en admin.py

### 7. Completar la view llamada "get_comic_api_view()"
Deberá compeltar una view basada en una función llamada "get_comic_api_view()", que se encuentra en el archivo "views.py" dentro de e-commerce. Esta view ya está configurada y el endpoint que se le adjudico (la URL) es `get-comic/`.

Lo que deberá hacer que completar esa función la cual deberá retornar el siguiente JSON:
```
    {
        "id": 1,
        "marvel_comic": "1010",
        "title": "Inove",
        "stock_qty": 6,
        "description": "Mi primer JSON en Django",
        "price": 10.0,
        "picture": "https://www.django-rest-framework.org/img/logo.png"
    }
```

Recuerde que para que Django pueda renderizar (el endpoint retornar) un JSON, deberá retornar los datos con un JsonResponse.

## ¡Hora de evaluar nuestro código!
Puede evaluar que ha alcanzo los solicitado en el desafio ejecutando los tests que vienen dentro la carpeta ejercicios_practica dónde ha estando incoporando su código. Para eso debe realizar los siguientos:

1 - Abrir una consola dentro de la carpeta ejercicios_practica

2 - Lanzar el docker de ejercicios_practica (si es que está usando docker):\
**$** `docker-compose up`

3 - Abrir una nueva consola dentro de la carpeta ejercicios_practica

4 - Ingresar su consola dentro del contenedor con el siguiente comando (si es que está usando docker):\
**$** `docker exec -it modulo_3_tp bash`

5 - Lance los tests con el siguiente comando:\
**$** `pytest -s`


---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en Inove.