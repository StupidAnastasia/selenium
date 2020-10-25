
from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input.first[required]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_tag_name("input.second[required]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_tag_name("input.third[required]")
    input3.send_keys("inav@gmail.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    welcome_text_elt = browser.find_element_by_tag_name("h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
