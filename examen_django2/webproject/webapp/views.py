from django.shortcuts import render,redirect,get_object_or_404
from gestorapp.models import Personaje, Npc, Dialogos, Ruta, Camino
from gestorapp.forms import PersonajeForm

# Create your views here.
def index(request):
    formaPersonaje = Personaje.objects.all()
    formaNpc = Npc.objects.all()
    formaDialogos = Dialogos.objects.all()
    formaRuta = Ruta.objects.all()
    formaCamino = Camino.objects.all()

    return render (
        request,
        'index.html',
        {
            'formaPersonaje' : formaPersonaje,
            'formaNpc' : formaNpc,
            'formaDialogos' : formaDialogos,
            'formaRuta': formaRuta,
            'formaCamino':formaCamino
        }
    )

def indexPersonaje(request):
    formaPersonaje = Personaje.objects.all()
    return render(request, 'indexPersonaje.html', {'formaPersonaje': formaPersonaje})

def nuevoPersonaje(request):
    if request.method == 'POST':
          formaPersonaje = PersonajeForm(request.POST)
          if formaPersonaje.is_valid():
                formaPersonaje.save()
                return redirect('indexPersonaje')
    else:
            formaPersona= PersonajeForm()
    return render(request,'nuevo.html',{'formaPersona': formaPersona})

def editarPersonaje(request,id):
      personaje = get_object_or_404(Personaje,pk=id)
      if request.method == 'POST':
        formaPersonaje = PersonajeForm(request.POST,instance=personaje)
        if formaPersonaje.is_valid():
             formaPersonaje.save()
             return redirect('indexPersonaje')
      else:
        formaPersonaje = PersonajeForm(instance=personaje)
      return render(request,'editar.html',{'formaPersona': formaPersonaje})

def eliminarPersonaje(request, id):
    personaje = get_object_or_404(Personaje, pk = id)
    if personaje:
        personaje.delete()
    return redirect('indexPersonaje')

def detallePersonaje(request,id):
     personaje = get_object_or_404(Personaje, pk = id)
     return render(request,'detalle.html',{'personaje':personaje})

def indexNpc(request):
    formaNpc = Npc.objects.all()
    return render(request, 'indexNpc.html', {'formaNpc': formaNpc})

def indexDialogos(request):
    formaDialogos = Dialogos.objects.all()
    return render(request, 'indexDialogos.html', {'formaDialogos': formaDialogos})

def indexRuta(request):
    formaRuta = Ruta.objects.all()
    return render(request, 'indexRuta.html', {'formaRuta': formaRuta})

def indexCamino(request):
    formaCamino = Camino.objects.all()
    return render(request, 'indexCamino.html', {'formaCamino': formaCamino})
