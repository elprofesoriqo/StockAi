# myapp/urls.py
from django.urls import path
from .views import HomeView, RegisterView, LoginView, DashboardView, CustomLogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Strona główna
    path('register/', RegisterView.as_view(), name='register'),  # Rejestracja
    path('login/', LoginView.as_view(), name='login'),  # Logowanie
    path('dashboard/', DashboardView.as_view(), name='dashboard'),  # Dashboard po zalogowaniu
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Wylogowanie
]
