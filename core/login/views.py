import json

from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView, RedirectView

from config import settings
from core.login.forms import LoginForm


class LoginTemplateView(FormView):
    form_class = LoginForm
    template_name = 'login/login.html'
    success_url = settings.LOGIN_REDIRECT_URL

    def dispatch(self, request, *args, **kwargs):
        return redirect(self.success_url) if request.user.is_authenticated else super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(user=form.get_user(), request=self.request)
        return super(LoginTemplateView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'cerrar_sesion':
                logout(request)
            else:
                data['error'] = 'Ha ocurrido un error al cerrar sesión.'
        except Exception as e:
            data['error'] = str(e)
        return HttpResponse(json.dumps(data), content_type='application/json')
