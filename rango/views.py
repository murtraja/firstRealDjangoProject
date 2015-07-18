# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage':'I am bold font from the context'}
    path = request.get_full_path()
    newpath = path+"about/"
    #return HttpResponse("Rango says hello world!<br>click <a href='"+newpath+"'>here</a> to go the about page")
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    path = request.get_full_path()
    newpath=path.replace("about/", "")
    return HttpResponse("Rango Says: Here is the <b>about</b> page.<br>Click <a href='"+newpath+"'>here</a> to go the previous page")
