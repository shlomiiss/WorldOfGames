import time
from selenium.webdriver.chrome.options import Options
from selenium import  webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import sys
my_driver = webdriver.Chrome('C:/Temp/chromedriver.exe')
mysite = 'http://127.0.0.1:8777/'

def main_function():
    test_score_service(mysite)
def test_score_service(url):
   my_driver.get(mysite)
   x = int(my_driver.find_element(By.XPATH,'//*[@id="score"]').text)
   print(x)
   if (x == 777):
       print('test success')
       return (sys.exit(0))
   else:
       print("test failure")
       return (sys.exit(-1))


main_function()
