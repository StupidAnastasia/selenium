
from selenium import webdriver
import math
import time
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    browser.find_element_by_tag_name("button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()
