from django.db import models


class Testimonial(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='Full names')
    description = models.CharField(max_length=200, verbose_name='Description')
    image = models.ImageField(verbose_name='Profile picture')

    def __str__(self):
        return self.full_name
