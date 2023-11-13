from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Character, Equipement, Lieu

def character_list(request):
        characters = Character.objects.all()
        return render(request, 'playground/character_list.html', {'characters': characters})


def character_detail(request, id_character):
        character = get_object_or_404(Character, id_character=id_character)
        ancien_equip = get_object_or_404(Equipement, id_equip=character.equipement.id_equip)
        lieu = get_object_or_404(Lieu, id_lieu=character.lieu.id_lieu)
        # print(ancien_equip)
        if request.method == "POST":
                form = MoveForm(request.POST, instance=character)
                if form.is_valid():
                        nouveau_equip = form.cleaned_data['equipement']
                        # print(nouveau_equip)
                        equip_choisi = get_object_or_404(Equipement, id_equip=nouveau_equip)
                        # print(equip_choisi)
                        if equip_choisi.disponibilite == "libre" :
                                        # ancien_equip = get_object_or_404(Equipement, id_equip=character.equipement.id_equip)
                                        ancien_equip.disponibilite = "libre"
                                        # print(ancien_equip)
                                        # print(ancien_equip.disponibilite)
                                        ancien_equip.save()
                                        if equip_choisi.id_equip != "Épée":
                                                equip_choisi.disponibilite = "occupé"
                                        equip_choisi.save()
                                        character.equipement = equip_choisi
                                        character.save()
                                        return redirect('character_detail', id_character=character.id_character)
                        else :
                                occupant = get_object_or_404(Character, equipement=equip_choisi.id_equip)
                                message = f"L'équipement {nouveau_equip} est déjà équipé par {occupant}  !"
                                return render(request, 'playground/character_detail.html', {'character': character, 'equipement': ancien_equip, 'form': form, 'message': message, 'lieu': lieu})
                else :
                        message = "Le formulaire n'est pas valide."
                        return render(request, 'playground/character_detail.html', {'character': character, 'equipement': character.equipement, 'form': form, 'message': message, 'lieu': lieu})
        else:
                form = MoveForm()
                return render(request, 'playground/character_detail.html', {'character': character, 'equipement': character.equipement, 'form': form, 'lieu': lieu})
