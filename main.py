from pake import *
from func1 import *
from func2 import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


# Gọi các hàm test từ func1.py
test_CP002008()


# Quit the WebDriver
driver.quit()