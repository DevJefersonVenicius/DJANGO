from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 
from .import views
from rest_framework import routers
from .api.viewsets import GerenciamentoDentarioViewSet

router = routers.DefaultRouter()
router.register('api_gerenciamentos_dentarios', GerenciamentoDentarioViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('area_exibicao/', views.area_exibicao, name='area_exibicao'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('api_gerenciamentos_dentarios/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)