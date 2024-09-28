# myapp/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = 'home'  # Przekierowanie po wylogowaniu na stronę główną

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class RegisterView(FormView):
    template_name = 'register.html'  # Bez prefixu, ponieważ jest w templates myapp
    form_class = RegisterForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            form.add_error('email', 'Użytkownik o tym adresie email już istnieje.')
            return self.form_invalid(form)
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

class LoginView(FormView):
    template_name = 'registration/login.html'  # Bez prefixu, ponieważ jest w templates myapp
    form_class = AuthenticationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect(self.get_success_url())

class DashboardView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')

    def get(self, request):
        return render(request, 'dashboard.html')

    def post(self, request):
        user_input = request.POST.get('user_input')
        context = {'user_input': user_input}
        return render(request, 'dashboard.html', context)
