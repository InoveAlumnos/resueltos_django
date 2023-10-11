import pytest
import requests

from django.test import TestCase

from rest_framework import status

from e_commerce.models import Comic, WishList
from pytest_fixtures import *


DOMAIN = 'http://localhost'


# Create your tests here.
@pytest.mark.django_db
class TestUser:
    endpoint = 'e-commerce/tests/superuser/'
    response = requests.get(f'{DOMAIN}:8000/{endpoint}')

    def test_superuser(self):
        assert self.response.status_code == status.HTTP_200_OK


class TestComic(TestCase):
    comic_data = {
        "marvel_id": 9999,
        "title": 'Mi primer Comic',
        "description": 'Esta es una descripcion de mi primer comic',
        "price": 9.99,
        "stock_qty": 5,
        "picture": 'https://www.django-rest-framework.org/img/logo.png'
    }
    endpoint = 'e-commerce/tests/comic/'
    response = requests.get(f'{DOMAIN}:8000/{endpoint}')

    def test_exists_comic(self):
        self.assertEqual(
            self.response.status_code,
            status.HTTP_200_OK,
            msg='Comic does not exist.'
        ) 

    def test_data_integrity(self):
        _data = self.response.json()
        # Compare fields' values:
        for k in self.comic_data:
            self.assertEqual(
                _data.get(k),
                self.comic_data.get(k),
                msg = f'The field {k} is not {self.comic_data[k]}'
            )


class TestWishList(TestCase):
    endpoint = 'e-commerce/tests/wishlist/'
    response = requests.get(f'{DOMAIN}:8000/{endpoint}')

    def test_exist_objects(self):
        self.assertEqual(
            self.response.status_code,
            status.HTTP_200_OK,
            msg='User,or Comic or WishList does not exist.'
        ) 

    def test_data_integrity(self):
        _data = self.response.json()
        self.assertEqual(
            _data.get('user', {}).get('username'),
            'inove',
            msg='User does not exist.'
        )
        self.assertEqual(
            _data.get('comic', {}).get('marvel_id'),
            9999,
            msg='Comic does not exist.'
        )
        self.assertTrue(
            _data.get('wishlist', {}).get('favorite', False),
            msg='Comic does not exist or is not in Favorite.'
        )


class TestComicView(TestCase):
    endpoint = 'e-commerce/api/comic/get/'
    response = requests.get(f'{DOMAIN}:8000/{endpoint}')

    _comic_data = {
		"id": 1,
		"marvel_comic": "1010",
		"title": 'Inove',
		"stock_qty": 6,
		"description": "Mi primer JSON en Django",
		"price": 10.0,
		"picture": "https://www.django-rest-framework.org/img/logo.png"
	}

    def test_url(self):
        self.assertEqual(
            self.response.status_code,
            status.HTTP_200_OK,
            msg='Wrong endpoint.'
        )

    def test_comic_data(self):
        _data = self.response.json()
        # Compare fields' values:
        for k in self._comic_data:
            self.assertEqual(
                _data.get(k),
                self._comic_data.get(k),
                msg = f'The field {k} is not {self._comic_data[k]}'
            )
