from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from game.models import SPR, HeadTails


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
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    points = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )
    
    # Add any additional fields you want here

    objects = UserProfileManager()

    USERNAME_FIELD = 'username'  # Specify the field to be used as the unique identifier

    def __str__(self):
        """ Return string representation of our user """
        return self.username

    def play_spr(self, user_choice):
            spr_game = SPR()
            result = spr_game.execute(user_choice)

            self.points += 1 if result['winner'] == 'User' else 0

            self.last_spr_user_choice = result['user_choice']
            self.last_spr_computer_choice = result['computer_choice']
            self.last_spr_winner = result['winner']

            self.save()

            return result

    def play_ht(self):
        ht_game = HeadTails()
        result = ht_game.execute()

        self.points += 1 if result == 'head' else 0

        self.last_ht_result = result

        self.save()

        return result