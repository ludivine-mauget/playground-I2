from django.db import models

class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default="Pas de description")
    def __str__(self):
        return self.id_equip
    
class Lieu(models.Model):
    id_lieu = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default="Pas de description")
    def __str__(self):
        return self.id_lieu


class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default="Pas de description")
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)
    def __str__(self):
        return self.id_character
