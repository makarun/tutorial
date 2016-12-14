from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessege': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context = context_dict)
    #return HttpResponse("Rango says hello! <br/> <a href='/rango/about'>About</a>")

def about(request):
    context_dict = {'boldmessege': 'This tutorial has been put together by devil'}
    return render(request, 'rango/about.html', context=context_dict)
    #return HttpResponse("Rango says here is the about page.<br/> <a href='/rango/'> MainPage </a>")