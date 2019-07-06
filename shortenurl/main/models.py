from django.db import models

# Create your models here.
class URLPair(models.Model):
    initial_url = models.CharField(max_length=512)
    new_url = models.CharField(max_length=128)
