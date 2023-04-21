from django.forms import ModelForm
from gestorapp.models import Personaje

class PersonajeForm(ModelForm):
    class Meta:
        model = Personaje
        fields = '__all__'
