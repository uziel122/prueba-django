"""
URL configuration for prueba project.
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings

from inicio.views import principal
from inicio.views import formulario
from inicio.views import nombre
from inicio.views import ejemplo

from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', principal, name='principal'),
    path('nombre/', nombre, name='nombre'),
    path('contacto/', views_registros.contacto, name='contacto'),
    path('formulario/', formulario, name='formulario'),
    path('ejemplo/', ejemplo, name='ejemplo'),

    # Registrar comentario
    path('registrar/', views_registros.registrar, name='Registrar'),

    # Nueva consulta de comentarios
    path(
        'consultaContacto/',
        views_registros.consultaContacto,
        name='consultaContacto'
    ),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )