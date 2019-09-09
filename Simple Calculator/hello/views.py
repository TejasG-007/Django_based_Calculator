from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Tejas'})
def add(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    val3=(request.GET['opr'])
    if val3=='*':
        res=val1*val2
    if val3=='+':
        res=val1+val2
    if val3=='-':
        res=val1-val2
    if val3=='/':
        res=val1/val2
    return render(request,'home.html',{'result':res})

