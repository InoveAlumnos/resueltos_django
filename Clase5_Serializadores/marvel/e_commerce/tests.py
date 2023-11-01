import json
import pytest

from pytest_fixtures import *

from django.urls import reverse, NoReverseMatch

from rest_framework import status
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, ListCreateAPIView
)
from rest_framework.serializers import ModelSerializer

from e_commerce.api import serializers
from e_commerce.api import views
from e_commerce.models import WishList


@pytest.mark.django_db
def test_serializer_user():
    serializer_name = 'UserSerializer'
    msg = (
        f'El serializador "{serializer_name}" no se encuentra definido en '
        'e_commerce/api/serializers.py'
    )
    assert hasattr(serializers, serializer_name), msg
    msg = f'El serializador "{serializer_name}" no hereda de la clase ModelSerializer'
    assert issubclass(serializers.UserSerializer, ModelSerializer), msg
    serializer_fields = serializers.UserSerializer.Meta.fields
    if serializer_fields != '__all__':
        serializer_fields = set(serializer_fields)
        user_fields = ('id', 'username', 'email')
        msg = (
            f'Alguno de estos campos: {user_fields} no se encuentran definidos '
            f'en "{serializer_name}".'
        )
        assert set(user_fields).issubset(serializer_fields), msg


@pytest.mark.django_db
def test_user_list_api_view(client):
    api_view_name = 'UserListAPIView'
    msg = (
        f'La clase API View "{api_view_name}" no se encuentra definida en '
        'e_commerce/api/views.py'
    )
    assert hasattr(views, api_view_name), msg
    msg = f'La clase "{api_view_name}" no hereda de la Clase "ListAPIView".'
    assert issubclass(views.UserListAPIView, ListAPIView), msg
    endpoint = reverse('user_class_list_api_view')
    response = client.get(endpoint)
    msg = f'Endpoint "{endpoint}" no encontrado.'
    assert response != status.HTTP_404_NOT_FOUND, msg


@pytest.mark.django_db
def test_user_retrieve_api_view(client, create_user):
    api_view_name = 'UserRetrieveAPIView'
    view_namespace = 'user_class_retrieve_api_view'
    msg = (
        f'La clase API View "{api_view_name}" no se encuentra definida en '
        'e_commerce/api/views.py'
    )
    assert hasattr(views, api_view_name), msg
    msg = f'La clase "{api_view_name}" no hereda de la Clase "RetrieveAPIView".'
    assert issubclass(views.UserRetrieveAPIView, RetrieveAPIView), msg
    user = create_user()
    try:
        endpoint = reverse(
            view_namespace, kwargs={"username": f"{user.username}"}
        )
    except NoReverseMatch:
        msg = (
            'El parámetro "name" no se encuentra definido o no es el '
            f'correcto cuando definió la URL de la view: {api_view_name}.'
        )
        assert False, msg
    response = client.get(endpoint)
    data = response.json()
    if response.status_code == status.HTTP_200_OK and data:
        msg = (
            'La view debe devolver un usuario según el "username" '
            'pasado en la URL.'
        )
        assert user.username == response.json().get('username'), msg


@pytest.mark.django_db
def test_serializer_wish_list():
    serializer_name = "WishListSerializer"
    msg = (
        f'El serializador "{serializer_name}"  no se encuentra definido en '
        'e_commerce/api/serializers.py'
    )
    assert hasattr(serializers, serializer_name), msg
    msg = f'El serializador "{serializer_name}" no hereda de la clase ModelSerializer'
    assert issubclass(serializers.WishListSerializer, ModelSerializer), msg
    serializer_fields = serializers.WishListSerializer.Meta.fields
    if serializer_fields != '__all__':
        serializer_fields = set(serializer_fields)
        wishlist_fields = [field.name for field in WishList._meta.get_fields()]
        msg = (
            f'Alguno de estos campos: {wishlist_fields} no se encuentran '
            f'definidos en "{serializer_name}".'
        )
        assert set(wishlist_fields).issubset(serializer_fields), msg


@pytest.mark.django_db
def test_wishlist_api_view(client, create_user, create_comic):
    user = create_user()
    comic = create_comic()
    data = {
        "user": user.id,
        "comic": comic.id,
        "favorite": True,
        "cart": False,
        "wished_qty": 2,
        "bought_qty": 0
    }
    api_view_name = 'WishListAPIView'
    msg = (
        f'La clase API View "{api_view_name}" no se encuentra definida en '
        'e_commerce/api/views.py'
    )
    assert hasattr(views, api_view_name), msg
    msg = f'La clase "{api_view_name}" no hereda de la Clase "ListCreateAPIView".'
    assert issubclass(views.WishListAPIView, ListCreateAPIView), msg
    endpoint = reverse('wishlist_class_api_view')
    response = client.post(endpoint, data=json.dumps(data), content_type='application/json')
    msg = f'Endpoint "{endpoint}" no encontrado.'
    assert response != status.HTTP_404_NOT_FOUND, msg
    assert response != status.HTTP_405_METHOD_NOT_ALLOWED, 'Método HTTP no permitido.'
    msg = f'Hubo un error: {response.json()}'
    assert response.status_code < status.HTTP_400_BAD_REQUEST, msg
    msg = 'No pudo crearse un nuevo registro para el modelo WishList.'
    assert comic.wishlist_set.filter(user=user).exists(), msg
