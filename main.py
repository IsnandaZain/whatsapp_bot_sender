from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import os

parent_directory = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Firefox(executable_path=parent_directory + "/geckodriver")
driver.get("https://web.whatsapp.com")

print(driver)