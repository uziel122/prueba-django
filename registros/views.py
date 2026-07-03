from django.shortcuts import render
from .forms import ComentarioContactoForm 

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)

        if form.is_valid():  # Si los datos recibidos son correctos
            form.save()      # Inserta en la base de datos
            return render(request, 'registros/contacto.html')

    form = ComentarioContactoForm()

    # Si sale mal se reenvían al formulario los datos ingresados
    return render(request, 'registros/contacto.html', {'form': form})

def contacto (request):
    return render(request,"registros/contacto.html")