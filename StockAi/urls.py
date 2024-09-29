# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Stock.urls')),  # Przekierowanie do myapp.urls, gdzie obsługujemy home i dashboard
    path('accounts/', include('django.contrib.auth.urls')),  # Logowanie
]
