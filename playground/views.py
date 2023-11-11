from django.shortcuts import render
from .models import Character

def character_list(request):
        characters = Character.objects.all()
        return render(request, 'playground/character_list.html', {'characters': characters})