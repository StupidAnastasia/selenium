
import unittest
from selenium import webdriver
import time

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'

def testFunc(link):

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
    return (welcome_text)

class TestReg(unittest.TestCase):
    def test1(self):
        test1 = testFunc(link1)
        self.assertEqual(test1, "Congratulations! You have successfully registered!", "Error")
        
    def test2(self):
        test2 = testFunc(link2)
        self.assertEqual(test2, "Congratulations! You have successfully registered!", "Error")
        
if __name__ == "__main__":
    unittest.main()
 