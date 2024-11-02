from django.urls import path

from core.logic.views.cliente.views import *

app_name = 'logic'

urlpatterns = [
    path('cliente/', ClienteTemplateView.as_view(), name='cliente_list'),
    path('cliente/create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('cliente/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('cliente/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_delete'),
]
