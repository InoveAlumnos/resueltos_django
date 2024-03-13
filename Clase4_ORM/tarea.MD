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
1 - Abrir una consola dentro de la carpeta **ejercicios_practica**.

2 - Lanzar el docker de ejercicios_practica (si es que está usando Docker):\
**$** `docker-compose up`

__NOTA__: Sino está utizando docker deberá lanzar el servidor usando el comando runserver. Cualquier duda nos consulta

### 2. Realizar las migraciones del sistema.
Recuerde que para poder comenzar a utilizar el Django Admin, es necesario que el sistema se encuentre alineado con la base de datos. Para ello debemos realizar las migraciones de la aplicación y crear un nuevo superusuario:
1 - Abrir una nueva consola dentro de la carpeta **ejercicios_practica**.

2 - Ingresar su consola dentro del contenedor con el siguiente comando (si es que está usando Docker):\
**$** `docker exec -it modulo_3b_tp bash`

3 - Ejecutar los siguientes comandos para realizar la primera migración:\
**$** `python manage.py makemigrations`

**$** `python manage.py migrate`

4 - Ejecutar el siguiente comando para crear un super usuario:

**$** `python manage.py createsuperuser`

5 - Ingresar al django admin y verificar que todas las tablas se encuentran allí (verá las tablas vacias)

6 - Si desea puede cerrar esta terminal o dejarla abierta para el siguiente paso

### 3. Llenar su base de datos de comics
Para poder realizar esta práctica necesitará contactar con varios comics. Para evitar realizar este proceso a mano deberá ejecutar el comando creado en esta aplicación para llenar su base de datos de comics:

1 - Abrir una nueva consola dentro de la carpeta **ejercicios_practica**.

2 - Ingresar su consola dentro del contenedor con el siguiente comando (si es que está usando Docker):\
**$** `docker exec -it modulo_3b_tp bash`

3 - Lance el comando creado para llenar su DB de comics:\
**$** `python3 manage.py  get_comics`

5 - Ingresar al django admin y verificar que ahora cuenta con comics dentro de su tabla de Comics

6 - Si desea puede cerrar esta terminal o dejarla abierta para el siguiente paso

### 4. Completar la view llamada "comic_list_api_view()"
Deberá compeltar una view basada en una función llamada "comic_list_api_view()", que se encuentra en el archivo "views.py" dentro de e-commerce.

Esta view ya está configurada y el endpoint que se le adjudicó (la URL) es:\
`http://127.0.0.1:8000/e-commerce/comic-list/`.

Su vista deberá retorna un JSON con todos los comics listados en su base de datos, para ello:
1 - Deberá utilizar el ORM de Django para obtener todos los datos diponibles del modelo "Comic".
2 - De la queryset obtenida en el punto anterior deberá utilizar el método "values" para a serializar sus datos y transformarlos en una lista de diccionarios.
3 - Deberá retornar los datos con un JsonResponse utilizando el parámetro data.
4 - Una vez completado los puntos anteriors, ingresar al endpoint desde su explorador web a la URL correspondiente y verificar que los datos han sido retornado como era esperado.

## ¡Hora de evaluar nuestro código!
Puede evaluar que ha alcanzo los solicitado en el desafio ejecutando los tests que vienen dentro la carpeta ejercicios_practica dónde ha estando incoporando su código. Para eso debe realizar los siguiente:

1 - Abrir una consola dentro de la carpeta **ejercicios_practica**.

2 - Lanzar el docker de ejercicios_practica (si es que está usando Docker):\
**$** `docker-compose up`

3 - Abrir una nueva consola dentro de la carpeta **ejercicios_practica**.

4 - Ingresar su consola dentro del contenedor con el siguiente comando (si es que está usando Docker):\
**$** `docker exec -it modulo_3b_tp bash`

5 - Lance los tests con el siguiente comando:\
**$** `pytest -s`


---

## ¿Dudas?
Ante cualquier inquietud, debe referirse a los canales especificados para su trato en Inove.