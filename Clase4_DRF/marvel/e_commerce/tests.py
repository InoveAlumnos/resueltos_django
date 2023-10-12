import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Comic

# Testeamos que sea una POST request y no GET:
@pytest.mark.django_db
def test_create_comic_view_post_only():

    client = APIClient()

    endpoint_url = reverse('create_comic_view') 

    response = client.get(endpoint_url)

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

# Testeamos que la vista creada por el alumno para crear un Comic, efectivamente cree el comic
@pytest.mark.django_db
def test_create_comic_view():

    client = APIClient()

    endpoint_url = reverse('create_comic_view') 

    comic_data = {
        "marvel_id": 1010,
        "title": 'Inove',
        "stock_qty": 6,
        "description": "Mi primer JSON en Django",
        "price": 10.0,
        "picture": "https://www.django-rest-framework.org/img/logo.png"
    }

    response = client.post(endpoint_url, data=json.dumps(comic_data), content_type='application/json')

    assert response.status_code == status.HTTP_201_CREATED

    assert Comic.objects.filter(title='Inove').exists()

    response_data = response.json()
    for k in comic_data:
        assert response_data["comic"].get(k) == comic_data.get(k), f'El campo {k} no es {comic_data[k]}'

