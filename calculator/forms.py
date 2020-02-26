from django import forms

class CalculationForm(forms.Form):
    x = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your number'}))
    y = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your number'}))
