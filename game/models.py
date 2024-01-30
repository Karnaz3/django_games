from django.db import models

class SPR(models.Model):
    user_choice = models.CharField(max_length=10)
    computer_choice = models.CharField(max_length=10)
    winner = models.CharField(max_length=10)

class HeadTails(models.Model):
    result = models.CharField(max_length=10)

