from django.shortcuts import render
from calculator.forms import CalculationForm
from calculator.models import CalculatedHistory


def CalculationView(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            results = {'+':x+y,'-':x-y,'x':x*y,'/':x/y}
            result = results[request.POST.get('operator')]

            CalculatedHistory.objects.create(x=x,y=y,operator=request.POST.get('operator'),result=result)

            history = list(CalculatedHistory.objects.all())[:-11:-1]
            return render(request,'calculator.html',{'form':form,'result':result,'history':history})
    else:
        history = list(CalculatedHistory.objects.all())[:-11:-1]
        form = CalculationForm()
    return render(request,'calculator.html',{'form': form,'history':history})