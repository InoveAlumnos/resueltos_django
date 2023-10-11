from django.urls import path

from e_commerce.views_test import *


urlpatterns = [
    path('tests/superuser/', user_test_view),
    path('tests/comic/', comic_test_view),
    path('tests/wishlist/', wishlist_test_view),
    path('api/comic/get/', get_comic_api_view),
]
