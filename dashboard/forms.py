from django.forms import ModelForm
from django import forms
from userprofiles.models import UserProfile

class ProfilePhotoForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']


class UserRegisterForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'