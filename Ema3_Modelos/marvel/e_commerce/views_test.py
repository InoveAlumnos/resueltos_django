from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.http import JsonResponse

from rest_framework import status

from e_commerce.models import Comic


User = get_user_model()


def user_test_view(request):
    if request.method == 'GET':
        qs = User.objects.filter(is_superuser=True).values(
            'id', 'username', 'email', 'is_superuser', 'is_staff'
        )
        if qs.exists():
            return JsonResponse(
                data=list(qs), status=status.HTTP_200_OK, safe=False
            )
    return JsonResponse(
        data=[], status=status.HTTP_404_NOT_FOUND, safe=False
    )


def comic_test_view(request):
    if request.method == 'GET':
        qs = Comic.objects.filter(marvel_id=9999)
        if qs.exists():
            return JsonResponse(
                model_to_dict(qs.first()), status=status.HTTP_200_OK
            )
    return JsonResponse(data={}, status=status.HTTP_404_NOT_FOUND)


def wishlist_test_view(request):
    data = {"user": {}, "comic": {}, "wishlist": {}}
    user_qs = User.objects.filter(username='inove')
    if user_qs.exists():
        user = user_qs.first()
        data['user'] = model_to_dict(user_qs.first())
        wishlist_qs = user.wishlist_set.filter(
            comic__marvel_id=9999, favorite=True
        )
        if wishlist_qs.exists():
            wishlist = wishlist_qs.first()
            data['comic'] = model_to_dict(wishlist.comic)
            data['wishlist'] = model_to_dict(wishlist)
            return JsonResponse(data=data, status=status.HTTP_200_OK)
    return JsonResponse(data=data, status=status.HTTP_404_NOT_FOUND)


def get_comic_api_view(request):
    _comic_data = {
		"id": 1,
		"marvel_comic": "1010",
		"title": 'Inove',
		"stock_qty": 6,
		"description": "Mi primer JSON en Django",
		"price": 10.0,
		"picture": "https://www.django-rest-framework.org/img/logo.png"
	}
    return JsonResponse(data=_comic_data, status=status.HTTP_200_OK)
