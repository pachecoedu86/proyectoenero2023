from django.db import models

# Create your models here.


class alummos(models.Model):
    nombre = models.CharField(max_length=40)   # lee mensajes de texto pequeños
    apellido = models.CharField(max_length=40)
    emails = models.EmailField()

