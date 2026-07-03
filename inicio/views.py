from django.shortcuts import render
from registros.models import Alumnos

def principal(request):
    alumnos = Alumnos.objects.all()

    return render(request, "registros/principal.html", {
        'titulo_pagina': 'Principal',
        'imagen_pagina': 'inicio/images/home.png',
        'alumnos': alumnos
    })

def nombre(request):
    return render(request, "inicio/nombre.html", {
        'titulo_pagina': 'Nombre'
    })

def contacto(request):
    return render(request, "inicio/contacto.html", {
        'titulo_pagina': 'Contacto',
        'imagen_pagina': 'inicio/images/contacto.png'
    })

def formulario(request):
    return render(request, "inicio/formulario.html", {
        'titulo_pagina': 'Formulario',
        'imagen_pagina': 'inicio/images/registrar.png'
    })

def ejemplo(request):
    return render(request, "inicio/ejemplo.html", {
        'titulo_pagina': 'Ejemplo'
    })