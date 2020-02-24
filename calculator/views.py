from django.shortcuts import render
from calculator.forms import calculationForm
# Create your views here.

def calculation(request):
    if request.method == 'POST':
        form = calculationForm(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            operator = ''
    else:
        form = calculationForm()
    return render(request,'calculator.html',{'form': form})