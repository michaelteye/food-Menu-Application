from tabnanny import verbose
from django.db import models
from django.urls import reverse
# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=2260)
    price = models.FloatField()
    discount_price = models.FloatField()
    time = models.DateTimeField(auto_now=True, blank=True)
    image = models.ImageField(upload_to = 'images', default = 'profile_pics/default.jpg')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Menu'

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])