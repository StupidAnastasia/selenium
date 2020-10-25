
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 110);")
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.quit()

   