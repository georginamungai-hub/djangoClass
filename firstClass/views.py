from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# def helloWorld(request):
#     return HttpResponse('Hello, World!')

def index(request):
    context = {'message': 'Hello, World!'}
    return render(request, 'index.html',context)

def home(request):
    return render(request, 'child.html')
