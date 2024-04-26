from pake import *
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

def start():
    login("student", "sandbox")
    accessToDashboard()
    clickToNewevent()
    
################################## mudule 1 ############################################
def test_NE001001():
    start()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0)
def test_NE001003():
    start()
    fillToForm("kiem tra GK","9","4","2024",False)
def test_NE001004():
    start()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",1,"12","4","2024")
def test_NE001005():
    start()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",2,None,None,None,"45")
def test_NE001006():
    start()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"2") 
def test_NE001007():
    start()
    fillToForm() 
def test_NE001008():
    start()
    fillToForm("kiem tra GK","31","2","2024",False)
def test_NE001009():
    start()
    fillToForm("kiem tra GK","3","2","2024",True,None,None,1,"1","1","2024")
    
def test_NE001010():
    start()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",2,None,None,None,"-1")
def test_NE001011():
    start()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",2,None,None,None,"999999999")
def test_NE001012():
    start()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"-1") 
def test_NE001013():
    start()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"2.5") 
def test_NE001014():
    start()
    fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"99999") 

################################## mudule 2 ############################################
def test_NE003001():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","4","2000")
def test_NE003002():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","4","2000")
def test_NE003003():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","4","2000")
def test_NE003004():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","4","2000")
def test_NE003005():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","4","1900")
def test_NE003006():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","4","2004")
def test_NE003007():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","4","1901")
def test_NE003008():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","4","1900")
def test_NE003009():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","4","2004")
def test_NE003010():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","4","1901")
def test_NE003011():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","4","1900")
def test_NE003012():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","4","2004")
def test_NE003013():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","4","1901")
def test_NE003014():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","4","1900")
def test_NE003015():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","4","2004")
def test_NE003016():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","4","1901")
def test_NE003017():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","1","2000")
def test_NE003018():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","1","2000")
def test_NE003019():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","1","2000")
def test_NE003020():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","1","2000")
def test_NE003021():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","1","1900")
def test_NE003022():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","1","2004")
def test_NE003023():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","1","1901")
def test_NE003024():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","1","1900")
def test_NE003025():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","1","2004")
def test_NE003026():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","1","1901")
def test_NE003027():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","1","1900")
def test_NE003028():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","1","2004")
def test_NE003029():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","1","1901")
def test_NE003033():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","2","2000")
def test_NE003034():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","2","2000")
def test_NE003035():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","2","2000")
def test_NE003036():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","2","2000")
def test_NE003037():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","2","1900")
def test_NE003038():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","2","2004")
def test_NE003039():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","2","1901")
def test_NE003040():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","2","1900")
def test_NE003041():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","2","2004")
def test_NE003042():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","2","1901")
def test_NE003043():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","2","1900")
def test_NE003044():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","2","2004")
def test_NE003045():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","2","1901")
def test_NE003046():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","2","1900")
def test_NE003047():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","2","2004")
def test_NE003048():
    start()
    fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","2","1901")










