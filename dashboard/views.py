from django.shortcuts import render , redirect , get_object_or_404 
from django.urls import reverse
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
            return redirect('/profile', {"user" : user})
        else:
            return HttpResponse('Invalid Form')
        


class UserListView(View):
    def get(self, request):

        # users = UserProfile.objects.filter(username=request.user)
        users = UserProfile.objects.all()
        context = {
            'users': users
        }
        return render(request, 'userlist.html', context)
    


class IncreasePointsView(View):
    def post(self, request, user_id):
        user = get_object_or_404(UserProfile, pk=user_id)
        new_points = user.points + 1

        # Validate points
        if new_points <= 10:
            user.points = new_points
            user.save()
        else:
            error_message = "Error: Points cannot exceed 10."
            return self.error_response(request, error_message)

        return redirect(reverse('userlist'))

    def error_response(self, request, error_message):
        # Add error message to context and render inline error message
        users = UserProfile.objects.all()  # You may need to adjust this query based on your actual model
        return render(request, 'userlist.html', {'users': users, 'error_message': error_message})

class DecreasePointsView(View):
    def post(self, request, user_id):
        user = get_object_or_404(UserProfile, pk=user_id)
        new_points = user.points - 1

        # Validate points
        if new_points >= 0:
            user.points = new_points
            user.save()
        else:
            error_message = "Error: Points cannot be less than 0."
            return IncreasePointsView().error_response(request, error_message)

        return redirect(reverse('userlist'))
    

class GameSelectView(View):
    def get(self, request):
        return render(request, 'gameselect.html')
    


class FaqView(View):
    def get(self, request):
        return render(request, 'faq.html')
    
class InvoiceView(View):
    def get(self, request):
        return render(request, 'invoice.html')