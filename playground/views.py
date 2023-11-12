from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Character

def character_list(request):
        characters = Character.objects.all()
        return render(request, 'playground/character_list.html', {'characters': characters})

def character_detail(request, id_character):
        character = get_object_or_404(Character, id_character=id_character)
        lieu = character.lieu
        form=MoveForm()
        return render(request, 'playground/character_detail.html', {'character': character, 'lieu': lieu, 'form': form})