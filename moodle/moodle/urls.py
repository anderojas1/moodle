from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    # Examples:
    # url(r'^$', 'moodle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #administrador Django
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login', login, kwargs={'template_name': 'campus/login.html'}),

    #Inicio
    url(r'^', include('app.campus.urls')),

    #Personas
    url(r'^usuarios/', include('app.campus.urls')),

    #cursos
    url(r'^curso/', include('app.curso.urls'))
]
