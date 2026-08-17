"""
URL configuration for prueba project.
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings

from inicio.views import (
    principal,
    formulario,
    nombre,
    ejemplo,
    consultas,
    consultas1,
    consultas2,
    consultarTurno,
    consultarCarrera,
    consultar5,
    consultar6,
    consultar7,
    consultasSQL,
    archivo,
)

from registros import views as views_registros


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', principal, name='principal'),
    path('nombre/', nombre, name='nombre'),
    path('contacto/', views_registros.contacto, name='contacto'),
    path('formulario/', views_registros.registrar, name='formulario'),
    path('ejemplo/', ejemplo, name='ejemplo'),

    # Registrar comentario
    path('registrar/', views_registros.registrar, name='Registrar'),

    # Consulta de comentarios
    path(
        'consultaContacto/',
        views_registros.consultaContacto,
        name='consultaContacto'
    ),

    # Eliminar comentario
    path(
        'eliminarComentario/<int:id>/',
        views_registros.eliminarComentarioContacto,
        name='Eliminar'
    ),

    # Consulta individual
    path(
        'formEditarComentario/<int:id>/',
        views_registros.consultarComentarioIndividual,
        name='ConsultaIndividual'
    ),

    # Editar comentario
    path(
        'editarComentario/<int:id>/',
        views_registros.editarComentarioContacto,
        name='Editar'
    ),

    # Consultas
    path('consultas/', consultas, name='consultas'),
    path('consultas1/', consultas1, name='consultas1'),
    path('consultas2/', consultas2, name='consultas2'),
    path('consultarTurno/', consultarTurno, name='consultarTurno'),
    path('consultarCarrera/', consultarCarrera, name='consultarCarrera'),
    path('consultas5/', consultar5, name='Consulta5'),
    path('consultas6/', consultar6, name='Consulta6'),
    path('consultas7/', consultar7, name='Consulta7'),
    path('consultasSQL/', consultasSQL, name='sql'),

    # Subir archivos
    path('subir/', archivo, name='Subir'),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )