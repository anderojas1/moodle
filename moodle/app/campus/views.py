from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from .models import Persona

def index(request):
	return render_to_response('campus/index.html')

def success(request):
	return render_to_response('campus/success.html')


class RegistrarPersona(CreateView):
	template_name = 'campus/registrar.html'
	model = Persona
	fields = ['cedula', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'email', 'celular', 'fijo']
	success_url = reverse_lazy('success')