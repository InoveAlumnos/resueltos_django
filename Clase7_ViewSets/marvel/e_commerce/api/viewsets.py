from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from e_commerce.models import WishList
from e_commerce.api.serializers import WishListSerializer


class WishListViewSet(ModelViewSet):
    queryset = WishList.objects.all().order_by('user__username')
    serializer_class = WishListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        _username = self.request.query_params.get('username')
        queryset = self.queryset
        if _username:
            queryset = queryset.filter(user__username=_username)
        return queryset
