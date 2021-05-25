from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    # Ваш код, который заполняет нужные поля
    input1 = browser.find_element_by_xpath('/html/body/div/form/div/input[1]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('/html/body/div/form/div/input[2]')
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_xpath('/html/body/div/form/div/input[3]')
    input3.send_keys("s2bb3t3t@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла
    send_file = browser.find_element_by_id("file")
    send_file.send_keys(file_path)	

    # Отправляем заполненную форму
    button1 = browser.find_element_by_xpath('//button[text()="Submit"]')
    button1.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
	
	