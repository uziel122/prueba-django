from django.contrib import admin
from .models import Alumnos, Comentario
from .models import ComentarioContacto

# Administración de Alumnos
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    list_filter = ('carrera', 'turno')

# Administración de Comentarios
class AdministrarComentario(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('id', 'alumno', 'created')
    search_fields = ('alumno__nombre',)
    list_filter = ('created',)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)

admin.site.register(Alumnos, AdministrarModelo)
admin.site.register(Comentario, AdministrarComentario)