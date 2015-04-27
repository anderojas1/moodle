from django.conf.urls import include, url
from .views import success
from .views import RegistrarCurso, RegistrarCohorte

urlpatterns = [
    url(r'^registrar-curso/$', RegistrarCurso.as_view(), name='registar_curso'),
    url(r'^registrar-cohorte/$', RegistrarCohorte.as_view(), name='registar_cohorte'),
]