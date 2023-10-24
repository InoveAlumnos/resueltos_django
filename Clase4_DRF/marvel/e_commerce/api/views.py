from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from e_commerce.models import Comic


@api_view(http_method_names=['GET'])
def comic_list_api_view(request):
    _queryset = Comic.objects.all()
    _data = list(_queryset.values()) if _queryset.exists() else []
    return Response(data=_data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def comic_retrieve_api_view(request):
    instance = get_object_or_404(
        Comic, id=request.query_params.get('id')
    )
    
    return Response(
        data=model_to_dict(instance), status=status.HTTP_200_OK
    )


@api_view(http_method_names=['POST'])
def comic_create_api_view(request):
    _marvel_id = request.data.pop('marvel_id', None)
    print(request.data)
    if not _marvel_id:
        raise ValidationError(
            {"marvel_id": "Este campo no puede ser nulo."}
        )
    _instance, _created = Comic.objects.get_or_create(
        marvel_id=_marvel_id,
        defaults=request.data
    )
    if _created:
        return Response(
            data=model_to_dict(_instance), status=status.HTTP_201_CREATED
        )
    return Response(
        data={
            "marvel_id": "Ya existe un comic con ese valor, debe ser único."
        },
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(http_method_names=['GET'])
def comic_list_filtered_api_view(request):
    _queryset = Comic.objects.filter(price__gt=5.00)
    _data = list(_queryset.values()) if _queryset.exists() else []
    return Response(data=_data, status=status.HTTP_200_OK)