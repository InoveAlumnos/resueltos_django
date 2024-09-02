import json
import pytest
from pytest_fixtures import *
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Comic

# Testeamos que sea una POST request y no GET:
@pytest.mark.django_db
def test_comic_create_api_view_post_only(client):
    endpoint_url = reverse('comic_create_api_view') 

    response = client.get(endpoint_url)

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED, f'Método HTTP incorrecto. Debe ser una request de tipo "POST".'

# Testeamos que la vista creada por el alumno para crear un Comic, efectivamente cree el comic
@pytest.mark.django_db
def test_comic_create_api_view(client):

    endpoint_url = reverse('comic_create_api_view') 

    comic_data = {
        "marvel_id": 1010,
        "title": 'Inove',
        "stock_qty": 6,
        "description": "Mi primer JSON en Django",
        "price": 10.0,
        "picture": "https://www.django-rest-framework.org/img/logo.png"
    }

    response = client.post(endpoint_url, data=json.dumps(comic_data), content_type='application/json')

    assert response.status_code != 404, f'Endpoint no encontrado'

    assert Comic.objects.filter(title='Inove').exists(), f'Comic no encontrado.'

    response_data = response.json()
    
    for k in comic_data:
        assert response_data.get(k) == comic_data.get(k), f'El campo {k} no coincide con el valor esperado: {comic_data[k]}.'


# Testeamos que la vista creada por el alumno permita listar los comics
@pytest.mark.django_db
def test_comic_list_api_view(client, create_list_of_comic):

    create_list_of_comic()
    
    endpoint_url = reverse('comic_list_api_view') 

    response = client.get(endpoint_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data != [], 'Se esperaba una lista con comics, al contrario, se obtuvo una lista vacía.'



# Testeamos que la vista creada por el alumno permita obtener un comic por id
@pytest.mark.django_db
def test_comic_retrieve_api_view(client, create_list_of_comic):
    create_list_of_comic()
    
    comic_id = Comic.objects.first().id

    endpoint_url = reverse('comic_retrieve_api_view') 

    response = client.get(f"{endpoint_url}?id={comic_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get('id') == comic_id, f"El ID del comic obtenido debería ser {comic_id}."


# Testeamos que la vista creada por el alumno permita listar los comics con precio superior a 5.00
@pytest.mark.django_db
def test_comic_list_filtered_api_view(client, create_list_of_comic):
    create_list_of_comic()
    
    endpoint_url = reverse('comic_list_filtered_api_view') 

    response = client.get(endpoint_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data != [], 'Se esperaba una lista con comics, al contrario, se obtuvo una lista vacía.'
    for comic in response.data:
        assert comic["price"] > 5.00, f'Se esperaba que el queryset contuviera comics filtrados por precio superior a 5.00, el presente comic posee un precio de {comic["price"]}.'
