from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename="Product")

urlpatterns = [
    path(r'',include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = []
# urlpatterns += router.urls