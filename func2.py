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
   
# open dropdown menu of User
def openMenu():
    try: 
        openMenuToggle = WebDriverWait(driver, 20,2).until(EC.element_to_be_clickable((By.ID, "user-menu-toggle")))
        openMenuToggle.click()
        time.sleep(2)
        prefer = WebDriverWait(driver,20,2).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'Preferences')]")))
        prefer.click()
        time.sleep(2)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
# change password
def changePassword(passwordCurr,newPassword1,newPassword2):
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
        time.sleep(2)
        WebDriverWait(driver, 20,2).until(EC.invisibility_of_element_located((By.XPATH, "//input[@id='id_submitbutton']")))
        time.sleep(10)
        
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

################################## mudule 1 ##########################################
def test_CP001001():
    login("student","sandbox")
    openMenu()
    changePassword("sandbox","1" * 100,"1" * 100)
    # changePassword("1","1","1")

def test_CP001002():
    login("student","1"*100)
    openMenu()
    changePassword("1"*100,"1" * 150,"1" * 150)
def test_CP001003():
    login("student","1"*128)
    openMenu()
    changePassword("1"*150,"1" * 150,"1" * 150)
def test_CP001004():
    login("student","1"*128)
    openMenu()
    changePassword("1"*128,"sandbox","sandbox")
    

################################## mudule 2 ##########################################
def test_CP002001():
    login("student","sandbox")
    openMenu()
    changePassword("sandbox","1","1")
def test_CP002002():
    login("student","1")
    openMenu()
    changePassword("1","11","1")
def test_CP002003():
    login("student","1")
    openMenu()
    changePassword("1","1","1")
def test_CP002004():
    login("student","1")
    openMenu()
    changePassword("1","1","11")
def test_CP002005():
    login("student","1")
    openMenu()
    changePassword("11","111","111")
def test_CP002006():
    login("student","1")
    openMenu()
    changePassword("11","111","1")
def test_CP002007():
    login("student","1")
    openMenu()
    changePassword("11","11","11")
def test_CP002008():
    login("student","1")
    openMenu()
    changePassword("11","11","111")
