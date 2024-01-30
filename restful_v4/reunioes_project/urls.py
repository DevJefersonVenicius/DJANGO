from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from rest_framework import routers
from .api.viewsets import ReuniaoViewSet

router = routers.DefaultRouter()
router.register(r'api_reunioes_project', ReuniaoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('api_reunioes_project/', include(router.urls)),
    path('delete/<int:id>', views.delete_reuniao, name='delete'),
] 
