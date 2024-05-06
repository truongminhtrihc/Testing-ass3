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
        # time.sleep(2)
        # WebDriverWait(driver, 20,2).until(EC.invisibility_of_element_located((By.XPATH, "//button[contains(text(),'Save')]")))
        time.sleep(4)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

def start():
    login("student", "sandbox")
def closeF():
    try: 
        close_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close']")))
        close_button.click()
        time.sleep(4)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
  
################################## mudule 1 ############################################
class Module1TestUsecase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        start()
    def setUp(self):
        accessToDashboard()
        clickToNewevent()
    def test_NE001001(self):
        print("---------------test_NE001001---------------")
        fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0)
        print("---------------test_NE001001 End---------------")
    def test_NE001003(self):
        print("---------------test_NE001003---------------")
        fillToForm("kiem tra GK","9","4","2024",False)
        print("---------------test_NE001003 End---------------")
    def test_NE001004(self):
        print("---------------test_NE001004---------------")
        fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",1,"12","4","2024")
        print("---------------test_NE001004 End---------------")
    def test_NE001005(self):
        print("---------------test_NE001005---------------")
        fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",2,None,None,None,"45")
        print("---------------test_NE001005 End---------------")
    def test_NE001006(self):
        print("---------------test_NE001006---------------")
        fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"2") 
        print("---------------test_NE001006 End---------------")
    def test_NE001007(self):
        print("---------------test_NE001007---------------")
        fillToForm() 
        closeF()
        print("---------------test_NE001007 End---------------")
        
    def test_NE001008(self):
        print("---------------test_NE001008---------------")
        fillToForm("kiem tra GK","31","2","2024",False)
        print("---------------test_NE001008 End---------------")
    def test_NE001009(self):
        print("---------------test_NE001009---------------")
        fillToForm("kiem tra GK","3","2","2024",True,None,None,1,"1","1","2024")
        closeF()
        print("---------------test_NE001009 End---------------")
        
    def test_NE001010(self):
        print("---------------test_NE001010---------------")
        fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",2,None,None,None,"-1")
        closeF()
        print("---------------test_NE001010 End---------------")
    def test_NE001011(self):
        print("---------------test_NE001011---------------")
        fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",2,None,None,None,"999999999")
        closeF()
        print("---------------test_NE001011 End---------------")
        
    def test_NE001012(self):
        print("---------------test_NE001012---------------")
        fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"-1") 
        closeF()
        print("---------------test_NE001012 End---------------")
        
    def test_NE001013(self):
        print("---------------test_NE001013---------------")
        fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"2.5") 
        closeF()
        print("---------------test_NE001013 End---------------")
       
    def test_NE001014(self):
        print("---------------test_NE001014---------------")
        fillToForm("kiem tra GK","9","4","2024",True,"kiểm tra 45p","H6 112",0,None,None,None,None,True,"99999") 
        closeF()
        print("---------------test_NE001014 End---------------")
        

################################## mudule 2 ############################################
class Module2TestBoudary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # start()
        print("#################### Module 2 ########################")
    def setUp(self):
        accessToDashboard()
        clickToNewevent()
    def test_NE003001(self):
        print("------------test_NE003001------------")
        closeF()
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","4","2000")
        closeF()
        print("------------test_NE003001 End------------")
    def test_NE003002(self):
        print("------------test_NE003002------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","4","2000")
        closeF()
        print("------------test_NE003002 End------------")
    def test_NE003003(self):
        print("------------test_NE003003------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","4","2000")
        closeF()
        print("------------test_NE003003 End------------")
    def test_NE003004(self):
        print("------------test_NE003004------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","4","2000")
        closeF()
        print("------------test_NE003004 End------------")
    def test_NE003005(self):
        print("------------test_NE003005------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","4","1900")
        closeF()
        print("------------test_NE003005 End------------")
    def test_NE003006(self):
        print("------------test_NE003006------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","4","2004")
        closeF()
        print("------------test_NE003006 End------------")
    def test_NE003007(self):
        print("------------test_NE003007------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","4","1901")
        closeF()
        print("------------test_NE003007 End------------")
    def test_NE003008(self):
        print("------------test_NE003008------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","4","1900")
        closeF()
        print("------------test_NE003008 End------------")
    def test_NE003009(self):
        print("------------test_NE003009------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","4","2004")
        closeF()
        print("------------test_NE003009 End------------")
    def test_NE003010(self):
        print("------------test_NE003010------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","4","1901")
        closeF()
        print("------------test_NE003010 End------------")
    def test_NE003011(self):
        print("------------test_NE003011------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","4","1900")
        closeF()
        print("------------test_NE003011 End------------")
    def test_NE003012(self):
        print("------------test_NE003012------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","4","2004")
        closeF()
        print("------------test_NE003012 End------------")
    def test_NE003013(self):
        print("------------test_NE003013------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","4","1901")
        closeF()
        print("------------test_NE003013 End------------")
    def test_NE003014(self):
        print("------------test_NE003014------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","4","1900")
        closeF()
        print("------------test_NE003014 End------------")
    def test_NE003015(self):
        print("------------test_NE003015------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","4","2004")
        closeF()
        print("------------test_NE003015 End------------")
    def test_NE003016(self):
        print("------------test_NE003016------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","4","1901")
        closeF()
        print("------------test_NE003016 End------------")
    def test_NE003017(self):
        print("------------test_NE003017------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","1","2000")
        closeF()
        print("------------test_NE003017 End------------")
    def test_NE003018(self):
        print("------------test_NE003018------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","1","2000")
        closeF()
        print("------------test_NE003018 End------------")
    def test_NE003019(self):
        print("------------test_NE003019------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","1","2000")
        closeF()
        print("------------test_NE003019 End------------")
    def test_NE003020(self):
        print("------------test_NE003020------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","1","2000")
        closeF()
        print("------------test_NE003020 End------------")
    def test_NE003021(self):
        print("------------test_NE003021------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","1","1900")
        closeF()
        print("------------test_NE003021 End------------")
    def test_NE003022(self):
        print("------------test_NE003022------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","1","2004")
        closeF()
        print("------------test_NE003022 End------------")
    def test_NE003023(self):
        print("------------test_NE003023------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","1","1901")
        closeF()
        print("------------test_NE003023 End------------")
    def test_NE003024(self):
        print("------------test_NE003024------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","1","1900")
        closeF()
        print("------------test_NE003024 End------------")
    def test_NE003025(self):
        print("------------test_NE003025------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","1","2004")
        closeF()
        print("------------test_NE003025 End------------")
    def test_NE003026(self):
        print("------------test_NE003026------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","1","1901")
        closeF()
        print("------------test_NE003026 End------------")
    def test_NE003027(self):
        print("------------test_NE003027------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","1","1900")
        closeF()
        print("------------test_NE003027 End------------")
    def test_NE003028(self):
        print("------------test_NE003028------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","1","2004")
        closeF()
        print("------------test_NE003028 End------------")
    def test_NE003029(self):
        print("------------test_NE003029------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","1","1901")
        closeF()
        print("------------test_NE003029 End------------")
    def test_NE003033(self):
        print("------------test_NE003033------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","2","2000")
        closeF()
        print("------------test_NE003033 End------------")
    def test_NE003034(self):
        print("------------test_NE003034------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","2","2000")
        closeF()
        print("------------test_NE003034 End------------")
    def test_NE003035(self):
        print("------------test_NE003035------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","2","2000")
        closeF()
        print("------------test_NE003035 End------------")
    def test_NE003036(self):
        print("------------test_NE003036------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","2","2000")
        closeF()
        print("------------test_NE003036 End------------")
    def test_NE003037(self):
        print("------------test_NE003037------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","2","1900")
        closeF()
        print("------------test_NE003037 End------------")
    def test_NE003038(self):
        print("------------test_NE003038------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","2","2004")
        closeF()
        print("------------test_NE003038 End------------")
    def test_NE003039(self):
        print("------------test_NE003039------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"15","2","1901")
        closeF()
        print("------------test_NE003039 End------------")
    def test_NE003040(self):
        print("------------test_NE003040------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","2","1900")
        closeF()
        print("------------test_NE003040 End------------")
    def test_NE003041(self):
        print("------------test_NE003041------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","2","2004")
        closeF()
        print("------------test_NE003041 End------------")
    def test_NE003042(self):
        print("------------test_NE003042------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"29","2","1901")
        closeF()
        print("------------test_NE003042 End------------")
    def test_NE003043(self):
        print("------------test_NE003043------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","2","1900")
        closeF()
        print("------------test_NE003043 End------------")
    def test_NE003044(self):
        print("------------test_NE003044------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","2","2004")
        closeF()
        print("------------test_NE003044 End------------")
    def test_NE003045(self):
        print("------------test_NE003045------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"30","2","1901")
        closeF()
        print("------------test_NE003045 End------------")
    def test_NE003046(self):
        print("------------test_NE003046------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","2","1900")
        closeF()
        print("------------test_NE003046 End------------")
    def test_NE003047(self):
        print("------------test_NE003047------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","2","2004")
        closeF()
        print("------------test_NE003047 End------------")
    def test_NE003048(self):
        print("------------test_NE003048------------")
        fillToForm("kiem tra GK","1","4","2024",True,None,None,1,"31","2","1901")
        closeF()
        print("------------test_NE003048 End------------")










