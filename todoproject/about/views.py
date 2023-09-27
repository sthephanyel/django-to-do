from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homeAbout(request):
    return render(request, 'about/index.html')

def helloWorld(request):
    return HttpResponse('Hello World')
