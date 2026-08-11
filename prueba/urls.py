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
from inicio.views import consultas
from inicio.views import consultas1
from inicio.views import consultas2
from inicio.views import consultarTurno
from inicio.views import consultarCarrera
from inicio.views import consultar5
from inicio.views import consultar6
from inicio.views import consultar7
from inicio.views import consultasSQL
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
    path('consultaContacto/',views_registros.consultaContacto,name='consultaContacto'),

    #Eliminar Comentario
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto, name='Eliminar'),
    
    path('formEditarComentario/<int:id>/',views_registros.consultarComentarioIndividual,name='ConsultaIndividual'),
    
    #Editar Comentario
    path('editarComentario/<int:id>/',views_registros.editarComentarioContacto,name='Editar'),
    
    
    path('consultas/', consultas, name='consultas'),

    path('consultas1', consultas1, name='consultas1'),

    path('consultas2',consultas2, name='consultas2'),

    path('consultarTurno/', consultarTurno, name='consultarTurno'),

    path('consultarCarrera/', consultarCarrera, name='consultarCarrera'),

    path('consultas5/', consultar5, name='Consulta5'),

    path('consultas6/', consultar6, name='Consulta6'),

    path('consultas7/', consultar7, name='Consulta7'),

    path('consultasSQL/', consultasSQL, name='sql'),

    path('subir', views_registros.archivos, name="Subir"),
    ]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )