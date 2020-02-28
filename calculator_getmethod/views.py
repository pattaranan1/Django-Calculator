from django.shortcuts import render
from calculator_getmethod.models import CalculatedGetHistory
from calculator_getmethod.forms import CalculationGetForm

# Create your views here.

def CalculationGetView(request):
    if request.method == "GET":
        form = CalculationGetForm(request.GET)
        if form.is_valid():

            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            results = {'+':x+y, '-':x-y, 'x':x*y, '/':x/y}
            result = results[request.GET.get('operator')]
            #CalculatedGetHistory.objects.create(x=x,y=y,operator=request.GET.get('operator'),result=result)
            #history = list(CalculatedGetHistory.objects.all())[:-11:-1]
            return render(request,'calculatorget.html',{'form':form,'result':result})
    else:
        form = CalculationGetForm()
    return render(request,'calculatorget.html',{'form':form})