from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link1 = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"


def num_sum(x, y):
    return str(int(x) + int(y))


try:
    browser = webdriver.Chrome()
    browser.get(link1)

    num_1_elem = browser.find_element_by_id('num1')
    num_1 = num_1_elem.text

    num_2_elem = browser.find_element_by_id('num2')
    num_2 = num_2_elem.text

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(num_sum(num_1, num_2))
    time.sleep(2)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
