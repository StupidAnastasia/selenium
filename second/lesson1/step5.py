
import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    inputX = browser.find_element_by_id("answer")
    inputX.send_keys(y)
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    robots = browser.find_element_by_id("robotsRule")
    robots.click()
    button = browser.find_element_by_tag_name("button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()