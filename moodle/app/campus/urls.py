from django.conf.urls import include, url
from .views import index, success
from .views import RegistrarMasterTeacher, ListarPersonas, RegistrarSecretariaEducacion, RegistrarLeaderTeacher

urlpatterns = [
    url(r'^$', 'app.campus.views.index'),
    url(r'^success/$', 'app.campus.views.success', name='success'),
    url(r'^registrar/$', RegistrarMasterTeacher.as_view(), name='registrar_persona'),
    url(r'^listados-personas/$', ListarPersonas.as_view(), name='listar_personas'),
    url(r'^secretaria-educacion/$', RegistrarSecretariaEducacion.as_view(), name='registrar_secretaria'),
    url(r'^registrarLT/$', RegistrarLeaderTeacher.as_view(), name= 'registrar_leader_teacher')
]
