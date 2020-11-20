'''DB models for the website'''
from django.db import models


class URLPair(models.Model):
    """
    Pair of initial and converted urls. Only code is stored
    Example:
    initial_url => http://example.com
    new_url => BNF30GE
    """
    initial_url = models.CharField(max_length=512)
    new_url = models.CharField(max_length=128)
