from django.contrib import admin

# Register your models here.
from core.account.models import User

admin.site.register(User)