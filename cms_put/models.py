from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pages(models.Model):
    nombre = models.CharField(max_length = 32)
    contenido = models.TextField()
