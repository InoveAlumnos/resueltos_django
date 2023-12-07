from rest_framework.routers import DefaultRouter

from canales.api.viewsets import ChatViewSet, MensajeViewSet


router = DefaultRouter()
router.register(
    r'chats',
    ChatViewSet,
    basename='chats'
)
router.register(
    r'mensajes',
    MensajeViewSet,
    basename='mensajes'
)

urlpatterns = router.urls
