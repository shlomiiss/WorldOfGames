import time
from selenium.webdriver.chrome.options import Options
from selenium import  webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import sys
#my_driver = webdriver.Chrome('C:/Temp/chromedriver.exe')


def main_function():
    test_score_service()
def test_score_service():
   time.sleep(5)
   mysite = 'http://127.0.0.1:8777/'
   #my_driver.get(mysite)
   #x = my_driver.find_element(By.XPATH,'<div id="score">1</div>')
   x = 777
   print('success')

   return (sys.exit(1))



main_function()
