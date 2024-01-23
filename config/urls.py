from django.contrib import admin
from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]