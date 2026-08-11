from django.shortcuts import render
from django.contrib import messages
from registros.models import Alumnos
import datetime
from .models import Archivo
from .forms import FormArchivos


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


def consultas(request):
    return render(request, "inicio/consultas.html")


def consultas1(request):
    alumnos = Alumnos.objects.filter(carrera="TI")

    return render(
        request,
        "inicio/consultas.html",
        {"alumnos": alumnos}
    )


def consultas2(request):
    alumnos = Alumnos.objects.filter(
        carrera="TI"
    ).filter(
        turno="matutino"
    )

    return render(
        request,
        "inicio/consultas.html",
        {"alumnos": alumnos}
    )


def consultarTurno(request):
    alumnos = Alumnos.objects.filter(turno="matutino")

    return render(
        request,
        "inicio/consultas.html",
        {"alumnos": alumnos}
    )


def consultarCarrera(request):
    alumnos = Alumnos.objects.filter(carrera="TI")

    return render(
        request,
        "inicio/consultas.html",
        {"alumnos": alumnos}
    )


def consultar5(request):
    alumnos = Alumnos.objects.filter(
        nombre__in=["Juan", "Ana"]
    )

    return render(
        request,
        "inicio/consultas.html",
        {"alumnos": alumnos}
    )


def consultar6(request):
    fechaInicio = datetime.date(2025, 1, 1)
    fechaFin = datetime.date(2026, 12, 31)

    alumnos = Alumnos.objects.filter(
        created__range=(fechaInicio, fechaFin)
    )

    return render(
        request,
        "inicio/consultas.html",
        {"alumnos": alumnos}
    )


def consultar7(request):
    alumnos = Alumnos.objects.filter(
        comentario__coment__contains="No inscrito"
    )

    return render(
        request,
        "inicio/consultas.html",
        {"alumnos": alumnos}
    )


def consultasSQL(request):
    alumnos = Alumnos.objects.raw("""
        SELECT id,
               matricula,
               nombre,
               carrera,
               turno,
               imagen
        FROM registros_alumnos
        ORDER BY turno DESC
    """)

    return render(
        request,
        "inicio/consultas.html",
        {"alumnos": alumnos}
    )


def archivos(request):

    if request.method == "POST":

        form = FormArchivos(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Archivo guardado correctamente"
            )

        else:

            messages.error(
                request,
                "Error al procesar el formulario"
            )

    else:

        form = FormArchivos()

    archivos = Archivo.objects.all()

    return render(
        request,
        "inicio/archivos.html",
        {
            "form": form,
            "archivos": archivos
        }
    )