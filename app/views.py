from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def urlmapping(request):
    return HttpResponse('Hello, I am Madhu!')

def headingtag(request):
    return HttpResponse('<h1>This content using h1 tag</h1>')

def marqueetag(request):
    return HttpResponse('<marquee><h1>This content using marquee tag</h1></marquee>')

def biodata(request):
    return HttpResponse('''<h1 style="color: crimson;">I am Ram Pothineni</h1>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Enim sapiente dicta quaerat nihil aut eos!</p>
                        <img src='https://images.javatpoint.com/biography/images/ram-pothineni.png'</img>''')