from django.db import models


class Team(models.Model):
    
    full_name = models.CharField(max_length=200, verbose_name='Full names')
    position  = models.CharField(max_length=200, verbose_name='Position')
    description = models.CharField(max_length=200, verbose_name='Description')
    facebook = models.CharField(max_length=200, verbose_name='Facebook profile')
    linkedin = models.CharField(max_length=200, verbose_name='LinkedIn profile')
    github = models.CharField(max_length=200, verbose_name='Github profile')
    tweeter = models.CharField(max_length=200, verbose_name='Tweeter profile')
    image = models.ImageField(verbose_name='Profile picture')

    def __str__(self):
        return self.full_name