from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import *

urlpatterns = patterns('',
    url(r'^$', pagina_index),
    url(r'^registro/$',registro), 
   	url(r'^login/$',login_usuario), 
   	url(r'^perfil/$',perfil),  
   	url(r'^logout/$',logout_usuario),
)