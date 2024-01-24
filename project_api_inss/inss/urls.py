from django.urls import path, include
from rest_framework import routers
from .api.viewsets import CadastroInssViewSet

router = routers.DefaultRouter()
router.register(r'cadastroinss', CadastroInssViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
