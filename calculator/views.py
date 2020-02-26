from django.shortcuts import render
from calculator.forms import CalculationForm
from calculator.models import Calculated_history
# Create your views here.

def CalculationView(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            x = float(form.cleaned_data['x'])
            y = float(form.cleaned_data['y'])
            results = {'+':x+y,'-':x-y,'x':x*y,'/':x/y}
            result = results[request.POST.get('operator')]

            Calculated_history.objects.create(x=x,y=y,operator=request.POST.get('operator'),result=result)

            history = list(Calculated_history.objects.all())[:-11:-1]
            return render(request,'calculator.html',{'form':form,'result':result,'history':history})
    else:
        history = list(Calculated_history.objects.all())[:-11:-1]
        form = CalculationForm()
    return render(request,'calculator.html',{'form': form,'history':history})