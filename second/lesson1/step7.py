import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
  link = "http://suninjuly.github.io/get_attribute.html"
  browser = webdriver.Chrome()
  browser.get(link)
  treasure = browser.find_element_by_id("treasure")
  x = treasure.get_attribute("valuex")
  y = calc(x)
  input1 = browser.find_element_by_id("answer")
  input1.send_keys(y)
  check = browser.find_element_by_id("robotCheckbox")
  check.click()
  robots = browser.find_element_by_id("robotsRule")
  robots.click()
  button = browser.find_element_by_tag_name("button")
  button.click()
finally:
  time.sleep(10)
  browser.quit()
