from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(self.request, user)
            return redirect('/dashboard')
        else:
            context = {
                'error': 'Invalid username or password'
            }
            return render(request, 'login.html', context)
    

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    
    def post(self, request):
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        pass

class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'forgot-password.html')
    
    def post(self, request):
        pass

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')
    



