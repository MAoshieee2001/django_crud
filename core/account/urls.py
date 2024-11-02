from django.urls import path

from core.account.views.user.views import *

app_name = 'account'

urlpatterns = [
    path('my/', MyProfileUserTemplateView.as_view(), name='my_profile'),
    path('', UserTemplateView.as_view(), name='user_list'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('change/password/', UserPasswordChangeView.as_view(), name='user_password_change'),
]
