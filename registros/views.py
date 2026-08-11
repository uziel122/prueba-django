from django.shortcuts import render, get_object_or_404, redirect
from .forms import ComentarioContactoForm
from .models import ComentarioContacto

def contacto(request):
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {"form": form})


def registrar(request):
    if request.method == "POST":
        form = ComentarioContactoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("consultaContacto")

    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {"form": form})


def consultaContacto(request):
    comentarios = ComentarioContacto.objects.all()

    return render(
        request,
        "registros/consultaContacto.html",
        {
            "comentarios": comentarios
        }
    )


def eliminarComentarioContacto(
    request,
    id,
    confirmacion="registros/confirmarEliminacion.html"
):
    comentario = get_object_or_404(ComentarioContacto, id=id)

    if request.method == "POST":
        comentario.delete()
        return redirect("consultaContacto")

    return render(
        request,
        confirmacion,
        {
            "object": comentario
        }
    )


# Mostrar el formulario con los datos del comentario
def consultarComentarioIndividual(request, id):
    comentario = get_object_or_404(
        ComentarioContacto,
        id=id
    )

    form = ComentarioContactoForm(instance=comentario)

    return render(
        request,
        "registros/formEditarComentario.html",
        {
            "comentario": comentario,
            "form": form
        }
    )


# Guardar los cambios del comentario
def editarComentarioContacto(request, id):
    comentario = get_object_or_404(
        ComentarioContacto,
        id=id
    )

    if request.method == "POST":

        form = ComentarioContactoForm(
            request.POST,
            instance=comentario
        )

        if form.is_valid():
            form.save()
            return redirect("consultaContacto")

    else:
        form = ComentarioContactoForm(instance=comentario)

    return render(
        request,
        "registros/formEditarComentario.html",
        {
            "comentario": comentario,
            "form": form
        }
    )