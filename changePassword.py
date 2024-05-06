from pake import *

################################## mudule 1 ##########################################
class Module1Test(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="./chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://sandbox403.moodledemo.net/login/index.php")
        
        
    def test_CP001001(self):
        print("-------------test_CP001001-------------")
        login(self.driver,"student","sandbox")
        openMenu(self.driver)
        changePassword(self.driver,"sandbox","1" * 100,"1" * 100)
        print("-------------test_CP001001 END -------------")
        # changePassword("1","1","1")

    def test_CP001002(self):
        print("-------------test_CP001002-------------")
        login(self.driver,"student","1"*100)
        openMenu(self.driver)
        changePassword(self.driver,"1"*100,"1" * 150,"1" * 150)
        print("-------------test_CP001002 END -------------")
    def test_CP001003(self):
        print("-------------test_CP001003-------------")
        login(self.driver,"student","1"*128)
        openMenu(self.driver)
        changePassword(self.driver,"1"*150,"1" * 150,"1" * 150)
        print("-------------test_CP001003 END -------------")
    def test_CP001004(self):
        print("-------------test_CP001004-------------")
        login(self.driver,"student","1"*128)
        openMenu(self.driver)
        changePassword(self.driver,"1"*128,"sandbox","sandbox")
        print("-------------test_CP001004 END -------------")
        

################################## mudule 2 ##########################################
class Module2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("#################### Module 2 ########################")
    def setUp(self):
        service = Service(executable_path="./chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://sandbox403.moodledemo.net/login/index.php")
        
    def test_CP002001(self):
        print("-------------test_CP002001-------------")
        login(self.driver,"student","sandbox")
        openMenu(self.driver)
        changePassword(self.driver,"sandbox","1","1")
        print("-------------test_CP002001 END-------------")
    def test_CP002002(self):
        print("-------------test_CP002002-------------")
        login(self.driver,"student","1")
        openMenu(self.driver)
        changePassword(self.driver,"1","11","1")
        print("-------------test_CP002002 END-------------")
    def test_CP002003(self):
        print("-------------test_CP002003-------------")
        login(self.driver,"student","1")
        openMenu(self.driver)
        changePassword(self.driver,"1","1","1")
        print("-------------test_CP002003 END-------------")
    def test_CP002004(self):
        print("-------------test_CP002004-------------")
        login(self.driver,"student","1")
        openMenu(self.driver)
        changePassword(self.driver,"1","1","11")
        print("-------------test_CP002004 END-------------")
    def test_CP002005(self):
        print("-------------test_CP002005-------------")
        login(self.driver,"student","1")
        openMenu(self.driver)
        changePassword(self.driver,"11","111","111")
        print("-------------test_CP002005 END-------------")
    def test_CP002006(self):
        print("-------------test_CP002006-------------")
        login(self.driver,"student","1")
        openMenu(self.driver)
        changePassword(self.driver,"11","111","1")
        print("-------------test_CP002006 END-------------")
    def test_CP002007(self):
        print("-------------test_CP002007-------------")
        login(self.driver,"student","1")
        openMenu(self.driver)
        changePassword(self.driver,"11","11","11")
        print("-------------test_CP002007 END-------------")
    def test_CP002008(self):
        print("-------------test_CP002008-------------")
        login(self.driver,"student","1")
        openMenu(self.driver)
        changePassword(self.driver,"11","11","111")
        print("-------------test_CP002008 END-------------")

#  log in
def login(driver,name , passw):
    try:
        username = WebDriverWait(driver, 20,2).until(EC.presence_of_element_located((By.NAME, "username")))
        password = WebDriverWait(driver, 20,2).until(EC.presence_of_element_located((By.NAME, "password")))
        username.send_keys(name)
        password.send_keys(passw)
        password.submit()
        time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu")
   
# open dropdown menu of User
def openMenu(driver):
    try: 
        openMenuToggle = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID, "user-menu-toggle")))
        openMenuToggle.click()
        time.sleep(2)
        prefer = WebDriverWait(driver,20,2).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Preferences')]")))
        prefer.click()
        time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu")
# change password
def changePassword(driver,passwordCurr,newPassword1,newPassword2):
    try:
        change = WebDriverWait(driver,20,2).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Change password')]")))
        change.click()
        time.sleep(2)
        
        passwordC = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='id_password']")))
        passwordC.send_keys(passwordCurr)
        time.sleep(2)
        
        passwordN1 = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='id_newpassword1']")))
        passwordN1.send_keys(newPassword1)
        time.sleep(2)
        
        passwordN2 = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='id_newpassword2']")))
        passwordN2.send_keys(newPassword2)
        time.sleep(2)
        
        # save
        save_button = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='id_submitbutton']")))
        save_button.click()
        # time.sleep(2)
        # WebDriverWait(driver, 20,2).until(EC.invisibility_of_element_located((By.XPATH, "//input[@id='id_submitbutton']")))
        time.sleep(4)
        
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu")