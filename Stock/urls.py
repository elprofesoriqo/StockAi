# myapp/urls.py
from django.urls import path
from .views import HomeView, RegisterView, LoginView, DashboardView, CustomLogoutView, ProfileView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Strona główna
    path('register/', RegisterView.as_view(), name='register'),  # Rejestracja
    path('login/', LoginView.as_view(), name='login'),  # Logowanie
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Wylogowanie
    path('accounts/profile/', ProfileView, name='profile'),  # Profil użytkownika
    path('accounts/dashboard/', DashboardView.as_view(), name='dashboard'),  # Dashboard
]
