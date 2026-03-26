from django.contrib import admin
from .models import Experiencia, Formacion, Proyecto

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display  = ('puesto', 'empresa', 'periodo')
    search_fields = ('puesto', 'empresa')
    ordering      = ('-periodo',)

@admin.register(Formacion)
class FormacionAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'institucion', 'periodo')
    search_fields = ('titulo', 'institucion')
    ordering      = ('-periodo',)

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display  = ('titulo', 'orden')
    search_fields = ('titulo', 'tecnologias')
    list_filter   = ('orden',)
    ordering      = ('orden',)

# --- Personalización del encabezado del panel ---
admin.site.site_header = "Admin — Tu Nombre Aquí"  # ← reemplaza con tu nombre
admin.site.site_title  = "Mi CV Admin"
admin.site.index_title = "Panel de Control del CV"
