from django.contrib import admin
from .models import Musica

class ListMusica(admin.ModelAdmin):
    list_display = ('nome', 'artista', 'data_gravacao')

admin.site.register(Musica, ListMusica)
