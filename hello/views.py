from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello World<h1>')
    return render(request,'email.html')
def indexx(request):
    return HttpResponse('<h1>Hello World<h1>')