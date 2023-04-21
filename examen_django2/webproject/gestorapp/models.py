from django.db import models

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_length=200)
    pe = models.CharField(max_length=200)
    ataque = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f'Personaje {self.id} : {self.nombre}, {self.pe}, {self.ataque}'

class Ruta(models.Model):
    personaje = models.ForeignKey(Personaje, on_delete=models.SET_NULL, null  = True)
    tipo = models.CharField(max_length=200)
    hostilidad = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f'Ruta {self.id} : {self.personaje} : {self.tipo} : {self.hostilidad}'

class Npc(models.Model):
    nombre = models.CharField(max_length=200)
    pv = models.CharField(max_length=200)
    ataque = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f'Npc {self.id} : {self.nombre} : {self.pv} : {self.ataque}'

class Dialogos(models.Model):
    npc = models.ForeignKey(Npc, on_delete=models.SET_NULL, null  = True)
    texto = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f'Dialogos {self.id} : {self.npc} : {self.texto}'

class Camino(models.Model):
    spawns = models.CharField(max_length=200)
    dificultad = models.IntegerField()
    def __str__(self) -> str:
        return f'Camino {self.id} : {self.spawns}'
