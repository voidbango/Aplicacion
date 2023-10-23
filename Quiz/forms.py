from django import forms

from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_models

User = get_user_models()

class ElegirInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInlineFormset, self).clean()

        respuesta_correcta=0
        for formulario in self.forms:
            if not formulario.is_valid():
                return

            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta +=1

        try:
            assert respuesta_correcta == Pregunta.NUMER_DE_RESPUESTAS_PERMITIDAS
        except AssertionError:
            raise forms.ValidationError('Exactamente una sola respuesta es permitida')
#creando el sign up
class RegistroFormulario(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name'
            'username',
            'email',
            'password1',
            'password2'

        ]

