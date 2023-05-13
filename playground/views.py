from django.shortcuts import render

# Create your views here.

def calculate():
    x = 10
    y = 10
    
    return x

def hello(request):
    x = calculate()
    return render(request,'hello.html',{'name':'bala','age':24})