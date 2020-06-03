from selenium import webdriver
import math
import time


link = "http://SunInJuly.github.io/execute_script.html"


def calc(n):
    return str(math.log(abs(12*math.sin(int(n)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text

    browser.execute_script("window.scrollBy(0, 1000);")

    input_res = browser.find_element_by_css_selector('input#answer')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);",
        input_res
    )
    input_res.send_keys(calc(x))

    on_checkbox = browser.find_element_by_css_selector('input#robotCheckbox')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);",
        on_checkbox
    )
    on_checkbox.click()

    on_radio = browser.find_element_by_css_selector('input#robotsRule')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);",
        on_radio
    )
    on_radio.click()

    button = browser.find_element_by_css_selector("button[type='submit']")
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);",
        button
    )
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
