from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('deletar/', views.deletar, name='deletar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
