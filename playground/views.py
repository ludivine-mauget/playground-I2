from django.shortcuts import render, get_object_or_404, redirect
from .forms import EquipForm, LieuForm
from .models import Character, Equipement, Lieu

def character_list(request):
        characters = Character.objects.all()
        return render(request, 'playground/character_list.html', {'characters': characters})


def character_detail(request, id_character):
        character = get_object_or_404(Character, id_character=id_character)
        ancien_equip = get_object_or_404(Equipement, id_equip=character.equipement.id_equip)
        ancien_lieu = get_object_or_404(Lieu, id_lieu=character.lieu.id_lieu)
        if request.method == "POST":
                if 'equipement' in request.POST:
                        equip_form = EquipForm(request.POST, instance=character)
                        lieu_form = LieuForm()
                        if equip_form.is_valid():
                                nouveau_equip = equip_form.cleaned_data['equipement']
                                equip_choisi = get_object_or_404(Equipement, id_equip=nouveau_equip)
                                if equip_choisi.disponibilite == "libre" :
                                                ancien_equip.disponibilite = "libre"
                                                ancien_equip.save()
                                                if equip_choisi.id_equip != "Epée":
                                                        equip_choisi.disponibilite = "occupé"
                                                equip_choisi.save()
                                                character.equipement = equip_choisi
                                                character.save()
                                                return redirect('character_detail', id_character=character.id_character)
                                else :
                                        occupants = Character.objects.filter(equipement=equip_choisi.id_equip)
                                        noms_occupants = ", ".join([occupant.id_character for occupant in occupants])
                                        message = f"L'équipement {equip_choisi} est déjà équipé par {noms_occupants}  !"
                                        return render(request, 'playground/character_detail.html', {'character': character, 'equipement': ancien_equip, 'equip_form': equip_form, 'lieu_form': lieu_form, 'message': message, 'lieu': ancien_lieu})
                        else :
                                message = "Le formulaire n'est pas valide."
                                return render(request, 'playground/character_detail.html', {'character': character, 'equipement': character.equipement, 'equip_form': equip_form, 'lieu_form': lieu_form, 'message': message, 'lieu': character.lieu})
                if 'lieu' in request.POST:
                        lieu_form = LieuForm(request.POST, instance=character)
                        equip_form = EquipForm()
                        if lieu_form.is_valid():
                                nouveau_lieu = lieu_form.cleaned_data['lieu']
                                lieu_choisi = get_object_or_404(Lieu, id_lieu=nouveau_lieu)
                                if lieu_choisi.disponibilite == "libre" :
                                                ancien_lieu.disponibilite = "libre"
                                                ancien_lieu.save()
                                                if lieu_choisi.id_lieu == "Lit":
                                                        lieu_choisi.disponibilite = "occupé"
                                                        character.etat = "endormi"
                                                if lieu_choisi.id_lieu == "Foncombe":
                                                        character.etat = "repus"
                                                if lieu_choisi.id_lieu == "Champ de bataille":
                                                        character.etat = "fatigué"
                                                if lieu_choisi.id_lieu == "Comté":
                                                        character.etat = "affamé"
                                                lieu_choisi.save()
                                                character.lieu = lieu_choisi
                                                character.save()
                                                return redirect('character_detail', id_character=character.id_character)
                                else :
                                        occupants = Character.objects.filter(lieu=lieu_choisi.id_lieu)
                                        noms_occupants = ",".join([occupant.id_character for occupant in occupants])
                                        message = f"Le lieu {nouveau_lieu} est déjà occupé par {noms_occupants}  !"
                                        return render(request, 'playground/character_detail.html', {'character': character, 'equipement': ancien_equip, 'equip_form': equip_form, 'lieu_form': lieu_form, 'message': message, 'lieu': ancien_lieu})
                        else :
                                message = "Le formulaire n'est pas valide."
                                return render(request, 'playground/character_detail.html', {'character': character, 'equipement': character.equipement, 'equip_form': equip_form, 'lieu_form': lieu_form, 'message': message, 'lieu': character.lieu})
        else:
                equip_form = EquipForm()
                lieu_form = LieuForm()
                return render(request, 'playground/character_detail.html', {'character': character, 'equipement': character.equipement, 'equip_form': equip_form, 'lieu_form': lieu_form, 'lieu': character.lieu})
