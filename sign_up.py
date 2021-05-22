from selenium import webdriver
from selenium.webdriver.common.keys import Keys

website = "http://secure-retreat-92358.herokuapp.com/"
chrome_driver_path = "C:\Sbos Programs\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(website)

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Sbo")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("TheMan")

email = driver.find_element_by_name("email")
email.send_keys("SboTheMan@gmail.com")

#when you use a css selector, you do not need to specify the id or class, you just need too use the type for example a form or button
button = driver.find_element_by_css_selector("form button")
button.send_keys(Keys.ENTER)
