from rest_framework.routers import DefaultRouter

from e_commerce.api.viewsets import WishListViewSet


router = DefaultRouter()
router.register(
    r'wishlist',
    WishListViewSet,
    basename='wishlist'
)

urlpatterns = router.urls
