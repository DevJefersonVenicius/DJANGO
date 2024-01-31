from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rosto_corpo_gerenciamento_consultas.urls')),
]
