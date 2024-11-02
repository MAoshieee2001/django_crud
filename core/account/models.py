from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

from django.forms import model_to_dict


class User(AbstractUser):
    imagen = models.ImageField(upload_to='users/', blank=True, null=True, verbose_name='Imagen')
    fecha_nacimiento = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'is_staft', 'groups', 'is_superuser', 'user_permissions', 'imagen'])
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%Y-%m-%d')
        item['last_login'] = self.last_login.strftime('%Y-%m-%d') if self.last_login else ''
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d') if self.last_login else ''
        item['full_names'] = self.get_full_name()
        return item

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['id']
