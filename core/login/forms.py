from django.contrib.auth import authenticate
from django.forms import *

from core.account.models import User


class LoginForm(Form):
    username = CharField(widget=TextInput(attrs={
        'placeholder': 'Ingrese su usuario.',
    }))
    password = CharField(widget=PasswordInput(attrs={
        'placeholder': 'Ingrese su contraseña.',
    }))

    def clean(self):
        cleaned = self.cleaned_data
        username = cleaned.get('username', '')
        password = cleaned.get('password', '')
        if len(username) < 0:
            raise ValidationError('Debe de ingresar un nombre de usuario.')
        if len(password) < 0:
            raise ValidationError('Debe de ingresar su contraseña de usuario.')
        user_autenticado = authenticate(username=username, password=password)
        if user_autenticado is None:
            raise forms.ValidationError(
                'Por favor introduzca el nombre de usuario y la clave correctos para una cuenta de personal.'
                ' Observe que ambos campos pueden ser sensibles a mayúsculas.')
        return cleaned

    def get_user(self):
        username = self.cleaned_data.get('username', '')
        return User.objects.get(username=username)