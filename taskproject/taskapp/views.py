from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return HttpResponse("It is Conatct Page")

def details(request):
    return HttpResponse("It is the Details Page")

def thanks(request):
    return render(request,"thanks.html")

def hey(request):
    return HttpResponse("HEY YOU")

def operations(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    resadd=x+y
    ressub=x-y
    resmul=x*y
    resdiv=x/y
    return render(request,"solution.html",{'solutionofadd':resadd,'solutionofsub':ressub,'solutionofmul':resmul,'solutionofdiv':resdiv})
