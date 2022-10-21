import time
from selenium.webdriver.common.by import By
from selenium import webdriver

chrome_browser = webdriver.Chrome("./chromedriver")
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

sum1 = chrome_browser.find_element(By.ID, 'sum1')
sum1.clear()
sum1.send_keys('1')

sum2 = chrome_browser.find_element(By.ID, 'sum2')
sum2.clear()
sum2.send_keys('2')

time.sleep(2)
get_total_button = chrome_browser.find_element(By.LINK_TEXT, 'Get Total')
get_total_button.click()
