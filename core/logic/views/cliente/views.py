import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from core.logic.forms import ClienteForm
from core.logic.models import Cliente

MODULE_NAME = 'Clientes'


class ClienteTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'cliente/list.html'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_clientes':
                start = int(request.POST.get('start', 0))
                length = int(request.POST.get('length', 10))
                term = request.POST.get('search[value]', '')
                clientes = Cliente.objects.all()
                if term:
                    clientes = clientes.filter(dni__startswith=term)
                paginator = Paginator(clientes, length)
                get_number = start // length + 1
                cliente_page = paginator.get_page(get_number)
                data = {
                    'clientes': [c.toJSON() | {'index': index} for index, c in enumerate(cliente_page, start=start + 1)],
                    'draw': int(request.POST.get('draw', 1)),
                    'recordsTotal': paginator.count,
                    'recordsFiltered': paginator.count
                }
            else:
                data['error'] = 'Ha ocurrido un error al devolver el listado de clientes.'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super(ClienteTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Listado de clientes'
        context['entity'] = MODULE_NAME
        context['create_url'] = reverse_lazy('logic:cliente_create')
        return context


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/create.html'
    success_url = reverse_lazy('logic:cliente_list')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'create':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Ha ocurrido un error al guardar el cliente.'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Creación de cliente'
        context['entity'] = MODULE_NAME
        context['action'] = 'create'
        context['list_url'] = self.success_url
        return context


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/create.html'
    success_url = reverse_lazy('logic:cliente_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ClienteUpdateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Ha ocurrido un error al actualizar al cliente.'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super(ClienteUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Edicción de Cliente'
        context['action'] = 'update'
        context['entity'] = MODULE_NAME
        context['list_url'] = self.success_url
        return context


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'delete.html'
    success_url = reverse_lazy('logic:cliente_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ClienteDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'delete':
                self.object.delete()
            else:
                data['error'] = 'Ha ocurrido un error al eliminar el cliente.'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super(ClienteDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Eliminar Cliente'
        context['action'] = 'delete'
        context['entity'] = MODULE_NAME
        context['list_url'] = self.success_url
        return context
