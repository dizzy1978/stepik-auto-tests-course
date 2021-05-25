from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    # Ваш код, который заполняет нужные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer1 = browser.find_element_by_id("answer")
    answer1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()	
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()	

	
    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
	

#option1 = browser.find_element_by_css_selector("[for='java']")
#option1.click()