from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(
        'div.first_block>div>input[class="form-control first"]'
    )
    input1.send_keys("Ivan")
    time.sleep(2)
    input2 = browser.find_element_by_css_selector(
        'div.first_block>div>input[class="form-control second"]'
    )
    input2.send_keys("Petrov")
    time.sleep(2)
    input3 = browser.find_element_by_css_selector(
        'div.first_block>div>input[class="form-control third"]'
    )
    input3.send_keys("123@123.ru")
    time.sleep(2)
    # Ваш код, который заполняет необязательные поля
    # input4 = browser.find_element_by_css_selector(
    #     'div.second_block>div>input[class="form-control first"]'
    # )
    # input4.send_keys("+1234567890")
    # time.sleep(3)
    # input5 = browser.find_element_by_css_selector(
    #     'div.second_block>div>input[class="form-control second"]'
    # )
    # input5.send_keys("ABS, abs, 123, 456, abs")
    # time.sleep(3)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
