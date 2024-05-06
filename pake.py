import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
 # Create Chrome WebDriver instance
## run in Mac OS
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)
## run in Windows OS
# service = Service(executable_path="./chromedriver.exe")
# driver = webdriver.Chrome(service=service)
# Access the webpage

driver.get("https://sandbox403.moodledemo.net/login/index.php")
