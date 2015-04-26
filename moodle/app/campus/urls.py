from django.conf.urls import include, url
from .views import index, success
from .views import RegistrarPersona, ListarPersonas

urlpatterns = [
    url(r'^$', 'app.campus.views.index'),
    url(r'^success/$', 'app.campus.views.success', name='success'),
    url(r'^registrar/$', RegistrarPersona.as_view(), name='registrar_persona'),
    url(r'^listados-personas/$', ListarPersonas.as_view(), name='listar_personas'),
]
