from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.validators import ValidationError

from e_commerce.models import Comic


# def comic_retrieve_api_view(request):
#     if request.method == 'GET':
#         instance = Comic.objects.filter(id=request.GET.get('id')).first()
#         if instance:
#             return JsonResponse(data=model_to_dict(instance), status=200)
#         return JsonResponse(data={}, status=404)
#     else:
#         return JsonResponse(
#             data={"message": "Método HTTP no permitido."},
#             status=405
#         )


# def comic_list_api_view(request):
#     if request.method == 'GET':
#         _queryset = Comic.objects.all()
#         _data = list(_queryset.values()) if _queryset.exists() else []
#         return JsonResponse(data=_data, safe=False, status=200)
#     else:
#         return JsonResponse(
#             data={"message": "Método HTTP no permitido."},
#             status=405
#         )

# @csrf_exempt
# def comic_create_api_view(request):
#     if request.method == 'POST':
#         # Casteo el query-dict request.POST a un dict para poder aplicar
#         # método .pop() ya que el query-dict es inmutable.
#         _request = dict(request.POST)
#         _marvel_id = _request.pop('marvel_id', None)
#         if not _marvel_id:
#             return JsonResponse(
#                 data={"marvel_id": "Este campo no puede ser nulo."},
#                 status=400
#             )
#         _instance, _created = Comic.objects.get_or_create(
#             marvel_id=_marvel_id,
#             defaults=_request.POST
#         )
#         if _created:
#             return JsonResponse(
#                 data=model_to_dict(_instance), status=201
#             )
#         return JsonResponse(
#             data={
#                 "marvel_id": "Ya existe un comic con ese valor, debe ser único."
#             },
#             status=400
#         )
#     else:
#         return JsonResponse(
#             data={"message": "Método HTTP no permitido."},
#             status=405
#         )


# NOTE: Ahora comenzamos usando DRF:
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