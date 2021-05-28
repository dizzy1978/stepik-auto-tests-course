import time
import math
import pytest
from selenium import webdriver

links = [
    ("https://stepik.org/lesson/236895/step/1"),
    ("https://stepik.org/lesson/236896/step/1"),
    ("https://stepik.org/lesson/236897/step/1"),
    ("https://stepik.org/lesson/236898/step/1"),
    ("https://stepik.org/lesson/236899/step/1"),
    ("https://stepik.org/lesson/236903/step/1"),
    ("https://stepik.org/lesson/236904/step/1"),
    ("https://stepik.org/lesson/236905/step/1")
 ]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():

    @pytest.mark.parametrize('link', links)
    def test_guest_should_see_login_link(self, browser, link):
        linka = f"{link}"
        browser.get(linka)
        #browser.find_element_by_css_selector("#login_link")
        print("Проверяемый URL %s" % linka)

