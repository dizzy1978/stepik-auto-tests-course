from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    # Ваш код, который заполняет нужные поля
    blue_butt = browser.find_element_by_xpath('//button[text()="I want to go on a magical journey!"]')
    blue_butt.click()
    
    alert = browser.switch_to.alert
    alert.accept()
	
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
	
    x_element = browser.find_element_by_id("answer")
    x_element.send_keys(y)
	
    button1 = browser.find_element_by_xpath('//button[text()="Submit"]')
    button1.click()
	
	
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(5)
    # закрываем браузер после всех манипуляций
    print(browser.switch_to.alert.text)
    browser.quit()
    
	
	