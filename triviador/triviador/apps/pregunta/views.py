from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
def pagina_index(request):
	return render_to_response("blog/index.html",{},context_instance=RequestContext(request))
