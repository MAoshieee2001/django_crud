import json

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView, TemplateView, CreateView, DeleteView, FormView

from core.account.forms import MyProfileForm, UserForm
from core.account.models import User


class MyProfileUserTemplateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = MyProfileForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return self.request.user

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(MyProfileUserTemplateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Ha ocurrido un error al actualizar el perfil del usuario.'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super(MyProfileUserTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Mi perfil de usuario'
        context['entity'] = 'Usuario'
        context['list_url'] = self.success_url
        context['action'] = 'update'
        return context


class UserTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'user/list.html'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_users':
                start = int(request.POST.get('start', 0))
                length = int(request.POST.get('length', 10))
                term = request.POST.get('search[value]', '')
                users = User.objects.all()
                if term:
                    users = users.filter(username__startswith=term)
                paginator = Paginator(users, length)
                get_num = start // length + 1
                user_page = paginator.get_page(get_num)
                data = {
                    'draw': int(request.POST.get('draw', 1)),
                    'user_list': [u.toJSON() | {'index': index} for index, u in enumerate(user_page, start=start + 1)],
                    'recordsTotal': paginator.count,
                    'recordsFiltered': paginator.count
                }
            else:
                data['error'] = 'Ha ocurrido un error al obtener el listado de usuarios.'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super(UserTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Listado de usuarios'
        context['entity'] = 'Usuarios'
        context['list_url'] = reverse_lazy('account:user_list')
        context['create_url'] = reverse_lazy('account:user_create')
        return context


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'create':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Ha ocurrido un error al crear el usuario.'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Creación de usuario'
        context['entity'] = 'Usuario'
        context['action'] = 'create'
        context['list_url'] = self.success_url
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('account:user_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'update':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'Ha ocurrido al actualizar el usuario.'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Actualización de usuario'
        context['entity'] = 'Usuario'
        context['action'] = 'update'
        context['list_url'] = self.success_url
        return context


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('account:user_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'delete':
                self.object.delete()
            else:
                data['error'] = 'Ha ocurrido al eliminar el usuario.'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='json')

    def get_context_data(self, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Eliminación de usuario'
        context['entity'] = 'Usuario'
        context['action'] = 'delete'
        context['list_url'] = self.success_url
        return context


class UserPasswordChangeView(LoginRequiredMixin, FormView):
    form_class = PasswordChangeForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('dashboard')

    def get_form(self, form_class=None):
        form = PasswordChangeForm(user=self.request.user)
        return form

    def get_context_data(self, **kwargs):
        context = super(UserPasswordChangeView, self).get_context_data(**kwargs)
        context['title'] = 'Actualización de contraseña'
        context['entity'] = 'Contraseña'
        context['action'] = 'update'
        context['list_url'] = self.success_url
        return context
