from django.db import models

class Experiencia(models.Model):
    periodo = models.CharField(max_length=50, verbose_name="Periodo (Ej: 2022 - Presente)")
    puesto = models.CharField(max_length=100, verbose_name="Puesto o Cargo")
    empresa = models.CharField(max_length=100, verbose_name="Empresa")
    descripcion = models.TextField(verbose_name="Descripción de tareas")
    tecnologias = models.CharField(max_length=200, blank=True, null=True, help_text="Separadas por comas.")
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name_plural = "Experiencias"

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"

    def listahabilidades(self):
        return [tec.strip() for tec in self.tecnologias.split(',')] if self.tecnologias else []


class Formacion(models.Model):
    periodo = models.CharField(max_length=50, verbose_name="Periodo")
    titulo = models.CharField(max_length=100, verbose_name="Título o Certificado")
    institucion = models.CharField(max_length=100, verbose_name="Institución")
    descripcion = models.TextField(blank=True, null=True)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name_plural = "Formaciones"

    def __str__(self):
        return self.titulo


class Proyecto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título del Proyecto")
    descripcion = models.TextField()
    enlace_github = models.URLField(blank=True, null=True, verbose_name="Enlace de GitHub")
    enlace_sitio = models.URLField(blank=True, null=True, verbose_name="Enlace del Sitio")
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    tecnologias = models.CharField(max_length=200, help_text="Separadas por comas.")
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.titulo

    def listatecnologias(self):
        return [tec.strip() for tec in self.tecnologias.split(',')] if self.tecnologias else []


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=150)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre}"

class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    bio = models.TextField()

