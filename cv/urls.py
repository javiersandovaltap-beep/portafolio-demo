from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('contacto/gracias/', views.contacto_gracias, name='contacto_gracias'),
    
    # Rutas de EDICIÓN
    path('experiencia/editar/<int:pk>/', views.editar_experiencia, name='editar_experiencia'),
    path('formacion/editar/<int:pk>/', views.editar_formacion, name='editar_formacion'),
    path('proyecto/editar/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),
    
    # NUEVAS RUTAS DE CREACIÓN (AÑADIR)
    path('proyecto/agregar/', views.agregar_proyecto, name='agregar_proyecto'),
    path('experiencia/agregar/', views.agregar_experiencia, name='agregar_experiencia'),
    path('formacion/agregar/', views.agregar_formacion, name='agregar_formacion'),
]
