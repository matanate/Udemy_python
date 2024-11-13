from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--start-maximized")


edge_options.add_argument(
    "user-data-dir=C:\\Users\\Matan\\AppData\\Local\\Microsoft\\Edge\\User Data"
)
edge_options.add_argument("--profile-directory=Personal")

driverpath = "msedgedriver.exe"

driver = webdriver.Edge(driverpath, options=edge_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3731645793&f_E=2&geoId=118410967&keywords=python%20developer&location=Rehovot%2C%20Center%20District%2C%20Israel&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
)

