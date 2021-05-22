from selenium import webdriver

chrome_driver_path = "C:\Sbos Programs\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#got to website and get the price for product
python_website = "https://www.python.org/"
driver.get(python_website)
get_upcoming_events = driver.find_elements_by_css_selector(".event-widget time")
get_upcoming_events_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

#add multiple entries into a dictionary
for n in range(len(get_upcoming_events)):
    events[n] = {
        "time": get_upcoming_events[n].text,
        "name": get_upcoming_events_names[n].text
    }

print(events)
driver.quit()
