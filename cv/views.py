from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Proyecto, Experiencia, Formacion, MensajeContacto
from .forms import ContactoForm, ExperienciaForm, FormacionForm, ProyectoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required, permission_required


def inicio(request):
    proyectos = Proyecto.objects.all()
    experiencia = Experiencia.objects.all()
    formacion = Formacion.objects.all()
    
    form_contacto = ContactoForm()

    contexto = {
        'nombre': 'Tu Nombre',
        'profesion': 'Desarrollador Web Full Stack',
        'sobre_mi': 'Hola. Me gusta crear cosas para la web.',
        'email': 'tu.correo@email.com',
        'github': 'https://github.com/tu-usuario',
        'proyectos': proyectos,
        'experiencia': experiencia,
        'formacion': formacion,
        'form_contacto': form_contacto,
    }
    
    return render(request, 'cv/inicio.html', contexto)

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Mensaje enviado correctamente!')
            return redirect('inicio')
    return redirect('inicio')

@login_required
@permission_required('cv.change_experiencia', raise_exception=True)
def editar_experiencia(request, pk):
    experiencia = get_object_or_404(Experiencia, pk=pk)
    if request.method == 'POST':
        form = ExperienciaForm(request.POST, instance=experiencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Experiencia actualizada.')
            return redirect('inicio')
    else:
        form = ExperienciaForm(instance=experiencia)
    return render(request, 'cv/formulario_edicion.html', {'form': form, 'titulo_seccion': 'Editar Experiencia'})

@login_required
@permission_required('cv.change_formacion', raise_exception=True)
def editar_formacion(request, pk):
    formacion = get_object_or_404(Formacion, pk=pk)
    if request.method == 'POST':
        form = FormacionForm(request.POST, instance=formacion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formación actualizada.')
            return redirect('inicio')
    else:
        form = FormacionForm(instance=formacion)
    return render(request, 'cv/formulario_edicion.html', {'form': form, 'titulo_seccion': 'Editar Formación'})

@login_required
@permission_required('cv.change_proyecto', raise_exception=True)
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES, instance=proyecto) # request.FILES es vital para la imagen
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto actualizado.')
            return redirect('inicio')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'cv/formulario_edicion.html', {'form': form, 'titulo_seccion': 'Editar Proyecto'})

def contacto_gracias(request):
    return render(request, 'cv/gracias.html')


@login_required
@permission_required('cv.add_proyecto', raise_exception=True)
def agregar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save() # Como no hay 'instance', Django CREA un nuevo registro
            messages.success(request, '¡Proyecto añadido correctamente!')
            return redirect('inicio')
    else:
        form = ProyectoForm()        
    return render(request, 'cv/formulario_edicion.html', {
        'form': form,
        'titulo_seccion': 'Añadir Nuevo Proyecto'
    })

@login_required
@permission_required('cv.add_experiencia', raise_exception=True)
def agregar_experiencia(request):
    if request.method == 'POST':
        form = ExperienciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Experiencia añadida correctamente!')
            return redirect('inicio')
    else:
        form = ExperienciaForm()
        
    return render(request, 'cv/formulario_edicion.html', {
        'form': form,
        'titulo_seccion': 'Añadir Nueva Experiencia'
    })

@login_required
@permission_required('cv.add_formacion', raise_exception=True)
def agregar_formacion(request):
    if request.method == 'POST':
        form = FormacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Formación añadida correctamente!')
            return redirect('inicio')
    else:
        form = FormacionForm()
        
    return render(request, 'cv/formulario_edicion.html', {
        'form': form,
        'titulo_seccion': 'Añadir Nueva Formación'
    })
