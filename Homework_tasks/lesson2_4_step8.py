import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


def calc(n):
    return str(math.log(abs(12*math.sin(int(n)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
condition = WebDriverWait(browser, 10).until(
        ec.text_to_be_present_in_element((By.ID, "price"), "100")
    )
if condition:
    button = browser.find_element_by_id('book')
    button.click()

try:
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
