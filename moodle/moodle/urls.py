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

<<<<<<< HEAD
    #Personas
    url(r'^usuarios/', include('app.campus.urls')),
=======
    #Usuario
    url(r'^usuario/', include('app.campus.urls')), #url(r'^persona/', include('app.campus.urls')),
>>>>>>> 1d69285776e0113c04e0dd4977782fbbd5e357c6

    #cursos
    url(r'^curso/', include('app.curso.urls'))
]
