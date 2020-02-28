from django import forms

class CalculationGetForm(forms.Form):
    x = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your number'}))
    y = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your number'}))
