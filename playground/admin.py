from django.contrib import admin

from .models import Character, Equipement, Lieu

admin.site.register(Character)
admin.site.register(Equipement)
admin.site.register(Lieu)