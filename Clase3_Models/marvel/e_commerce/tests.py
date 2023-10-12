import pytest
from pytest_fixtures import *

from django.urls import reverse
from rest_framework import status

from e_commerce import models


@pytest.mark.django_db
def test_modelo_WishList(create_user, create_comic):
    assert hasattr(models, 'WishList'), "El modelo WishList no está definido en models"
    
    # crear un comic para el ensayo de WishList
    comic = create_comic()
    
    # crear un usuario para el ensayo de WishList
    user = create_user()
    
    # Ensayar si WhishList fue generada correctamente
    models.WishList.objects.create(
        user=user,
        comic=comic,
        favorite=True,
        cart=False,
        wished_qty=2,
        bought_qty=1
    )
    
@pytest.mark.django_db
def test_get_comic(client):
    endpoint = '/get-comic/'
    response = client.get(endpoint)

    comic_data = {
		"id": 1,
		"marvel_comic": "1010",
		"title": 'Inove',
		"stock_qty": 6,
		"description": "Mi primer JSON en Django",
		"price": 10.0,
		"picture": "https://www.django-rest-framework.org/img/logo.png"
	}

    # Verificar que la petición haya retornando 200
    assert response.status_code == status.HTTP_200_OK, f'Endpoint incorrecto'

    data = response.json()
   
    # Comparar los valores obtenidos con el patron
    # uno por uno
    for k in comic_data:
        assert data.get(k) == comic_data.get(k), f'El campo {k} no es {comic_data[k]}'
