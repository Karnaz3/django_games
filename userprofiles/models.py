from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserProfileManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """ Create a new user profile """
        if not username:
            raise ValueError('User must have a username')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        """ Create a new superuser profile """
        user = self.create_user(username, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    username = models.CharField(max_length=255, unique=True)
    profile_picture = models.ImageField(upload_to='uploads/profile', null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    # Add any additional fields you want here

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'  # Specify the field to be used as the unique identifier

    def __str__(self):
        """ Return string representation of our user """
        return self.username
