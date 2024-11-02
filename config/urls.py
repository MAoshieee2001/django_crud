from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('core/', include('core.logic.urls')),
                  path('', include('core.login.urls')),
                  path('dashboard/', include('core.dashboard.urls')),
                  path('account/', include('core.account.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
