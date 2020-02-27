from django.shortcuts import render
from calculator.forms import CalculationForm
from calculator.models import CalculatedHistory


def CalculationView(request):
    history = list(CalculatedHistory.objects.all())[:-11:-1]
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']

            if request.POST.get('operator') == 'continue':
                result_to_x = list(CalculatedHistory.objects.all())[-1].result
                form = CalculationForm(data={'x':result_to_x})
                return render(request,'calculator.html',{'form': form,'history':history})

            results = {'+':x+y,'-':x-y,'x':x*y,'/':x/y}
            result = results[request.POST.get('operator')]

            CalculatedHistory.objects.create(x=x,y=y,operator=request.POST.get('operator'),result=result)

            history = list(CalculatedHistory.objects.all())[:-11:-1]
            return render(request,'calculator.html',{'form':form,'result':result,'history':history})
    else:
        form = CalculationForm()
    return render(request,'calculator.html',{'form': form,'history':history})

def HomepageView(request):
    return render(request,'homepage.html')

def AboutmeView(request):
    return render(request,'aboutme.html')