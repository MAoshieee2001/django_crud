from django.forms import *

from core.account.models import User


class MyProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'fecha_nacimiento', 'email', 'imagen']
        exclude = ['username', 'password', 'last_login', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'date_joined']
        widgets = {
            'first_name': TextInput(attrs={
                'placeholder': 'Ingrese su nombre.',
            }),
            'last_name': TextInput(attrs={
                'placeholder': 'Ingrese su apellido.',
            }),
            'fecha_nacimiento': DateInput(attrs={
                'placeholder': 'Ingrese su fecha de nacimiento.',
            }),
            'email': EmailInput(attrs={
                'placeholder': 'Ingrese su email.',
            })
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


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'fecha_nacimiento', 'email', 'imagen', 'username', 'password', 'is_active']
        exclude = ['last_login', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'date_joined']
        widgets = {
            'first_name': TextInput(attrs={
                'placeholder': 'Ingrese su nombre.',
            }),
            'last_name': TextInput(attrs={
                'placeholder': 'Ingrese su apellido.',
            }),
            'fecha_nacimiento': DateInput(attrs={
                'placeholder': 'Ingrese su fecha de nacimiento.',
            }),
            'email': EmailInput(attrs={
                'placeholder': 'Ingrese su email.',
            }),
            'username': TextInput(attrs={
                'placeholder': 'Ingrese su username.',
            }),
            'password': PasswordInput(render_value=True, attrs={
                'placeholder': 'Ingrese su contraseña.',
            }),
        }

    def save(self, commit=True):
        data = {}
        try:
            instance = super(UserForm, self).save(commit=False)
            if self.is_valid():
                password = self.cleaned_data['password']
                if instance.id is None or User.objects.get(pk=instance.id).password != password:
                    instance.set_password(password)
                instance.save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
