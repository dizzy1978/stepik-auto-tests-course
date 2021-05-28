import time
import math
import pytest
from selenium import webdriver

links = [
    ("https://stepik.org/lesson/236895/step/1"),
    ("https://stepik.org/lesson/236896/step/1"),
    #("https://stepik.org/lesson/236897/step/1"),
    #("https://stepik.org/lesson/236898/step/1"),
    #("https://stepik.org/lesson/236899/step/1"),
    #("https://stepik.org/lesson/236903/step/1"),
    #("https://stepik.org/lesson/236904/step/1"),
    #("https://stepik.org/lesson/236905/step/1")
 ]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():

    @pytest.mark.parametrize('link', links)
    def test_found_message(self, browser, link):
        linka = f"{link}"
        browser.get(linka)
        text_area = browser.find_element_by_xpath('//textarea')
        y = str(math.log(int(time.time())))
        text_area.send_keys(y)
        time.sleep(1)
        button = browser.find_element_by_xpath('//button[text()="Отправить"]')
        button.click()
        time.sleep(3)





        #print("Вычисленное значение %s", y)
        #print("Проверяемый URL %s" % linka)
        #browser.find_element_by_css_selector("#login_link")
        #button1 = browser.find_element_by_xpath('//button[text()="Отправить"]')
        #button1.click()

