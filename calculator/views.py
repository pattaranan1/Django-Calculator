from django.shortcuts import render
from calculator.forms import calculationForm
# Create your views here.

def calculation(request):
    if request.method == 'POST':
        form = calculationForm(request.POST)
        if form.is_valid():
            x = float(form.cleaned_data['x'])
            y = float(form.cleaned_data['y'])
            results = {'add':x+y,'subtract':x-y,'multiply':x*y,'divide':x/y}
            result = results[request.POST.get('operator')]
            return render(request,'calculator.html',{'form':form,'result':result})
    else:
        form = calculationForm()
    return render(request,'calculator.html',{'form': form})