from django.shortcuts import render
from calculator_getmethod.models import CalculatedGetHistory
from calculator_getmethod.forms import CalculationGetForm

# Create your views here.

def CalculationGetView(request):
    x = request.GET.get('x')
    y = request.GET.get('y')
    if x != None and y != None:
        x = float(x)
        y = float(y)
        results = {'+':x+y,'-':x-y,'x':x*y,'/':x/y}
        result = results[request.GET.get('operator')]
        #CalculatedGetHistory.objects.create(x=x,y=y,operator=request.GET.get('operator'),result=result)
        #history = list(CalculatedGetHistory.objects.all())[:-11:-1]
        return render(request,'calculatorget.html',{result:'result'})
    else:
        return render(request,'calculatorget.html')