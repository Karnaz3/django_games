from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from userprofiles.models import UserProfile
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
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'register.html', {'form': form})
        
class ForgotPasswordView(View):
    def get(self, request):
        return render(request, 'forgot-password.html')
    
    def post(self, request):
        pass

class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')
    



class ProfileView(View):
    def get(self, request):
        user = self.request.user
        context = { 'user': user }
        return render(request, 'profile.html', context)
    
    def post(self, request , *args, **kwargs):
        user = self.request.user
        user_form = ProfilePhotoForm(self.request.POST, self.request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/profile')
        


class UserListView(ListView):
    model = get_user_model()
    template_name = 'userlist.html'
    context_object_name = 'users'
    paginate_by = 10
    ordering = ['username']

    def get_queryset(self):
        return get_user_model().objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context variables if needed
        return context
