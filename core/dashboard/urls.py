from django.urls import path

from core.dashboard.views import DashboardTemplateView

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='dashboard'),
]
