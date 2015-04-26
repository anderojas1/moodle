from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'moodle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #administrador Django
    url(r'^admin/', include(admin.site.urls)),

    #Inicio
    url(r'^', include('app.campus.urls')),

    #Personas
    url(r'^persona/', include('app.campus.urls')),

    #cursos
    url(r'^curso/', include('app.curso.urls'))
]
