from django.urls import path

from core.login.views import LoginTemplateView, LogoutView

urlpatterns = [
    path('', LoginTemplateView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
