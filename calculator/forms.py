from django import forms

class calculationForm(forms.Form):
    x = forms.FloatField()
    y = forms.FloatField()
    