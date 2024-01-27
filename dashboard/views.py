from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
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
        return render(request, 'register.html')
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = UserProfile.objects.create_user(username=username)
        user.set_password(password)
        user.save()
        return redirect('/')
    
        
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
        user = request.user
        context = { 
            'user': user 
            }
        print(user.profile_picture)
        return render(request, 'profile.html', context)
    
    def post(self, request):
        user = request.user
        user_form = ProfilePhotoForm(request.POST ,  request.FILES , instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('/profile')
        else:
            return HttpResponse('Invalid Form')
        


class UserListView(View):
    def get(self, request):
        users = UserProfile.objects.all()
        context = { 
            'users': users
            }
        return render(request, 'userlist.html', context)
    

