from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import unittest
from calculator.models import Calculated_history

class CalculationTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def calculate(self,_x,_y,operator):

        # He see that there is x,y form to enter inputs, result label to show result and +,-,x,/ buttons for calculation
        x = self.browser.find_element_by_id('id_x')
        y = self.browser.find_element_by_id('id_y')
        operator_btn = self.browser.find_element_by_id(operator)
        x.clear()
        y.clear()
        x.send_keys(_x)
        y.send_keys(_y)
        operator_btn.send_keys(Keys.ENTER)
        time.sleep(1)
    
    def check_result(self,_x,_y,_result):

        # Now he see the result of x - y = result in the result
        result = self.browser.find_element_by_id('result').text
        self.assertEqual(_result,result)

        # And he see that there stll are _x in x and _y in y
        x = self.browser.find_element_by_id('id_x').get_attribute('value')
        y = self.browser.find_element_by_id('id_y').get_attribute('value')
        
        self.assertEqual(_x,x)
        self.assertEqual(_y,y)
        time.sleep(1)

    def test_user_can_use_calculator_to_calculate(self):

        # Now Ronnie has a trouble with his calculator
        # He remember that there is a calculator on a website
        # Then He goes to calculator website 
        self.browser.get(self.live_server_url)
        time.sleep(1)

        # He found that there is Calculator on the title and header of the website

        self.assertEqual('calculator',self.browser.title)
        header = self.browser.find_element_by_id('header').text
        self.assertEqual('Calculator',header)

        # He notice there are calculation history that he has calculated before
        # that is 34.0 + 10.0 = 44.0 and 22.0 - 99.0 = -77.0
        history_list = self.browser.find_element_by_id('history')
        history_item = history_list.find_elements_by_name('history_item')
        self.assertEqual('34.0 + 10.0 = 44.0',history_item[0].text)
        self.assertEqual('22.0 - 99.0 = -77.0',history_item[1].text)

        # He see that there is x,y form to enter inputs, result label to show result and +,-,x,/ buttons for calculation
        # Now he want to calculate 121 + 555
        # So he enter 121 into x ,and 555 into y ,then he click on '+' button 

        self.calculate('121','555','+')
        time.sleep(1)

        # Now he see the result of 121 + 555 = 676.0 in the result
        # And he see that there stll are 121 in x and 555 in y
        self.check_result('121','555','676.0')
        time.sleep(1)

        # In history list , He see a new history 121.0 + 555.0 = 676.0 in the first order
        history_list = self.browser.find_element_by_id('history')
        history_item = history_list.find_elements_by_name('history_item')
        self.assertEqual('121.0 + 555.0 = 676.0',history_item[0].text)
        self.assertEqual('34.0 + 10.0 = 44.0',history_item[1].text)
        self.assertEqual('22.0 - 99.0 = -77.0',history_item[2].text)

        # Then he want to calculate 1111 - 999
        # So he enter 1111 into x,and 999 into y,then he click on '-' button
        self.calculate('1111','999','-')
        time.sleep(1)

                
        # Now he see the result of 1111 - 999 = 112.0 in the result
        # And he see that there stll are 1111 in x and 999 in y
        self.check_result('1111','999','112.0')

        # In history list , He see a new history 1111.0 - 999.0 = 112.0 in the first order
        history_list = self.browser.find_element_by_id('history')
        history_item = history_list.find_elements_by_name('history_item')
        self.assertEqual('1111.0 - 999.0 = 112.0',history_item[0].text)
        self.assertEqual('121.0 + 555.0 = 676.0',history_item[1].text)
        self.assertEqual('34.0 + 10.0 = 44.0',history_item[2].text)

        # Then he want to calculate 222 x 1.7
        # So he enter 222 into x,and 4 into y,then he click on 'x' button
        self.calculate('222','1.7','x')
        time.sleep(1)
        
        # Now he see the result of 222 x 1.7 = 377.4 in the result
        # And he see that there stll are 222 in x and 4 in y
        self.check_result('222','1.7','377.4')

        # In history list , He see a new history 222.0 x 1.7 = 377.4 in the first order
        history_list = self.browser.find_element_by_id('history')
        history_item = history_list.find_elements_by_name('history_item')
        self.assertEqual('222.0 x 1.7 = 377.4',history_item[0].text)
        self.assertEqual('1111.0 - 999.0 = 112.0',history_item[1].text)
        self.assertEqual('121.0 + 555.0 = 676.0',history_item[2].text)
        

        # Then he want to calculate 75 / 12
        # So he enter 75 into x,and 12 into y,then he click on '/' button
        self.calculate('75','12','/')
        time.sleep(1)
        
        # Now he see the result of 75 / 12  = 6.25 in the result
        # And he see that there stll are 75 in x and 5 in y
        self.check_result('75','12','6.25')

        # In history list , He see a new history 75.0 / 12.0  = 6.25 in the first order
        history_list = self.browser.find_element_by_id('history')
        history_item = history_list.find_elements_by_name('history_item')
        
        self.assertEqual('1111.0 - 999.0 = 112.0',history_item[0].text)
        self.assertEqual('121.0 + 555.0 = 676.0',history_item[1].text)
        self.assertEqual('75.0 / 12.0  = 6.25',history_item[2].text)

        self.fail('finish test')

    


        