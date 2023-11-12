from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Character, Equipement
from django.db import transaction

def character_list(request):
        characters = Character.objects.all()
        return render(request, 'playground/character_list.html', {'characters': characters})


def character_detail(request, id_character):
        character = get_object_or_404(Character, id_character=id_character)
        if request.method == "POST":
                form = MoveForm(request.POST, instance=character)
                if form.is_valid():
                        if character.equipement.disponibilite == "libre" :
                                        ancien_equip = get_object_or_404(Equipement, id_equip=character.equipement.id_equip)
                                        ancien_equip.disponibilite = "libre"
                                        ancien_equip.save()
                                        form.save(commit=False)
                                        nouveau_equip = get_object_or_404(Equipement, id_equip=character.equipement.id_equip)
                                        if nouveau_equip.id_equip != "Épée":
                                                nouveau_equip.disponibilite = "occupé"
                                        nouveau_equip.save()
                                        character.equipement = nouveau_equip
                                        character.save()
                                        return redirect('character_detail', id_character=character.id_character)
                        else :
                                return redirect('character_detail', id_character=character.id_character)
                else:
                        form = MoveForm()
                        return render(request, 'playground/character_detail.html', {'character': character, 'equipement': character.equipement, 'form': form})
        else:
                form = MoveForm()
                return render(request, 'playground/character_detail.html', {'character': character, 'equipement': character.equipement, 'form': form})
