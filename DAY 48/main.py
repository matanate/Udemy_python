from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)
driver.get("https://www.python.org")
dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
n = 0
for event, date in zip(event_names, dates):
    events[n] = {
        "time": date.get_attribute("datetime").split("T")[0],
        "name": event.text,
    }
    n += 1
print(events)
driver.close()
