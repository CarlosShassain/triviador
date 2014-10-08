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

from .models import *
def pagina_index(request):
	return render_to_response("blog/index.html",{},context_instance=RequestContext(request))
def registro(request):
	username = password = email =''
	if request.POST:
		user_form = UserCreateForm(request.POST)
		if user_form.is_valid():
			usuario = User(username=request.POST['username'], email=request.POST['email'])
			usuario.set_password(request.POST['password1'])
			usuario.save()
			return HttpResponseRedirect("/blog/login")
	else:
		user_form = UserCreateForm()

	diccionario = {
		'user_form': user_form,
		'page_title': 'Aplicacion - Register',
		'body_class': 'register',
	}
	return render_to_response("usuario/registro.html", diccionario, context_instance=RequestContext(request))
def login_usuario(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado:
				login(request,resultado)
				request.session["name"]=username
				return HttpResponseRedirect("/blog/perfil/")
	form=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form":form},RequestContext(request))

def perfil(request):
	return render_to_response("usuario/perfil.html",{"nombre":request.session["name"]},RequestContext(request))
def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect("/blog/")
def addCategoria(request):
	if(request.method=="POST"):
		form_cat=Categorias_Form(request.POST)
		if(form_cat.is_valid()):
			form_cat.save()
			return HttpResponseRedirect("/blog/categoria/")
	form_cat=Categorias_Form()
	return render_to_response("blog/categorias.html",{"form":form_cat},RequestContext(request))
def addPregunta(request):
	if(request.method=="POST"):
		form_pre=Pregunta_Form(request.POST)
		if(form_pre.is_valid()):
			form_pre.save()
			return HttpResponseRedirect("/blog/preguntas/")
	form_pre=Pregunta_Form()
	return render_to_response("blog/preguntas.html",{"form":form_pre},RequestContext(request))
def addRespuesta(request):
	if(request.method=="POST"):
		form_res=Respuestas_Opcionales_Form(request.POST)
		if(form_res.is_valid()):
			form_res.save()
			return HttpResponseRedirect("/blog/respuestas/")
	form_res=Respuestas_Opcionales_Form()
	return render_to_response("blog/respuestas.html",{"form":form_res},RequestContext(request))
@login_required
def set_registro(request):
	if request.method=="POST":
		formulario_registro=Perfil_Form(request.POST)
		if formulario_registro.is_valid():
			formulario_registro.save()
			return HttpResponseRedirect("/login/")
	else:
		formulario_registro=Perfil_Form()
	return render_to_response("usuario/setregistro.html",{'form':formulario_registro},context_instance=RequestContext(request))
