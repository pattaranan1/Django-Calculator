from django.shortcuts import render

# Create your views here.

def calculation(request):
    return render(request,'calculator.html')