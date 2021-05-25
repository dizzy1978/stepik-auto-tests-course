from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    # Ваш код, который заполняет нужные поля
    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    answer1 = browser.find_element_by_id("answer")
    answer1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()	
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()	

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
	