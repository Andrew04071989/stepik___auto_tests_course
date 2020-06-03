from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/redirect_accept.html"


def calc(n):
    return str(math.log(abs(12*math.sin(int(n)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text

    input_res = browser.find_element_by_css_selector('input#answer')
    input_res.send_keys(calc(x))

    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()