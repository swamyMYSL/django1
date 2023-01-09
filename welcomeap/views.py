from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    return render(request,'input.html')
def add(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=x+y
    return HttpResponse("the sum is:"+str(z))

# Create your views here.
