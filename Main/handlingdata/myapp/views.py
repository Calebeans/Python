from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def say_hello(request):
    return HttpResponse("Hello World")

def homepage(request):
    return HttpResponse("Welcome to Little Lemon!")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little Lemon again!</h1>"""
    return HttpResponse(text)

def index(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 
