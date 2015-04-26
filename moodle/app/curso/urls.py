from django.conf.urls import include, url
from .views import success
from .views import RegistrarCurso

urlpatterns = [
    url(r'^registrar-curso/$', RegistrarCurso.as_view(), name='registar_curso'),
]