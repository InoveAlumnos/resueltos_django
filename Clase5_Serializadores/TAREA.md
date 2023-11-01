![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---
# Tarea: Django - DRF - Vistas basadas en Clases y Serializadores

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

### 3. Crear un archivo para los serializadores
En caso de no existir debe crear un archivo dentro del directorio: *marvel/e_commerce/api/*
llamado **serializers.py**. Tenga en cuenta que acá van a ir los serializadores utilizados
para la aplicación en cuestión.

### 4. Crear un serializador para el modelo de User
Debe crear un serializador llamado **UserSerializer** dentro del archivo *serializers.py*
* Dicho serializador debe heredar de **ModelSerializer**.
* Los campos mínimos a serializar y/o deserializar deben ser: **id**, **username** e **email** del model en cuestión.

### 5. Crear una api-view basada en una clase y su url para que liste todos los Usuarios
* El nombre de la view debe ser: **UserListAPIView**.
* Debe heredar de la clase genérica **ListAPIView**.
* Utilizar el serializador creado anteriormente: **UserSerializer**.
* La url a la cual se accede debe ser la siguiente: *{{URL}}/e-commerce/api/users/list/*
  * Declarar el endpoint convenientemente en el directorio *marvel/e_commerce/api/urls.py*
  * Utiliza la función "path()" y dentro de ella, además de los parámetros conocidos debe pasar un 3er parámetro
  llamado **name** cuyo valor debe ser **user_class_list_api_view**.

### 6. Crear una api-view basada en una clase y su url para que devuelva un usuario
* Se busca crear una view que permita devolver los datos del usuario a partir de su nombre de usuario.
* El nombre de la view debe ser: **UserRetrieveAPIView**.
* Debe heredar de la clase genérica **RetrieveAPIView**.
* Utilizar el serializador creado anteriormente: **UserSerializer**.
* La url a la cual se accede debe ser la siguiente: *{{URL}}/e-commerce/api/users/<username>/*
  * <username> es el parámetro estático que debemos pasarle al momento de realizar el GET:
    * Ejemplo: *{{URL}}/e-commerce/api/users/root/*, siendo **root** el nombre de usuario.
  * Declarar el endpoint convenientemente en el directorio *marvel/e_commerce/api/urls.py*
  * Utiliza la función "path()" y dentro de ella, además de los parámetros conocidos, debe pasar un 3er parámetro
  llamado **name** cuyo valor debe ser **user_class_retrieve_api_view**.

### 7. Crear un serializador para el modelo de WishList
Debe crear un serializador llamado **WishListSerializer** dentro del archivo *serializers.py*
* Dicho serializador debe heredar de **ModelSerializer**.
* Debe poder serializar y/o deserializar *todos* los campos del modelo en cuestión.

### 8. Crear una api-view basada en una clase que permita crear un registro de WishList.
* Se busca crear una view que permita crear una lista de deseos a partir de
* El nombre de la view debe ser: **WishListAPIView**.
* Debe heredar de la clase genérica **ListCreateAPIView**.
* Utilizar el serializador creado anteriormente: **WishListSerializer**.
* La url a la cual se accede debe ser la siguiente: *{{URL}}/e-commerce/api/wish/list-create/*
  * Esta view permite los métodos HTTP: **GET** y **POST**. 
  * Declarar el endpoint convenientemente en el directorio *marvel/e_commerce/api/urls.py*
  * Utiliza la función "path()" y dentro de ella, además de los parámetros conocidos, debe pasar un 3er parámetro
  llamado **name** cuyo valor debe ser **wishlist_class_api_view**.

## ¡Hora de evaluar nuestro código!
Puede evaluar que ha alcanzo los solicitado en el desafio ejecutando los tests que vienen dentro la carpeta ejercicios_practica dónde ha estando incoporando su código. Para eso debe realizar los siguientos:

1 - Abrir una consola dentro de la carpeta ejercicios_practica

2 - Lanzar el docker de ejercicios_practica (si es que está usando docker):\
**$** `docker-compose up`

3 - Abrir una nueva consola dentro de la carpeta ejercicios_practica

4 - Ingresar su consola dentro del contenedor con el siguiente comando (si es que está usando docker):\
**$** `docker exec -it modulo_4b_tp bash`

5 - Lance los tests con el siguiente comando:\
**$** `pytest -s`


---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en Inove.