from django.forms import *

from core.logic.models import Cliente


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombres': TextInput(attrs={
                'placeholder': 'Ingrese su nombre completo.',
            }),
            'apellidos': TextInput(attrs={
                'placeholder': 'Ingrese su apellido completo.',
            }),
            'dni': TextInput(attrs={
                'placeholder': 'Ingrese su DNI.',
            }),
        }

    def save(self, commit=True):
        data = {}
        try:
            if self.is_valid():
                self.instance.save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
