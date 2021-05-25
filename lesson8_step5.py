from selenium import webdriver
browser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing';alert('Robots at work');")
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button) # Джаваскриптом прокручиваем окно до видимости кнопки.
button.click()	

#browser.execute_script("window.scrollBy(0, 100);") # scroll the window to 100px down

# Можно выполнять в консоли хрома
#// javascript
#button = document.getElementsByTagName("button")[0];
#button.scrollIntoView(true);

# Если мы столкнулись с такой ситуацией, мы можем заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.
# Делается это с помощью следующего скрипта:

#"return arguments[0].scrollIntoView(true);"