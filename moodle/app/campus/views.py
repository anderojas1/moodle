from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Persona, MasterTeacher, SecretariaEducacion, LeaderTeacher

def index(request):
	return render_to_response('campus/index.html')

def success(request):
	return render_to_response('campus/success.html')


class RegistrarMasterTeacher(CreateView):
	template_name = 'campus/registrar.html'
	model = MasterTeacher
	fields = ['cedula', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'email', 'celular', 'fijo', 'experiencia']
	success_url = reverse_lazy('success')
	#model.enviarCorreo()


class ListarPersonas(ListView):
	template_name = 'campus/listados-personas.html'
	model = MasterTeacher
	context_object_name = 'masterteachers'


class RegistrarSecretariaEducacion(CreateView):
    template_name = 'campus/secretaria-educacion.html'
    model = SecretariaEducacion
    fields = ['codigo', 'entidadTerritorial', 'email', 'fijo', 'direccion']
    success_url = reverse_lazy('success')


class RegistrarLeaderTeacher(CreateView):
    template_name = 'campus/registrarLT.html'
    model = LeaderTeacher
    fields = ['cedula', 'nombre', 'apellidos', 'fecha_nacimiento', 'sexo', 'email', 'celular', 'fijo', 'areaAsignada', 'calificacion', 'certificado']
    success_url = reverse_lazy('success')


class listarLeaderTeacher(ListView):
    template_name = 'campus/listado-leader-teacher.html'
    model = LeaderTeacher
    context_object_name = 'leaderTeacher'
