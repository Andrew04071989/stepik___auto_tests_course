from selenium import webdriver
import os
import time


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('I')

    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('am')

    input2 = browser.find_element_by_name('email')
    input2.send_keys('mail@smth.smth')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_name('file')
    element.send_keys(file_path)

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
