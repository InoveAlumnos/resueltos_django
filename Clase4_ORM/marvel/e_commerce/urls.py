from django.urls import path
from e_commerce.views import *


urlpatterns = [
    path('comic-list/', comic_list_api_view, name="comic_list_api_view"),
    path('comic-filter-stock/', comic_filter_stock_api_view, name="comic_filter_stock_api_view"),
    path('comic-filter-price/', comic_filter_price_api_view, name="comic_filter_price_api_view"),
    path('comic-list-order/', comic_list_order_api_view, name="comic_list_order_api_view"),
]
