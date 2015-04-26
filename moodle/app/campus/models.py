from django.db import models
#from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Persona(models.Model):
	cedula = models.CharField(primary_key = True, max_length = 20)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	sexo = models.CharField(max_length=20)
	email = models.EmailField(max_length=50)
	celular = models.CharField(max_length=30, null=True, blank=True)
	fijo = models.CharField(max_length=30, null=True, blank=True)
	fecha_nacimiento = models.DateField()

	def __str__(self):
		return self.nombre

	#def enviarCorreo():
	#	print("correoenviado %s" % email)


class MasterTeacher(Persona):
	experiencia = models.PositiveIntegerField()

	def __str__(self):
		return self.nombre


