import time
from selenium.webdriver.chrome.options import Options
from selenium import  webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
my_driver = webdriver.Chrome(executable_path="C:/Temp/chromedriver")
#mysite = 'http://127.0.0.1:30000/'
#my_driver = webdriver.chrome(executable_path="/Users/x1/Downloads")

#test_scores_service('mysite')
# Class 4
# Write a program that does the following:
# 1. Write a script which will open the following:
# a. Chrome – http://www.walla.co.il
# b. FireFox – http://www.ynet.co.il
my_driver.get('https://www.ynet.co.il')

# 2. In one of the browsers you open do the following:
# a. Create a variable with the website’s title
# b. Refresh website
# c. Get website name and compare it to the variable you
# created in clause 1.
# web_title = my_driver.title
# print(web_title)
# my_driver.refresh()
#c not clear


# //*[@id="ArticleHeaderComponent"]/div[1]/h1
# Opera:
# //*[@id="ArticleHeaderComponent"]/div[1]/h1
#
# We have same XPATH



#mysite = 'https://translate.google.com/'
#my_driver.get(mysite)
# my_driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys("טקסט")
#
# 5.
#  Open Youtube web page
#  Type a name of a song
#  Click on search.
# #



# mysite = ('https://youtube.com')
# my_driver.get(mysite)
# my_driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("song")
# my_driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button').click()



# 6.
#  Open Chrome browser on Google Translate website:
# https://translate.google.com/
#  Find translation text field (the one you send keys to)
# with 3 different locators and print the WebElement
# you created.

# mysite = ('https://translate.google.com/')
# my_driver.get(mysite)
# #my_driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
# #my_driver.find_element(By.CSS_SELECTOR,'body#yDmH0d > c-wiz > div > div:nth-of-type(2) > c-wiz > div:nth-of-type(2) > c-wiz > div > div:nth-of-type(2) > div:nth-of-type(3) > c-wiz > span > span > div > textarea').send_keys('class')
# my_driver.find_element(By.TAG_NAME,'TEXTAREA').send_keys('class')



# 7.
#  Open Chrome browser on Facebook website
# https://www.facebook.com/
#  Login into Facebook (No need to send me credentials).


# mysite = ('https://facebook.com/')
# my_driver.get(mysite)
# #my_driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
#my_driver.find_element(By.CSS_SELECTOR,'body#yDmH0d > c-wiz > div > div:nth-of-type(2) > c-wiz > div:nth-of-type(2) > c-wiz > div > div:nth-of-type(2) > div:nth-of-type(3) > c-wiz > span > span > div > textarea').send_keys('class')
# my_driver.find_element(By.XPATH,'//*[@id="email"]').send_keys('email')
# my_driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys('password')
# my_driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').submit()
# time.sleep(5)

#
#
#
# CHALLENGES:
# 8.
#  Open Chrome browser on any webpage.
#  Delete all cookies from browser.
#  Make sure all cookies are deleted by printing all cookies
# stored in the browser.
# mysite = ('https://facebook.com/')
# my_driver.get(mysite)
# print(my_driver.get_cookies())
# time.sleep(5)
# my_driver.delete_all_cookies()
# print(my_driver.get_cookies())


# 9.
#  Open any browser on "Github" website.
#  https://github.com/
#  Enter “Selenium” keyword in search textfield
#  Press Enter to search (through code - of course).

# mysite = ('https://github.com/')
# my_driver.get(mysite)
# my_driver.find_element(By.XPATH,'body/div[1]/header[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/form[1]/label[1]/input[1]').send_keys('Selenium')


#  # 10.
#  Find a way to disable all extensions in
# o Chrome
# o Firefox
# o Internet Explorer.
#  Run browsers without extensions.

# #Chrome
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# my_driver = webdriver.Chrome(executable_path="C:/Temp/chromedriver",options=chrome_options)

#Firefox
#When running  webdriver ,the Firefox extensions are disabled




#
