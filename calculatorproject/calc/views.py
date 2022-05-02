from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')


def addfun(request):
    n1 = request.POST['num1']
    n2 = request.POST['num2']
    sum = int(n1)+int(n2)
    return HttpResponse(f"Sum is {sum}")


def subfun(request):
    n1 = request.POST['num1']
    n2 = request.POST['num2']
    diff= int(n1) - int(n2)
    return HttpResponse(f"differnce  is {diff}")

def multifun(request):
    n1 = request.POST['num1']
    n2 = request.POST['num2']
    multi= int(n1) * int(n2)
    return HttpResponse(f"prodect  is {multi}")

def divfun(request):
    n1 = request.POST['num1']
    n2 = request.POST['num2']
    divi= int(n1) // int(n2)
    return HttpResponse(f"divisan  is {divi}")