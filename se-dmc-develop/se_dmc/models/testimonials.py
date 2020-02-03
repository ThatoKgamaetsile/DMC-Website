from django.db import models


class Testimonial(models.Model):
    
    full_name = models.CharField(max_length=200, verbose_name='Full names')
    position  = models.CharField(max_length=200, verbose_name='Position')
    image = models.ImageField(verbose_name='Profile picture')



