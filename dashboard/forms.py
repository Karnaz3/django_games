from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from userprofiles.models import UserProfile

class ProfilePhotoForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserProfile  # Use your custom user model
        fields = ['username', 'password1', 'password2']  # You can customize the fields if needed