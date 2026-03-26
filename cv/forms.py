from django import forms
from .models import Experiencia, Formacion, Proyecto, MensajeContacto

class ExperienciaForm(forms.ModelForm):
    class Meta:
        model = Experiencia
        fields = ['periodo', 'puesto', 'empresa', 'descripcion', 'tecnologias']
        widgets = {
            'periodo': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tecnologias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Python, Django'}),
        }

class FormacionForm(forms.ModelForm):
    class Meta:
        model = Formacion
        fields = ['periodo', 'titulo', 'institucion', 'descripcion']
        widgets = {
            'periodo': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'enlace_github', 'enlace_sitio', 'imagen', 'tecnologias']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'enlace_github': forms.URLInput(attrs={'class': 'form-control'}),
            'enlace_sitio': forms.URLInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'tecnologias': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
