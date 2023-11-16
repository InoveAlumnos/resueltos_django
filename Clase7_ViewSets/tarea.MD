![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---
# Tarea: Django - DRF - ViewSets, Filtros, Paginado y Serializadores.

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


### 3. Verificar que se encuentre instala la biblioteca "django-filter==2.4.0".
Revise en el archivo **requirements.txt** si se encuentra agregada, caso contrario,
debe agregarla. Luego, si está usando Docker, debe detener los contenedores y ejecutar el
siguiente comando:
**$** `docker-compose build`
En caso de no estar usando Docker basta con volver a instalar las dependencias que
se encuentran en el archivo **requirements.txt** usando pip. (Fijarse el comando para instalarlo en el archivo **Dockerfile**).


### 4. Desarrollar una única view que permita realizar una API y que responda a un CRUD del modelo WishList.
Basado en el material visto en clase, incluido en la carpeta "ejemplos_clase" desarrolle la siguiente view: **WishListViewSet** la cual debe heredar de **ModelViewSet**. Para eso debe:
  1) Crear un archivo dentro de la carpeta "api" llamado *viewsets.py* y desarrollar la view en dicho archivo.
  2) Utilizar el serializador **WishListSerializer** desarrollado en las clases anteriores.
  3) Para poder acceder a todos los endpoints correspondientes a la view en cuestión el cliente debe estar *authenticado* (Recuerde de la clase anterior que atributo debe sobreescribir).
  4) En el caso del endpoint que **lista** los objetos WishList, debe devolver el listado ordenado alfabéticamente según el campo **username** del modelo *User*.
     - A continuación se deja el link de la documentación oficial de Django donde se detalla como ordenar por un campo de otro modelo que se encuentra relacionado: [order_by](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#order-by).
     - Debe permitir filtrar aquellas listas de deseo de determinado *usuario*. Para ello el query-param a utilizar debe ser el siguiente: **username** --> Ejemplo: *{{URL}}/?username=root* Debería devolver listado de los wish-list del usuario cuyo username es *root*.
     - Debe poseer paginado. Para esto la clase a utilizar debe ser **PageNumberPagination**, recuerde que puede agregar la paginación en la configuración general de DRF o llamarla directamente a través del atributo correspondiente en la clase.
  5) Deberá crear un archivo llamado **routers.py** dentro de la carpeta "api", y, dentro del mismo crear una variable llamada *router* que deberá ser una instancia de la clase **DefaultRouter**. Luego deberá registrar su view, y, por último deberá concatenar las urls del router al *urlpatterns*. Deberá ver el ejemplo de clase para saber como realizar esta tarea. Al registar la view, deberá tener los siguientes valores:
    - **prefix**: r"wishlist"
    - **basename**: "wishlist
  **NOTA**:
    - Seguramente deberá sobreescribir el método `.get_queryset()`.
    - El response esperado debe ser por ejemplo como el siguiente:
      ```
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
                  "id": 1,
                  "favorite": true,
                  "cart": false,
                  "wished_qty": 2,
                  "bought_qty": 0,
                  "user": {
                      "id": 1,
                      "last_login": "2023-11-15T05:43:20.429832Z",
                      "is_superuser": true,
                      "username": "root",
                      "first_name": "",
                      "last_name": "",
                      "email": "root@gmail.com",
                      "is_staff": true,
                      "is_active": true,
                      "date_joined": "2023-11-15T05:43:03.878651Z",
                      "groups": [],
                      "user_permissions": []
                  },
                  "comic": {
                      "id": 2,
                      "marvel_id": 6181,
                      "title": "Ultimate Spider-Man Ultimate Collection Book 1 (Trade Paperback)",
                      "description": "Collecting the groundbreaking first year of Ultimate",
                      "price": 9.99,
                      "stock_qty": 5,
                      "picture": "http://i.annihil.us/u/prod/marvel/i/mg/6/c0/59079911f0fdb/standard_xlarge.jpg"
                  }
              }
          ]
      }
      ```


### 5. Desarrollar una API que únicamente liste todos los comics que estén en favoritos y también en el carrito de compras de un determinado usuario.
Debe crear una view llamada **UserComicAPIView** dentro de la carpeta *api*, dentro del archivo views.py.
- La clase debe heredar de la clase **ListAPIView**.
- Debe utilizar un serializador para el modelo de *Comic*.
- El listado de sus comics deben estar ordenados alfabéticamente por el campo **title**.
- Debe permitir buscar aquellos comics que contengan en el campo **title** o **description** el valor del siguiente query-param: **search**. Ejemplo --> *{{URL}}/?search=spiderman* Entonces debe devolverme todos los comics del usuario que **contengan** tanto en el *título* como en la *descripción* la palabra *spiderman*. Tener en cuenta que **no** debe ser "case sensitive" (sensible a minúsculas o mayúsculas).
  - Para esto puede utilizar la clase **SearchFilter** o trabajarlo utilizando los objetos **Q** dentro del método *.get_queryset().*
- Puede utilizar el serializador visto en clase o definido anteriormente.
- El endpoint debe ser el siguiente: **{{URL}}/e-commerce/api/comics/user/{username}/** donde "username" es un parámetro estático de la URL --> Ejemplo: *{{URL}}/e-commerce/api/comics/user/root/*.. Dicho endpoint debe ser declarado dentro del archivo *urls.py* de la carpeta "api". Recuerde establecer dentro de la función *.path()* el atributo **name** que debe ser el siguiente: **comic_list_user**.
- Debe estar paginado. Para esto la clase a utilizar debe ser **PageNumberPagination**.
**NOTA**:
  - Seguramente deberá sobreescribir el método `.get_queryset()`.
  - El response esperado debe ser por ejemplo como el siguiente:
    ```
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "marvel_id": 6181,
                "title": "Ultimate Spider-Man Ultimate Collection Book 1 (Trade Paperback)",
                "description": "Collecting the groundbreaking first year of Ultimate",
                "price": 9.99,
                "stock_qty": 5,
                "picture": "http://i.annihil.us/u/prod/marvel/i/mg/6/c0/59079911f0fdb/standard_xlarge.jpg"
            }
        ]
    }
    ```




## ¡Hora de evaluar nuestro código!
Puede evaluar que ha alcanzo los solicitado en el desafio ejecutando los tests que vienen dentro la carpeta ejercicios_practica dónde ha estando incoporando su código. Para eso debe realizar los siguientos:

1 - Abrir una consola dentro de la carpeta ejercicios_practica

2 - Lanzar el docker de ejercicios_practica (si es que está usando docker):\
**$** `docker-compose up`

3 - Abrir una nueva consola dentro de la carpeta ejercicios_practica

4 - Ingresar su consola dentro del contenedor con el siguiente comando (si es que está usando docker):\
**$** `docker exec -it modulo_4e_tp bash`

5 - Lance los tests con el siguiente comando:\
**$** `pytest -s`

---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en inove.