#encoding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
#from django.contrib.auth import RequestContext

from .models import PerfilUser
def pagina_index(request):
	return render_to_response("blog/index.html",{},context_instance=RequestContext(request))
def registro(request):
	if request.method=="POST":
		fusuario=UserCreationForm(request.POST)
		if(fusuario.is_valid()):
			fusuario.save();
			usuario=request.POST["username"]
			pais=request.POST["pais"]
			telefono=request.POST["telefono"]
			nuevo=User.objects.get(username=usuario)
			perfil=PerfilUser.objects.create(user=nuevo,pais=pais,telefono=telefono)
			return HttpResponse("Registrado")
	else:
		fusuario=UserCreationForm()
	return render_to_response("usuario/registro.html",{'formulario':fusuario},context_instance=RequestContext(request))