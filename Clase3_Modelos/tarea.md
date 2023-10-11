1) Se debe crear un usuario que sea "superuser", para eso, puede utilizar el comando visto en clase. Recuerde que debe estar parado en el mismo directorio donde está el archivo (script) "manage.py" para poder ejecutar cualquier tipo de comando de Django.

2) Con el usuario ya creado, ahora puede acceder al "Administrador de Django". Si necesita saber cual es el endpoint, para ello dirigirse al directorio del proyecto llamado "marvel", y, dentro del mismo, existe otro directorio con el mismo nombre (marvel), dentro de éste, se encuentra varios archivos, entre ellos hay uno llamado "urls.py", dentro de este archivo encontrará el endpoint que nos dirigirá al administrador.
Luego acceda con las credenciales del superusuario y verifique que los modelos Comic y WishList estén registrados y aparezcan en el Administrador, caso contrario, deberá agregar dichos modelos. Recuerde que deberá crear las clases correspondientes dentro del archivo "admin.py" en el directorio de cada aplicación.
Por último, crear un Comic nuevo, con los siguientes valores para cada uno de estos campos:
	- marvel_id = 9999
	- title = 'Mi primer Comic'
	- stock_qty = 5
	- description = 'Esta es una descripcion de mi primer comic'
	- price = 9.99
	- picture = 'https://www.django-rest-framework.org/img/logo.png'


3) Crear un nuevo usuario que no sea superusuario ni pertezca al staff. Debe colocarle el siguiente username: "inove" (los demás campos puede completarlo a gusto). Luego deberá crear una lista de deseos con un único comic para dicho usuario. El comic es el que corresponde al campo "marvel_id"=9999, estará SÓLO en Favoritos, y las cantidades a comprar o de deseos queda a libre elección.

4) Crear una view basada en una función llamada "get_comic_api_view()", la cual deberá retornar el siguiente JSON:
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
El endpoint a utilizar es el siguiente: '{{URL}}/e-commerce/api/comic/get/'.
Recuerde que el primer parámetro que recibe una vista basada en función es "request".