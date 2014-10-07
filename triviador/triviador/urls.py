from django.conf.urls import patterns, include, url
from django.contrib import admin
#admin.autodiscover()
from trivia.apps.pregunta.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include("trivia.apps.pregunta.urls")), 
)
