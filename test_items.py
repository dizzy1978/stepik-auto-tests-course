import time # Для проверки "глазами"

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(2) # Для проверки "глазами"
    txt_button = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button').text
    print("ADD BUTTON TEXT IS: ", txt_button )
    assert len(txt_button) > 0, 'ADD BUTTON NOT FOUND!'
