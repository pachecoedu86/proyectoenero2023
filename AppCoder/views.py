from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import alummos

# Create your views here.

def inicio(request):
    return HttpResponse("hello welcome to my website.")


def agregar_alumno (request):
    alumno1 = alummos(nombre = "Eduardo" , apellido = "Pacheco" , emails = " eduardoarg149@gmail.com")
    alumno1.save()

    return HttpResponse("se ha agregado un alumno nuevo a la base de datos.")