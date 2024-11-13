from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--start-maximized")

driver = webdriver.Edge(options=edge_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# articlecount = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # articlecount.click()

# all_portals = driver.find_element(By.LINK_TEXT, "View source")
#
# search_box = driver.find_element(By.NAME, "search")
# search_box.send_keys("Python")
# search_box.send_keys(Keys.ENTER)

fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CLASS_NAME, "btn")

fname.send_keys("matan")
lname.send_keys("atedgi")
email.send_keys("abcd@gamil.com")
button.click()
