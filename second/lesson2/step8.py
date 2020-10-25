
from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input[type='text']")
    for element in elements:
        element.send_keys("idk")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'Text.txt')
    input1 = browser.find_element_by_id("file")
    input1.send_keys(file_path)
    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()
