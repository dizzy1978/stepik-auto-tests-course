from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[2]/input')
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[3]/input')
    input3.send_keys("s2bb3t3t@mail.ru")	
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
	

    # По-хорошему, надо было делать так, а не копировать Х-Path пути из браузера =))))
    #firstName = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    #firstName.send_keys('Artemy')
    #lastName = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    #lastName.send_keys('Vetts')
    #eMail = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    #eMail.send_keys('vetc@list.ru')