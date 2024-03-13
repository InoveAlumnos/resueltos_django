import pytest
from pytest_fixtures import *

from django.urls import reverse
from django.core.management import call_command

from rest_framework import status

from e_commerce import models


@pytest.mark.django_db
def test_comic_list(client, create_list_of_comic):

    create_list_of_comic()

    endpoint_url = reverse('comic_list_api_view')
    response = client.get(endpoint_url)

    assert response.status_code == status.HTTP_200_OK, 'El endpoint falló al ejecutarse'

    data = response.json()
    print(f"Tipo de dato retornado por la vista: {type(data)}")
    assert isinstance(data, list), f'Se espera que el endpoint retorne una lista'

    print(f"Cuantos comics retornó el enpdoint en la lista: {len(data)}")
    assert len(data), 'La lista de comics no debe estar vacía'


@pytest.mark.django_db
def test_comic_filter_stock(client, create_list_of_comic):

    create_list_of_comic()

    endpoint_url = reverse('comic_filter_stock_api_view')
    response = client.get(endpoint_url)

    assert response.status_code == status.HTTP_200_OK, 'El endpoint falló al ejecutarse'

    data = response.json()
    print(f"Tipo de dato retornado por la vista: {type(data)}")
    assert isinstance(data, list), f'Se espera que el endpoint retorne una lista'

    print(f"Cuantos comics retornó el enpdoint en la lista: {len(data)}")
    assert len(data), 'La lista de comics no debe estar vacía'

    for comic in data:
        assert comic['stock_qty'] == 5, 'El stock de cada comic retornado debe ser 5'


@pytest.mark.django_db
def test_comic_filter_price(client, create_list_of_comic):

    create_list_of_comic()

    endpoint_url = reverse('comic_filter_price_api_view')
    response = client.get(endpoint_url)

    assert response.status_code == status.HTTP_200_OK, 'El endpoint falló al ejecutarse'

    data = response.json()
    print(f"Tipo de dato retornado por la vista: {type(data)}")
    assert isinstance(data, list), f'Se espera que el endpoint retorne una lista'

    print(f"Cuantos comics retornó el enpdoint en la lista: {len(data)}")
    assert len(data), 'La lista de comics no debe estar vacía'

    for comic in data:
        assert comic['price'] > 3, 'El precio de cada comic retornado debe ser mayor a 3'

@pytest.mark.django_db
def test_comic_list_order(client, create_list_of_comic):

    create_list_of_comic()

    endpoint_url = reverse('comic_list_order_api_view')
    response = client.get(endpoint_url)

    assert response.status_code == status.HTTP_200_OK, 'El endpoint falló al ejecutarse'

    data = response.json()
    print(f"Tipo de dato retornado por la vista: {type(data)}")
    assert isinstance(data, list), f'Se espera que el endpoint retorne una lista'

    print(f"Cuantos comics retornó el enpdoint en la lista: {len(data)}")
    assert len(data), 'La lista de comics no debe estar vacía'

    data_ordenada = sorted(data, key=lambda k: k['marvel_id'])

    for c1, c2 in zip(data, data_ordenada):
        assert c1['id'] == c2['id'], 'La lista debe estar ordenada por marvel_id de menor a mayor'