from django.test import TestCase
from django.urls import resolve
from calculator.views import CalculationView
from calculator.forms import CalculationForm
from calculator.models import CalculatedHistory
# Create your tests here.

class CalculationTest(TestCase):

    def test_rootURL_mapping_to_calculation_view(self):
        found = resolve('/calculator')
        self.assertEqual(found.func,CalculationView)

    def test_rendering_calculator_template(self):
        response = self.client.get('/calculator')
        self.assertTemplateUsed(response,'calculator.html')

    def test_display_calculation_form(self):
        response = self.client.get('/calculator')
        self.assertIsInstance(response.context['form'],CalculationForm)
    
    def test_can_save_POST_into_calculation_history(self):
        self.client.post('/',data={'x':'1','y':'2','operator':'+'})
        self.assertEqual(CalculatedHistory.objects.count(),1)
        new_history = CalculatedHistory.objects.first()
        self.assertEqual(new_history.x,1.0)
        self.assertEqual(new_history.y,2.0)
        self.assertEqual(new_history.operator,'+')
        self.assertEqual(new_history.result,3.0)
    
    def test_after_POST_pass_correct_result_to_template(self):
        response = self.client.post('/calculator',data={'x':'1','y':'2','operator':'+'})
        self.assertEqual(response.context['result'],3.0)

        response = self.client.post('/calculator',data={'x':'5','y':'1.2','operator':'-'})
        self.assertEqual(response.context['result'],3.8)

        response = self.client.post('/calculator',data={'x':'2.5','y':'1.5','operator':'x'})
        self.assertEqual(response.context['result'],3.75)

        response = self.client.post('/calculator',data={'x':'1','y':'2','operator':'/'})
        self.assertEqual(response.context['result'],0.5)
    
    def test_after_POST_pass_correct_history_and_order_to_template(self):
        response = self.client.post('/calculator',data={'x':'1','y':'2','operator':'+'})
        self.assertEqual(str(response.context['history'][0]),'1.0 + 2.0 = 3.0')

        response = self.client.post('/calculator',data={'x':'5','y':'1.2','operator':'-'})
        self.assertEqual(str(response.context['history'][0]),'5.0 - 1.2 = 3.8')
        self.assertEqual(str(response.context['history'][1]),'1.0 + 2.0 = 3.0')

        response = self.client.post('/calculator',data={'x':'2.5','y':'1.5','operator':'x'})
        self.assertEqual(str(response.context['history'][0]),'2.5 x 1.5 = 3.75')
        self.assertEqual(str(response.context['history'][1]),'5.0 - 1.2 = 3.8')
        self.assertEqual(str(response.context['history'][2]),'1.0 + 2.0 = 3.0')

        response = self.client.post('/calculator',data={'x':'1','y':'2','operator':'/'})
        self.assertEqual(str(response.context['history'][0]),'1.0 / 2.0 = 0.5')
        self.assertEqual(str(response.context['history'][1]),'2.5 x 1.5 = 3.75')
        self.assertEqual(str(response.context['history'][2]),'5.0 - 1.2 = 3.8')
        self.assertEqual(str(response.context['history'][3]),'1.0 + 2.0 = 3.0')