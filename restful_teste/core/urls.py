from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('farmacias.urls')),
    path('cadastro_medicamentos', include('cadastro_medicamentos.urls')),
]
