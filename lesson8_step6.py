from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    # Ваш код, который заполняет нужные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    #button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button) # Джаваскриптом прокручиваем окно до видимости кнопки.
    browser.execute_script("window.scrollBy(0, 100);") # scroll the window to 100px down	
    answer1 = browser.find_element_by_id("answer")
    answer1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()	
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()	

    # Отправляем заполненную форму
    button1 = browser.find_element_by_xpath('//button[text()="Submit"]')
    button1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
	