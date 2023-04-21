from django.shortcuts import render
from gestorapp.models import Personaje, Npc, Dialogos, Ruta, Camino

# Create your views here.
def index(request):
    formaPersonaje = Personaje.objects.all()
    formaNpc = Npc.objects.all()
    formaDialogos = Dialogos.objects.all()

    return render (
        request,
        '',
        {
            'formaPersonaje' : formaPersonaje,
            'formaNpc' : formaNpc,
            'formaDialogos' : formaDialogos
        }
    )