 link = "http://selenium1py.pythonanywhere.com/"
import time



def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(20)
    browser.find_element_by_css_selector("#login_link")