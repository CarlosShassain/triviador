from django.conf.urls import patterns, include, url
from django.contrib import admin
#admin.autodiscover()
from triviador.apps.pregunta.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include("triviador.apps.pregunta.urls")), 
)
