from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    # Ищем цифры вопроса и считаем их сумму
    x_element1 = browser.find_element_by_id("num1")
    x_element2 = browser.find_element_by_id("num2")
    x1 = int(x_element1.text)
    x2 = int(x_element2.text)
    y = str(x1 + x2)
    print (y)
	
	# Ищем выпадающий список и выбираем значение, равное вычисленной ранее сумме
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(y) # Выбираем соответствующее значение из выпадающего списка
	
    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('/html/body/div/form/button')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()


