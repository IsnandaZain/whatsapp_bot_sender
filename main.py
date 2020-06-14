from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup
import time
import os

parent_directory = os.path.dirname(os.path.abspath(__file__))

# TO START GOOGLE CHROME
navigator = webdriver.Chrome(executable_path=parent_directory+ "/chromedriver.exe")
navigator.get("https://web.whatsapp.com/")

# DELAY TO MAKE SURE QR IS LOADED
time.sleep(5)
source = navigator.find_element_by_xpath("html/body/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]")
barcode = BeautifulSoup(source.get_attribute('innerHTML'), 'html.parser').find('div').attrs['data-ref']

# GENERATE IMAGE FOR QRCODE
import pyqrcode
qr = pyqrcode.create(barcode)
qr_filename = "barcode_user_" + str(int(time.time())) + ".png"
qr.png(qr_filename, scale=9)


# GET MAIN PAGE DATA
# DELAY TO MAKE SURE QR CODE IS SCANNED
time.sleep(10)
mainpage_source = navigator.page_source
soup = BeautifulSoup(mainpage_source, 'html.parser')
# f = open("mainpage_source", "w", encoding="utf-8")
# f.write(soup.text)
# f.close()