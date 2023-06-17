from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    # pull data from db
    # Transform
    # end email
    x=1
    y=2
    return render(request, 'hello.html' , {'name': 'Mosh'})