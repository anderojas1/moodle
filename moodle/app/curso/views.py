from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Curso

# Create your views here.

def success(request):
	return render_to_response('curso/success.html')

class RegistrarCurso(CreateView):
	template_name =  'curso/registrar-curso.html'
	model = Curso
	fields = ['codigo', 'nombre', 'area']
	success_url = reverse_lazy('success')