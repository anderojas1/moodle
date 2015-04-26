from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Persona(models.Model):
	cedula = models.CharField(primary_key = True, max_length = 20)
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	sexo = models.CharField(max_length=20)
	email = models.CharField(max_length=50)
	celular = models.CharField(max_length=30, null=True, blank=True)
	fijo = models.CharField(max_length=30, null=True, blank=True)
	fecha_nacimiento = models.DateField()

	def __str__(self):
		return self.nombre


class MasterTeacher(Persona):
	experiencia = models.IntegerField(default=0, validators=[
		MaxValueValidator(80),
		MinValueValidator(0)])

	def __str__(self):
		return self.nombre

