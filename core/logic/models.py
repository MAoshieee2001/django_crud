from datetime import datetime

from django.forms import model_to_dict

from core.logic.choices import choices_genero

from django.db import models


class Cliente(models.Model):
    nombres = models.CharField(max_length=144, verbose_name='Nombres')
    apellidos = models.CharField(max_length=255, verbose_name='Apellidos')
    dni = models.CharField(max_length=8, unique=True, verbose_name='DNI', help_text='Nunca compartiremos su DNI.')
    fecha_nacimiento = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    genero = models.BooleanField(default=True, choices=choices_genero, verbose_name='Género')

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha_nacimiento'] = self.fecha_nacimiento.strftime('%Y-%m-%d')
        item['genero'] = {'id': self.genero, 'names': self.get_genero_display()}
        return item

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
