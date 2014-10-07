#encoding:utf-8

from .forms import *
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext, loader, Context, Template
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from django.http import *

from .models import PerfilUser
def pagina_index(request):
	return render_to_response("blog/index.html",{},context_instance=RequestContext(request))
#def registro(request):
#	if request.method=="POST":
#		form=PerfilUser_Form(request.POST)
#		if(form.is_valid()):
#			form.save()
#			return HttpResponseRedirect("/blog/")
#	form=PerfilUser_Form()
#	return render_to_response("usuario/registro.html",{"form":form},RequestContext(request))
def registro(request):
	username = password = email =''
	if request.POST:
		user_form = UserCreateForm(request.POST)
		if user_form.is_valid():
			usuario = User(username=request.POST['username'], email=request.POST['email'])
			usuario.set_password(request.POST['password1'])
			usuario.save()
			return HttpResponseRedirect("/blog/")
	else:
		user_form = UserCreateForm()

	diccionario = {
		'user_form': user_form,
		'page_title': 'Aplicacion - Register',
		'body_class': 'register',
	}
	return render_to_response("usuario/registro.html", diccionario, context_instance=RequestContext(request))