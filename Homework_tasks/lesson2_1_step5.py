from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/math.html"


def calc(n):
    return str(math.log(abs(12*math.sin(int(n)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('span#input_value.nowrap')
    x = x_element.text

    input_res = browser.find_element_by_css_selector('input#answer')
    input_res.send_keys(calc(x))
    time.sleep(2)
    on_checkbox = browser.find_element_by_css_selector('input#robotCheckbox')
    on_checkbox.click()
    time.sleep(2)
    on_radio = browser.find_element_by_css_selector('input#robotsRule')
    on_radio.click()
    time.sleep(2)
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
