from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
# Create Chrome WebDriver instance
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# Access the webpage

driver.get("https://sandbox.moodledemo.net/login/index.php")

#  log in
def login():
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    username.send_keys("student")
    password.send_keys("sandbox")
    password.submit()
    time.sleep(2)
def accessToDashboard():
    dashboard_link = driver.find_element(By.CSS_SELECTOR,"a[href='https://sandbox.moodledemo.net/my/']")
    dashboard_link.click()
    time.sleep(2)
def clickToNewevent():
    new_event_button = driver.find_element(By.XPATH,"//button[@data-action='new-event-button']")
    new_event_button.click()
    time.sleep(4)
def fillToForm():
    # title
    name_input = driver.find_element(By.ID,"id_name")
    name_input.send_keys("kiểm tra GK")
    time.sleep(1)
    # date
    day_dropdown = Select(driver.find_element(By.ID,"id_timestart_day"))
    day_dropdown.select_by_value("9") 
    time.sleep(1)
    # month
    month_dropdown = Select(driver.find_element(By.ID,"id_timestart_month"))
    month_dropdown.select_by_value("4") 
    time.sleep(1)
    # year
    year_dropdown = Select(driver.find_element(By.ID,"id_timestart_year"))
    year_dropdown.select_by_value("2024")
    time.sleep(1)
    # click show more 
    show_more_link = driver.find_element(By.CLASS_NAME,"moreless-toggler")
    show_more_link.click()
    time.sleep(1)
    
    ################################ begin desciption########################################
    # Chuyển tới iframe
    iframe = driver.find_element(By.ID, "id_description_ifr")
    driver.switch_to.frame(iframe)
    time.sleep(1)
    # desciption
    p_textarea = driver.find_element(By.ID,"tinymce")
    p_textarea.click()
    p_textarea.send_keys("kiểm tra 45p")
    time.sleep(1)
    # Quay lại khung cha
    driver.switch_to.default_content()
    ################################ end desciption########################################
    
    # location
    location_input = driver.find_element(By.ID,"id_location")
    location_input.send_keys("H6 112")
    time.sleep(1)
    # Chọn input "Without duration"
    without_duration_radio = driver.find_element(By.XPATH,"//input[@id='id_duration_0']")
    without_duration_radio.click()
    time.sleep(1)
    # save
    save_button = driver.find_element(By.XPATH,"//button[contains(text(),'Save')]")
    save_button.click()
    time.sleep(10)
        
    
    
def test_NE001001():
    login()
    accessToDashboard()
    clickToNewevent()
    fillToForm()
    
    

