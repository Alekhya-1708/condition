from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':100,'b':50,'c':400}
    return render(request,'condition.html',d)