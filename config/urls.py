from django.contrib import admin
from django.urls import path
from dashboard.views import *
from game.views import *
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('userlist/', UserListView.as_view(), name='userlist'),
    path('increase_points/<int:user_id>/', IncreasePointsView.as_view(), name='increase_points'),
    path('decrease_points/<int:user_id>/', DecreasePointsView.as_view(), name='decrease_points'),
    path('games/', GameSelectView.as_view(), name='games'),
    path('spr/', SPRView.as_view(), name='spr'),
    path('headtails/', HeadTailsView.as_view(), name='headtails'),
    path("faq/", FaqView.as_view(), name="faq"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)