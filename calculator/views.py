from django.shortcuts import render
from calculator.forms import calculationForm
# Create your views here.

def calculation(request):
    if request.method == 'POST':
        form = calculationForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            print(request.POST.get('+',''))
            print(request.POST.get('-',''))
            print(request.POST.get('x',''))
            print(request.POST.get('/',''))
    else:
        form = calculationForm()
    return render(request,'calculator.html',{'form': form})