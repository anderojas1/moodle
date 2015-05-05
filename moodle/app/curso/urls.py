from django.conf.urls import include, url
from .views import success
from .views import RegistrarCurso, RegistrarCohorte, ListarCursos, ListarCohortes

urlpatterns = [
    url(r'^registrar-curso/$', RegistrarCurso.as_view(), name='registar_curso'),
    url(r'^registrar-cohorte/$', RegistrarCohorte.as_view(), name='registar_cohorte'),
    url(r'^listar-curso/$', ListarCursos.as_view(), name='listar_cursos'),
    url(r'^listar-cohorte/$', ListarCohortes.as_view(), name='listar_cohortes')
]