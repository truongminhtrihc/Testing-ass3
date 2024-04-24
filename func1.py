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
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# Access the webpage

driver.get("https://sandbox.moodledemo.net/login/index.php")

#  log in
def login(name , passw):
    try:
        username = WebDriverWait(driver, 20,2).until(EC.presence_of_element_located((By.NAME, "username")))
        password = WebDriverWait(driver, 20,2).until(EC.presence_of_element_located((By.NAME, "password")))
        username.send_keys(name)
        password.send_keys(passw)
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
def selectdate(day, month, year):
    try:
        # year
        year_dropdown = Select(WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timestart_year"))))
        year_dropdown.select_by_value(year)
        time.sleep(2)
        # month
        month_dropdown = Select(WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timestart_month"))))
        month_dropdown.select_by_value(month) 
        time.sleep(2)
        # date
        day_dropdown = Select(WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timestart_day"))))
        day_dropdown.select_by_value(day) 
        time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
def selectdateUntil(day, month, year):
    try:
        # year
        year_dropdown = Select(WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timedurationuntil_year"))))
        year_dropdown.select_by_value(year)
        time.sleep(2)
        # month
        month_dropdown = Select(WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timedurationuntil_month"))))
        month_dropdown.select_by_value(month) 
        time.sleep(2)
        # date
        day_dropdown = Select(WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timedurationuntil_day"))))
        day_dropdown.select_by_value(day) 
        time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    
def fillToForm(title=None,day=None, month=None,year=None,isShowmore=False,description=None,location=None, duration=None,dayU=None, monthU=None,yearU=None,durationMinute=None,isRepeat=False,repeatS=None):
    try:
        # title
        if title is not None:
            name_input = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID, "id_name")))
            name_input.send_keys(title)
            time.sleep(2)
            
        if day is not None:
            # Select Date
            selectdate(day,month,year)
        
        if isShowmore is True: 
            # click show more 
            show_more_link = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.CLASS_NAME, "moreless-toggler")))
            show_more_link.click()
            time.sleep(2)
            
            
            ################################ begin desciption########################################
            if description is not None:
                # Chuyển tới iframe
                iframe = WebDriverWait(driver, 20,2).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "id_description_ifr")))
                # desciption
                p_textarea = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"tinymce")))
                p_textarea.click()
                p_textarea.send_keys(description)
                time.sleep(2)
                # Quay lại khung cha
                driver.switch_to.default_content()
            ################################ end desciption########################################
            
            if location is not None:
                # location
                location_input = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_location")))
                location_input.send_keys(location)
                time.sleep(2)
            # Chọn input "Without duration"
            without_duration_radio = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.XPATH,f"//input[@id='id_duration_{duration}']")))
            without_duration_radio.click()
            time.sleep(2)
            if duration == 1:
                selectdateUntil(dayU,monthU,yearU)
            if duration == 2:
                minute_input = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_timedurationminutes")))
                minute_input.send_keys(durationMinute)
                time.sleep(2)
            
            if isRepeat is True:
                repeat = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.XPATH,f"//input[@id='id_repeat']")))
                repeat.click()
                time.sleep(2)
                
                repeats = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"id_repeats")))
                repeats.clear()
                repeats.send_keys(repeatS)
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
    try:
        # Click vào cuốn lịch
        open_calendar_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "id_timestart_calendar")))

        # Scroll đến phần tử để nó trở nên nhìn thấy được
        driver.execute_script("arguments[0].scrollIntoView();", open_calendar_button)

        # Click vào nút mở lịch
        driver.execute_script("arguments[0].click();", open_calendar_button)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "dateselector-calendar-content")))

        time.sleep(3)
        # Chọn ngày
        # day_element = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID, "calendaryui_3_18_1_1_1713887201701_156_pane_0_7_9")))
        # driver.execute_script("arguments[0].click();", day_element)
        # time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

        
def fillToForm_withCalendar():
    try:
        # title
        name_input = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID, "id_name")))
        name_input.send_keys("kiểm tra GK")
        time.sleep(2)
        # Select Date
        calendar()
        
        # click show more 
        show_more_link = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.CLASS_NAME, "moreless-toggler")))
        show_more_link.click()
        time.sleep(2)
        
        ################################ begin desciption########################################
        # Chuyển tới iframe
        iframe = WebDriverWait(driver, 20,2).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "id_description_ifr")))
        # desciption
        p_textarea = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID,"tinymce")))
        # Cuộn đến phần tử
        driver.execute_script("arguments[0].scrollIntoView();", p_textarea)

        # # Sử dụng ActionChains để nhấp vào phần tử
        # actions = ActionChains(driver)
        # actions.move_to_element(element_to_click).click().perform()
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

    
def test_NE001001():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0)
def test_NE001003():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",False)
def test_NE001004():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",1,"12","4","2024")
def test_NE001005():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",2,None,None,None,"45")
def test_NE001006():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"2") 
def test_NE001007():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm() 
def test_NE001008():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","31","2","2024",False)
def test_NE001009():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","3","2","2024",True,None,None,1,"1","1","2024")
    
def test_NE001010():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",2,None,None,None,"-1")
def test_NE001011():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",2,None,None,None,"999999999")
def test_NE001012():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"-1") 
def test_NE001013():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"2.5") 
def test_NE001014():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"99999") 