from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'first.html')


def generate(request):
    num = int(request.POST['txtNum'])
    return render(request,'second.html',{'n':range(num)})