import pytest

from django.urls import reverse, NoReverseMatch

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from e_commerce.api import routers
from e_commerce.api import views
from e_commerce.api import viewsets
from pytest_fixtures import *


# Testeamos que la view solo permite requests de tipo POST
@pytest.mark.django_db
def test_wishlist_viewset(client, create_wishlist, get_token):
    api_view_name = "WishListViewSet"
    msg = (
        f'La clase API View "{api_view_name}" no se encuentra definida en '
        'e_commerce/api/viewsets.py'
    )
    assert hasattr(viewsets, api_view_name), msg
    msg = f'La clase "{api_view_name}" no hereda de la Clase "ModelViewSet".'
    assert issubclass(viewsets.WishListViewSet, ModelViewSet), msg
    
    _msg = 'La variable "router" no es una instancia de la clase "DefaultRouter".'
    assert isinstance(routers.router, DefaultRouter), _msg
    try:
        endpoint = reverse('wishlist-list')
    except NoReverseMatch:
        msg = (
            'El parámetro "name" no se encuentra definido o no es el '
            f'correcto cuando definió la URL de la view: {api_view_name}.'
        )
        assert False, msg
    response = client.get(endpoint)
    _msg = (
        f'El endpoint: "{response.request.get("PATH_INFO")}" '
        'debería ser sólo accesible para un cliente authenticado.'
    )
    _unauthorized = response.status_code == status.HTTP_401_UNAUTHORIZED
    _forbidden = response.status_code == status.HTTP_403_FORBIDDEN
    assert _unauthorized or _forbidden, _msg
    _wish_list = create_wishlist()
    _token = get_token(_wish_list.user)
    client.force_login(_wish_list.user)
    response = client.get(
        endpoint,
        {"username": f'{_wish_list.user.username}'},
        HTTP_AUTHORIZATION=f'Token {_token.key}'
    )
    _data = response.json()
    assert response.status_code != status.HTTP_401_UNAUTHORIZED, 'Token Inválido.'
    assert response.status_code == status.HTTP_200_OK, f'Ocurrió un error: {_data}'
    assert 'results' in _data, 'La API no está paginando.'
    _results = _data.get('results')
    if _results:
        _msg = f'El campo "user" tiene que ser un objeto. user: {_data.get("user")}'
        assert isinstance(_results[0].get('user'), dict), _msg
        _msg = f'El campo "comic" tiene que ser un objeto. comic: {_data.get("comic")}'
        assert isinstance(_results[0].get('comic'), dict), _msg
    else:
        assert _results != [], f'La API no está filtrando por el campo "username".'


@pytest.mark.django_db
def test_comics_user(client, create_wishlist, get_token):
    api_view_name = "ComicUserAPIView"
    msg = (
        f'La clase API View "{api_view_name}" no se encuentra definida en '
        'e_commerce/api/views.py'
    )
    assert hasattr(views, api_view_name), msg
    msg = f'La clase "{api_view_name}" no hereda de la Clase "ModelViewSet".'
    assert issubclass(views.ComicUserAPIView, ListAPIView), msg
    
    _wish_list = create_wishlist()
    try:
        endpoint = reverse(
            'comic_list_user',
            kwargs={"username": f"{_wish_list.user.username}"}
        )
    except NoReverseMatch:
        msg = (
            'El parámetro "name" no se encuentra definido o no es el '
            f'correcto cuando definió la URL de la view: {api_view_name}.'
        )
        assert False, msg
    response = client.get(endpoint)
    _msg = (
        f'El endpoint: "{response.request.get("PATH_INFO")}" '
        'debería ser sólo accesible para un cliente authenticado.'
    )
    _unauthorized = response.status_code == status.HTTP_401_UNAUTHORIZED
    _forbidden = response.status_code == status.HTTP_403_FORBIDDEN
    assert _unauthorized or _forbidden, _msg
    _token = get_token(_wish_list.user)
    client.force_login(_wish_list.user)
    response = client.get(
        endpoint,
        {"search": f'{_wish_list.comic.title[:3]}'},
        HTTP_AUTHORIZATION=f'Token {_token.key}'
    )
    _data = response.json()
    assert response.status_code != status.HTTP_401_UNAUTHORIZED, 'Token Inválido.'
    assert response.status_code == status.HTTP_200_OK, f'Ocurrió un error: {_data}'
    assert 'results' in _data, 'La API no está paginando.'
    assert _data.get('results') != [], f'La API no está buscando por el campo "search".'
