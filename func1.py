from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
# Create Chrome WebDriver instance
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# Access the webpage

driver.get("https://sandbox.moodledemo.net/login/index.php")

#  log in
def login():
    try:
        username = WebDriverWait(driver, 20,2).until(EC.presence_of_element_located((By.NAME, "username")))
        password = WebDriverWait(driver, 20,2).until(EC.presence_of_element_located((By.NAME, "password")))
        username.send_keys("student")
        password.send_keys("sandbox")
        password.submit()
        time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
        
def accessToDashboard():
    try: 
        dashboard_link = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/my/']")))
        dashboard_link.click()
        time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

def clickToNewevent():
    try: 
        new_event_button = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-action='new-event-button']")))
        new_event_button.click()
        WebDriverWait(driver, 20,2).until(EC.visibility_of_element_located((By.ID, "id_name")))
        time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
def selectdate():
    try:
        # date
        day_dropdown = Select(WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timestart_day"))))
        day_dropdown.select_by_value("9") 
        time.sleep(2)
        # month
        month_dropdown = Select(WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timestart_month"))))
        month_dropdown.select_by_value("4") 
        time.sleep(2)
        # year
        year_dropdown = Select(WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timestart_year"))))
        year_dropdown.select_by_value("2024")
        time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    
def fillToForm():
    try:
        # title
        name_input = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID, "id_name")))
        name_input.send_keys("kiểm tra GK")
        time.sleep(2)
        # Select Date
        selectdate()
        
        # click show more 
        show_more_link = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.CLASS_NAME, "moreless-toggler")))
        show_more_link.click()
        time.sleep(2)
        
        ################################ begin desciption########################################
        # Chuyển tới iframe
        iframe = WebDriverWait(driver, 20,2).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "id_description_ifr")))
        # desciption
        p_textarea = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"tinymce")))
        p_textarea.click()
        p_textarea.send_keys("kiểm tra 45p")
        time.sleep(2)
        # Quay lại khung cha
        driver.switch_to.default_content()
        ################################ end desciption########################################
        
        # location
        location_input = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_location")))
        location_input.send_keys("H6 112")
        time.sleep(2)
        # Chọn input "Without duration"
        without_duration_radio = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='id_duration_0']")))
        without_duration_radio.click()
        time.sleep(2)
        # save
        save_button = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Save')]")))
        save_button.click()
        time.sleep(2)
        WebDriverWait(driver, 20,2).until(EC.invisibility_of_element_located((By.XPATH, "//button[contains(text(),'Save')]")))
        time.sleep(10)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

def calendar():
    # Click vào cuốn lịch
    calendar_button = driver.find_element(By.ID, "id_timestart_calendar")
    calendar_button.click()
    time.sleep(3)
    # Chọn ngày
    calendar_day = driver.find_element(By.ID, "calendaryui_3_18_1_1_1713841688081_156_pane_0_7_9")
    calendar_day.click()
    time.sleep(2)
    
def fillToForm_withCalendar():
    # title
    name_input = driver.find_element(By.ID,"id_name")
    name_input.send_keys("kiểm tra GK")
    time.sleep(1)
    calendar()
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
def test_NE001002():
    login()
    accessToDashboard()
    clickToNewevent()
    fillToForm_withCalendar()
    
    

