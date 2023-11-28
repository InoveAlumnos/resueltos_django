![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---
# Tarea: Django - DRF - Autenticación y Permisos

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


### 3. Realice la class-based API view para el Login del usuario.
Basado en el material visto en clase, incluido en la carpeta "ejemplos_clase" desarrolle una API view basada en clase para el login del usuario.
La misma debe incluir la creación de un Token con su asignación al correspondiente usuario.
Requisitos:
  - Su correspondiente URL debe poseer el 'name' = 'login'.


### 4. Cree los serializadores.
Cree los serializadores tanto para el UserLogin como para el Token. 
Debe crear un serializador llamado UserLoginSerializer y otro llamado TokenSerializer, ambos dentro del archivo serializers.py

    UserLoginSerializer debe heredar de Serializer.
    Debe poder serializar y/o deserializar los campos 'username' y 'password'.

    TokenSerializer debe heredar de ModelSerializer.
    Debe poder serializar y/o deserializar los campos 'user' y 'token'.


### 5 Realizar las vistas de API (class-based) para el modelo WishList, con permisos determinados.
Debe realizar las siguientes vistas de API (class-based) necesarias para realizar el CRUD de la base de datos para la entidad "WishList". A dichas views, deberá asignarle los permisos aclarados a continuación, con las urls detalladas.
  -  GetWishListAPIView (GET):
      - endpoint: 'wishlist/<int:pk>/'
      - name: 'get_wishlist_api_view'
      - Permisos: AllowAny
      - Autenticación: Sin autenticación (vacio)
  -  PostWishListAPIView (POST):
      - endpoint: 'wishlist/create/'
      - name: 'post_wishlist_api_view'
      - Permisos: IsAuthenticated
      - Autenticación: BasicAuthentication
  -  UpdateWishListAPIView (UPDATE):
      - endpoint: 'wishlist/update/<int:pk>/'
      - name: 'update_wishlist_api_view'
      - Permisos: IsAuthenticated | IsAdminUser
      - Autenticación: TokenAuthentication
  -  DeleteWishListAPIView (DELETE)
      - endpoint: 'wishlist/delete/<int:pk>/'
      - name: 'delete_wishlist_api_view'
      - Permisos: IsAdminUser
      - Autenticación: TokenAuthentication

Recuerde utilizar el serializador creado la clase anterior.


### 6. Instale Swagger para poder ver la documentación general de las APIs.
Basandose en la documentación de clase y el ejemplo brindado en "ejemplo_clase" instale Swagger para poder ver la documentación de sus APIs.


## ¡Hora de evaluar nuestro código!
Puede evaluar que ha alcanzo los solicitado en el desafio ejecutando los tests que vienen dentro la carpeta ejercicios_practica dónde ha estando incoporando su código. Para eso debe realizar los siguientos:

1 - Abrir una consola dentro de la carpeta ejercicios_practica

2 - Lanzar el docker de ejercicios_practica (si es que está usando docker):\
**$** `docker-compose up`

3 - Abrir una nueva consola dentro de la carpeta ejercicios_practica

4 - Ingresar su consola dentro del contenedor con el siguiente comando (si es que está usando docker):\
**$** `docker exec -it modulo_4c_tp bash`

5 - Lance los tests con el siguiente comando:\
**$** `pytest -s`

---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en inove.
