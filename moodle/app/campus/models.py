from django.db import models

# Create your models here.
class Persona(models.Model):
	cedula = models.CharField(primary_key = True, max_length = 20)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	sexo = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	celular = models.CharField(max_length=30)
	fijo = models.CharField(max_length=30)
	fecha_nacimiento = models.DateField()

	def __str__(self):
		return self.nombre


class MasterTeacher(Persona, models.Model):
	experiencia = models.CharField(max_length = 5)

	def __str__(self):
		return self.nombre
