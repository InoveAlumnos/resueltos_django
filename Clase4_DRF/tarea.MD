![Inove banner](/inove.jpg)
Inove Escuela de Código\
info@inove.com.ar\
Web: [Inove](http://inove.com.ar)

---
# Tarea: Django - Django REST FRAMEWORK 1

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

### 3. Familiarícese con el proyecto "marvel".
Recorra los directorios, incluso el directorio "tools" que sirve como muestra del proceso de consumo de datos en el servicio de Marvel. Recuerde que el objetivo de consumir estos datos es para llenar la base de datos y llenar nuestro stock de comics.
También vea cómo se realizaron las APIs de la aplicación e_commerce, los archivos relacionados, librerías y urls. 

### 4. Instale Django REST Framework (DRF) en "ejercicios_practica".
En ejercicios_practica se encuentra el proyecto avanzado hasta la clase 3, debe incluir los cambios necesarios para incluir DRF en el proyecto (declararlos en settings.py etc;) puede guiarse por el ejemplo de clase para ello.

### 5. Agregue la carpeta "api" a su aplicación e_commerce.
Agregue la carpeta "api" a su aplicación e_commerce al igual que en el ejemplo de clase, y desarrolle las siguientes 3 vistas de API con decoradores (las cuales deben ser de tipo GET y POST):

- Una para LISTAR comics (Al asignarle una URL en el campo name nombrela "comic_list_api_view")

- Una para OBTENER un comic por "id" (Al asignarle una URL en el campo name nombrela "comic_retrieve_api_view")

- Una para CREAR un comic (Al asignarle una URL en el campo name nombrela "comic_create_api_view")


### 6. Cree una API view que liste comics filtrando por precio.
Desarrolle una vista de api la cual liste comics filtrandolos de modo que muestre solamente aquellos con precio mayor o igual a 5.00.
Nombrela "comic_list_filtered_api_view".


### 7. Incluya alguna API view creada por usted.
Imagine alguna funcionalidad adicional que le gustaría proveer al usuario y desarrolle su propia vista de api a dichos fines.
Por ejemplo, listar determinados comics en virtud de algún filtro.

---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en Inove.