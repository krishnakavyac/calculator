from django.shortcuts import render

# Create your views here.
def calculator(request):
    return render(request,'calculator.html')

def result(request):
    x=int(request.POST.get("num1"))
    y=int(request.POST.get("num2"))
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    e=x%y
    f=x//y
    g=x**y
    return render(request,'result.html',{"sum":a,"difference":b,"product":c,"quotient":d,"modulus":e,"round":f,"exponent":g})