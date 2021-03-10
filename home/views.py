from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def home(requset):
    return render( request , "home.html", {"name": "Nabin"})

def add(request):
    val1 = int(request.POST['num1']),
    val2 = int(request.POST['num2'])
    res = val1 + val2

    return Render( request, "result.html", {"result": res} ) 