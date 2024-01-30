from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from rest_framework import routers
from .api.viewsets import FilmeViewSet

router = routers.DefaultRouter()
router.register('api_filmes', FilmeViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('api_filmes/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
