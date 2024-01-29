from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from rest_framework import routers
from .api.viewsets import FarmaciaViewSet

router = routers.DefaultRouter()
router.register(r'api_farmacias', FarmaciaViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
