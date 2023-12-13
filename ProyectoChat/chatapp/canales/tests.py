import pytest
import json

from django.urls import reverse, NoReverseMatch

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ModelViewSet

from pytest_fixtures import *
from canales import models

@pytest.mark.django_db()
def test_model_chat():
    assert hasattr(models, 'Chat'), "El modelo Chat no está definido en models"

    # Verificar que le modelo puede ser creado
    # como se especifico
    try:
        _chat = models.Chat.objects.create(
            nombre="Chat prueba",
        )
    except:
        _chat = None

    _msg = "No se ha podido crear un objeto Chat con los campos especificados en el enunciado"
    assert _chat is not None, _msg

@pytest.mark.django_db()
def test_model_mensaje(create_user, create_chat):
    assert hasattr(models, 'Mensaje'), "El modelo Mensaje no está definido en models"

    _user = create_user()
    _chat = create_chat()

    # Verificar que le modelo puede ser creado
    # como se especifico
    try:
        _mensaje = models.Mensaje.objects.create(
            user=_user,
            chat=_chat,
            contenido="Un mensaje"
        )
    except:
        _mensaje = None
    
    _msg = "No se ha podido crear un objeto Mensaje con los campos especificados en el enunciado"
    assert _mensaje is not None, _msg

@pytest.mark.django_db()
def test_chats(client, create_user, get_token):
    assert hasattr(models, 'Chat'), "El modelo Chat no está definido en models"
    assert hasattr(models, 'Mensaje'), "El modelo Mensaje no está definido en models"

    endpoint = "/api/canales/chats/"
        
    response = client.get(endpoint)
    _msg = f'Endpoint "{endpoint}" no encontrado.'
    assert response.status_code != status.HTTP_404_NOT_FOUND, _msg
    
    _msg = (
        f'El endpoint: "{response.request.get("PATH_INFO")}" '
        'debería ser sólo accesible para un cliente authenticado.'
    )
    _unauthorized = response.status_code == status.HTTP_401_UNAUTHORIZED
    _forbidden = response.status_code == status.HTTP_403_FORBIDDEN
    assert _unauthorized or _forbidden, _msg

    _user = create_user()
    _token = get_token(_user)
    client.force_login(_user)

    _payload = {"nombre": "ChatNuevo"}
    
    response = client.post(
        endpoint,
        HTTP_AUTHORIZATION=f'Token {_token.key}',
        data=json.dumps(_payload),
        content_type='application/json'
    )
    assert response.status_code != status.HTTP_401_UNAUTHORIZED, 'Token Inválido.'
    
    _data = response.json()
    assert response.status_code == status.HTTP_201_CREATED, f'Ocurrió un error: {_data}'
    
    _msg = f'El endpoint chats al utilizar POST debe retornar el chat creado, respuesta: {_data}'
    assert isinstance(_data, dict), _msg
    
    _msg = f'El chat se creó con el nombre {_payload}, respuesta: {_data["nombre"]}'
    assert _data['nombre'] == _payload['nombre'], _msg
    
    _chat = _data

    response = client.get(
        endpoint,
        HTTP_AUTHORIZATION=f'Token {_token.key}'
    )

    assert response.status_code != status.HTTP_401_UNAUTHORIZED, 'Token Inválido.'
    
    _data = response.json()
    assert response.status_code == status.HTTP_200_OK, f'Ocurrió un error: {_data}'

    _msg = f"El endpoint {endpoint} debe retornar una lista de chats"
    assert isinstance(_data, list), _msg
    
    _msg = f"El endpoint {endpoint} debe retornar el único chat creado hasta el momento"
    assert len(_data) == 1, _msg
    
    _result = _data[0]

    _msg = f"El endpoint {endpoint} debe retornar el campo nombre de cada chat"
    assert _result.get('nombre'), _msg
    
    _msg = f'El campo "nombre" tiene que ser un string. nombre: {_result.get("nombre")}'
    assert isinstance(_result.get('nombre'), str), _msg
    
    endpoint = f"/api/canales/chats/{_chat['id']}/"
        
    response = client.get(
        endpoint, 
        HTTP_AUTHORIZATION=f'Token {_token.key}'
    )
    _msg = f'Endpoint "{endpoint}" no encontrado.'
    assert response.status_code != status.HTTP_404_NOT_FOUND, _msg
    
    _payload = {'nombre': "nuevoNombre"}
    response = client.patch(
        endpoint,
        HTTP_AUTHORIZATION=f'Token {_token.key}',
        data=json.dumps(_payload),
        content_type='application/json'
    )

    _data = response.json()
    assert response.status_code == status.HTTP_200_OK, f'Ocurrió un error: {_data}'
    
    _chat['nombre'] = _payload['nombre']
    
    response = client.get(
        endpoint, 
        HTTP_AUTHORIZATION=f'Token {_token.key}'
    )
    
    _data = response.json()
    assert response.status_code == status.HTTP_200_OK, f'Ocurrió un error: {_data}'
    
    _msg = f"El endpoint {endpoint} debe retornar el chat  {_chat['id']}"
    assert isinstance(_data, dict), _msg
    assert _data == _chat, _msg

@pytest.mark.django_db()
def test_mensajes(client, create_user, create_chat, get_token):
    assert hasattr(models, 'Chat'), "El modelo Chat no está definido en models"
    assert hasattr(models, 'Mensaje'), "El modelo Mensaje no está definido en models"

    endpoint = "/api/canales/mensajes/"
        
    response = client.get(endpoint)
    _msg = f'Endpoint "{endpoint}" no encontrado.'
    assert response.status_code != status.HTTP_404_NOT_FOUND, _msg

    _msg = (
        f'El endpoint: "{response.request.get("PATH_INFO")}" '
        'debería ser sólo accesible para un cliente authenticado.'
    )
    _unauthorized = response.status_code == status.HTTP_401_UNAUTHORIZED
    _forbidden = response.status_code == status.HTTP_403_FORBIDDEN
    assert _unauthorized or _forbidden, _msg
    
    _chat = create_chat()
    _user = create_user()
    _token = get_token(_user)
    
    _payload = {
        "chat": _chat.id,
        "user": _user.id,
        "contenido": "NuevoMensaje"
    }
    
    response = client.post(
        endpoint,
        HTTP_AUTHORIZATION=f'Token {_token.key}',
        data=json.dumps(_payload),
        content_type='application/json'
    )
    assert response.status_code != status.HTTP_401_UNAUTHORIZED, 'Token Inválido.'
    
    _data = response.json()
    assert response.status_code == status.HTTP_201_CREATED, f'Ocurrió un error: {_data}'
    
    _msg = f'El endpoint mensajes al utilizar POST debe retornar el mensaje creado, respuesta: {_data}'
    assert isinstance(_data, dict), _msg
    
    key = "contenido"
    _msg = f'El mensaje se debió crear con el {key} {_payload[key]}, respuesta: {_data[key]}'
    assert _data[key] == _payload[key], _msg
    
    _chat = _data
    
    
    client.force_login(_user)
    response = client.get(
        endpoint,
        HTTP_AUTHORIZATION=f'Token {_token.key}'
    )
    assert response.status_code != status.HTTP_401_UNAUTHORIZED, 'Token Inválido.'
    
    _data = response.json()
    assert response.status_code == status.HTTP_200_OK, f'Ocurrió un error: {_data}'
    assert 'results' in _data, 'La API no está paginando.'
    
    _msg = "El endpoint debe retornar los chats creados"
    assert len(_data.get('results')) == 1, _msg
    
    _result = _data.get('results')[0]
    if _result:
        _msg = f'El campo "user" tiene que ser un ID. user: {_result.get("user")}'
        assert isinstance(_result.get('user'), int), _msg
        _msg = f'El campo "chat" tiene que ser un ID. chat: {_result.get("chat")}'
        assert isinstance(_result.get('chat'), int), _msg

@pytest.mark.django_db()
def test_chat_mensajes_get(client, create_chat, create_user, get_token, serialize_mensaje):
    assert hasattr(models, 'Chat'), "El modelo Chat no está definido en models"
    assert hasattr(models, 'Mensaje'), "El modelo Mensaje no está definido en models"

    info = {}
    _user1 = create_user()
    _user2 = create_user()
    for i in range(3):
        _chat = create_chat()
        info[_chat.id] = []
        for j in range((i+1)*2):
            mensaje = models.Mensaje.objects.create(
                chat=_chat,
                user=_user1 if j % 2 else _user2,
                contenido="Mensaje de prueba"
            )
            info[_chat.id].append(serialize_mensaje(mensaje))
    
    _chat_id, _mensajes = list(info.items())[0]
    endpoint = f'/api/chats/{_chat_id}/mensajes/'
    
    response = client.get(endpoint)
    _msg = (
        f'El endpoint: "{response.request.get("PATH_INFO")}" '
        'debería ser sólo accesible para un cliente authenticado.'
    )
    _unauthorized = response.status_code == status.HTTP_401_UNAUTHORIZED
    _forbidden = response.status_code == status.HTTP_403_FORBIDDEN
    assert _unauthorized or _forbidden, _msg
    
    _user = _user1
    _token = get_token(_user)
    client.force_login(_user)
    response = client.get(
        endpoint,
        HTTP_AUTHORIZATION=f'Token {_token.key}'
    )

    assert response.status_code != status.HTTP_401_UNAUTHORIZED, 'Token Inválido.'
    
    _data = response.json()
    assert response.status_code == status.HTTP_200_OK, f'Ocurrió un error: {_data}'

    _msg = "El endpoint debe retornar una lista de chats"
    assert isinstance(_data, list), _msg
    
    for _result in _data:    
        _mensaje_encontrado = False
        for _mensaje in _mensajes:
            if _result == _mensaje:
                _mensaje_encontrado = True
                break
        
        _msg = f"El mensaje {_result} debe ser retornando al filtrar por chat_id {_chat_id}"
        assert _mensaje_encontrado, _msg

@pytest.mark.django_db()
def test_chat_mensajes_user_get(client, create_chat, create_user, get_token, serialize_mensaje):
    assert hasattr(models, 'Chat'), "El modelo Chat no está definido en models"
    assert hasattr(models, 'Mensaje'), "El modelo Mensaje no está definido en models"

    info = {}
    _user1 = create_user()
    _user2 = create_user()
    for i in range(3):
        _chat = create_chat()
        info[_chat.id] = []
        for j in range((i+1)*2):
            mensaje = models.Mensaje.objects.create(
                chat=_chat,
                user=_user1 if j % 2 else _user2,
                contenido="Mensaje de prueba"
            )
            info[_chat.id].append(serialize_mensaje(mensaje))
    
    _chat_id, _mensajes = list(info.items())[0]
    _user_id = _user1.id
    _username = _user1.username
    _mensajes = [x for x in _mensajes if x['user'] == _user_id]
    endpoint = f'/api/chats/{_chat_id}/mensajes/{_username}/'
    
    response = client.get(endpoint)
    _msg = (
        f'El endpoint: "{response.request.get("PATH_INFO")}" '
        'debería ser sólo accesible para un cliente authenticado.'
    )
    _unauthorized = response.status_code == status.HTTP_401_UNAUTHORIZED
    _forbidden = response.status_code == status.HTTP_403_FORBIDDEN
    assert _unauthorized or _forbidden, _msg
    
    _user = _user1
    _token = get_token(_user)
    client.force_login(_user)
    response = client.get(
        endpoint,
        HTTP_AUTHORIZATION=f'Token {_token.key}'
    )

    assert response.status_code != status.HTTP_401_UNAUTHORIZED, 'Token Inválido.'
    
    _data = response.json()
    assert response.status_code == status.HTTP_200_OK, f'Ocurrió un error: {_data}'

    _msg = "El endpoint debe retornar una lista de chats"
    assert isinstance(_data, list), _msg
    
    for _result in _data:    
        _mensaje_encontrado = False
        for _mensaje in _mensajes:
            if _result == _mensaje:
                _mensaje_encontrado = True
                break
        
        _msg = f"El mensaje {_result} debe ser retornando al filtrar por chat_id {_chat_id} y username {_username}"
        assert _mensaje_encontrado, _msg