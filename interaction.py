from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Sbos Programs\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
website = "https://en.wikipedia.org/wiki/Main_Page"

#one way to click on a link
driver.get(website)
article_count = driver.find_element_by_css_selector("#articlecount a")
article_count.click()

#find method that is specific too links
all_portals = driver.find_element_by_link_text("All portals")
all_portals.click()

#add text to search bar
search_bar = driver.find_element_by_name("search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

