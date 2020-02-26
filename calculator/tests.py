from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from calculator.views import CalculationView
from calculator.forms import CalculationForm
from calculator.models import Calculated_history
# Create your tests here.

class CalculationTest(TestCase):

    def test_rootURL_mapping_to_calculation_view(self):
        found = resolve('/')
        self.assertEqual(found.func,CalculationView)

    def test_rendering_calculator_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'calculator.html')

    def test_display_calculation_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'],CalculationForm)
    
    def test_can_save_POST_into_calculation_history(self):
        self.client.post('/',data={'x':'1','y':'2','operator':'+'})
        self.assertEqual(Calculated_history.objects.count(),1)
        new_history = Calculated_history.objects.first()
        self.assertEqual(new_history.x,1.0)
        self.assertEqual(new_history.y,2.0)
        self.assertEqual(new_history.operator,'+')
        self.assertEqual(new_history.result,3.0)
    
    def test_after_POST_pass_correct_result_to_template(self):
        response = self.client.post('/',data={'x':'1','y':'2','operator':'+'})
        self.assertEqual(response.context['result'],3.0)

        response = self.client.post('/',data={'x':'5','y':'1.2','operator':'-'})
        self.assertEqual(response.context['result'],3.8)

        response = self.client.post('/',data={'x':'2.5','y':'1.5','operator':'x'})
        self.assertEqual(response.context['result'],3.75)

        response = self.client.post('/',data={'x':'1','y':'2','operator':'/'})
        self.assertEqual(response.context['result'],0.5)
        