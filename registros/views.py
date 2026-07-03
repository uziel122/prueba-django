from django.shortcuts import render
from .forms import ComentarioContactoForm
from .models import ComentarioContacto


def contacto(request):
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {"form": form})


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)

        if form.is_valid():
            form.save()

            comentarios = ComentarioContacto.objects.all()

            return render(
                request,
                "registros/consultaContacto.html",
                {"comentarios": comentarios}
            )

    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {"form": form})


def consultaContacto(request):
    comentarios = ComentarioContacto.objects.all()

    return render(
        request,
        "registros/consultaContacto.html",
        {"comentarios": comentarios}
    )