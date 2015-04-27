from django.db import models

# Create your models here.
class Curso(models.Model):
	codigo = models.CharField(primary_key=True, max_length=15)
	nombre = models.CharField(max_length=100)
	area = models.CharField(max_length=40)

	def __str__(self):
		return self.nombre

class Cohorte(models.Model):
	curso = models.ForeignKey(Curso)
	