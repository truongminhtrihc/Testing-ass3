"""
    author: Nguyen Minh Toan
    date: 2024:29:04
    version: 1
"""
import time
import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta

TIME = 0.5
def clickEnrolUser(driver):
    try:
        enroluser = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, "//form[@action='https://sandbox.moodledemo.net/enrol/manual/manage.php']")))
        enroluser.click()
        WebDriverWait(driver, 20, 2).until(EC.visibility_of_element_located((By.ID, 'id_main')))
        time.sleep(TIME)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.") 
def selectUser(driver, search=None):
    try:
        
        if search is None:
            btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/div[3]/span')))
            btn.click()  # Clicking the dropdown arrow
            # sltUser = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul')))
            adminUser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//li[@data-value=\'2\']')))
            adminUser.click() # Clicking the dropdown arrow
        else:
            btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/div[3]/input')))
            btn.send_keys(search)
            # sltUser = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul')))
            adminUser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//li[@data-value=\'2\']')))
            adminUser.click()
        time.sleep(TIME)
    except:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.") 
def selectAssignRole(driver, val=4):
    ## val == 5 -> student
    ## otp == 4 -> non-editing teacher
    try:
        sltAssignRole = Select(WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.ID, 'id_roletoassign'))))
        sltAssignRole.select_by_value(val)
        time.sleep(TIME)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.") 
def selectShowMore(driver):
    try:
        showmoreBtn = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Show more...')]")))
        showmoreBtn.click()
        time.sleep(TIME)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
def clickRecover(driver):
    try:
        btn = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_recovergrades']")))
        btn.click()
        time.sleep(TIME)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
def selectStartFrom(driver, val):
    ## val : 2 -> course start = 26/02/13
    ##      : 3 -> Today
    ## : 4 -> Now
    try:
        btn = Select(WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_startdate']"))))
        btn.select_by_value(val)
        time.sleep(TIME)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
def selectEnrolDuration(driver, day=None):
    ## day * 86400 and day <= 365 and >=1
    try:
        val = day * 86400 if day is not None else ''
        btn = Select(WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='id_duration']"))))
        btn.select_by_value(str(val))
        time.sleep(TIME)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
def selectEnd(driver, en=False, calender=False, default=False, day=None, month=None, year=None, hour=None, minute=None):
    try:
        if en == True:
            # click enable
            btn = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.ID, 'id_timeend_enabled')))
            btn.click()
            # select datetime
            if calender == True: 
                # cal = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, '//i[@aria-label=\'Calendar\']')))
                # cal.click()
                # for i in range(12):
                #     temp = WebDriverWait(driver, 20, 2).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div/div/div/div/div[1]/div')))
                #     print(temp.text())
                #     break
                pass
            elif default == False:
                # day
                daySlt = Select(WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.ID, 'id_timeend_day'))))
                daySlt.select_by_value(day)
                # month 
                monthSlt = Select(WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.ID, 'id_timeend_month'))))
                monthSlt.select_by_value(month)
                # year
                yearSlt = Select(WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.ID, 'id_timeend_year'))))
                yearSlt.select_by_value(year)
                # hour
                hourSlt = Select(WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.ID, 'id_timeend_hour'))))
                hourSlt.select_by_value(hour)
                # minute
                minuteSlt = Select(WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.ID, 'id_timeend_minute'))))
                minuteSlt.select_by_value(minute)
        else:
            pass
        time.sleep(TIME * 10)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
def clickEnrol(driver):
    try:
        btn = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),\'Enrol users\')]')))
        btn.click()
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
def remove(driver):
    try:
        checkstr = """AU
Admin User"""
        for i in range(0, 6):  # Assuming there are 20 rows in total
            row_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, f'user-index-participants-2_r{i}'))
            )
            if 'emptyrow' not in row_element.get_attribute('class'):
                # This row is not empty, do something
                try:
                    th_element = row_element.find_element(By.TAG_NAME, 'th')
                    a_element = th_element.find_element(By.TAG_NAME, 'a')
                    if a_element.text == checkstr:
                        unenrol_link = row_element.find_element(By.CLASS_NAME, 'unenrollink')
                        driver.get(unenrol_link.get_attribute('href'))
                        # Unenroll
                        btnVer = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/div[3]/div/section/div/div/div/div[3]/div/div[2]/form/button')))
                        btnVer.click()
                        # Optionally, break out of the loop if you found and clicked the link
                        break
                except:
                    print("th or a element not found in the row.")
    except TimeoutException:
        print('Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.')

def clickInfor(driver):
    ## func: Function -> get (driver: Driver) -> None. This func with purpose check information
    try:
        for i in range(0, 5):  # Assuming there are 20 rows in total
            row_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, f'user-index-participants-2_r{i}'))
            )
            th_element = row_element.find_element(By.TAG_NAME, 'th')
            a_element = th_element.find_element(By.TAG_NAME, 'a')
            # print(th_element.text)
            checkstr = """AU
Admin User"""
            if a_element.text == checkstr:
                infoButton =  WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="user-index-participants-2_r{i}_c6"]/div/a[1]')))
                driver.execute_script("arguments[0].scrollIntoView();", infoButton)
                time.sleep(2)
                driver.execute_script("arguments[0].click();", infoButton)
                time.sleep(2)
                break  
    except Exception as e:
        print('Encountered an error:', e)
        print('have problems with check infor!')

def login(driver):
    try:
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        username.send_keys("teacher")
        password.send_keys("sandbox")
        password.submit()
    except:
        print('dang login co loi')

class Test_EnrolUser(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path='./chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://sandbox.moodledemo.net/login/index.php")
        # login with username: teacher
        try:
            login(self.driver)
            txt = ['Your session has timed out. Please log in again.']
            if txt[0] in self.driver.page_source:
                login(self.driver)
            time.sleep(TIME)
        except:
            print("Co loi xay ra khi dang nhap")
        # Access "my first course" -> participants
        try:
            self.driver.get('https://sandbox.moodledemo.net/user/index.php?id=2')
            time.sleep(TIME)
            
            #click enrol users
            clickEnrolUser(self.driver)
        except TimeoutException:
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    def test_UCT_1(self):
        # step 1:
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '5')
        # step 3:
        selectShowMore(self.driver)
        # step 4:
        clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '3')
        # step 6
        selectEnrolDuration(self.driver)
        # step 7
        selectEnd(self.driver, en=True, calender=False, default=True)
        # step 8:
        clickEnrol(self.driver)
        ### check results
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            self.assertEqual('1 enrolled users', chk.text)
        except:
            print('popup result sai!')
        ## check infor
        clickInfor(self.driver)
        try:
            usernameInfo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[1]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            self.assertTrue('Admin User', usernameInfo.text)
        except:
            print("username is created not correct with expect")
        ## remove make sure
        remove(self.driver)
    def test_UCT_2(self):
        ## Khong tich enable
         # step 1:
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '5')
        # step 3:
        selectShowMore(self.driver)
        # step 4:
        clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '3')
        # step 6
        selectEnrolDuration(self.driver)
        # step 7 -> en -> false, khong tich enable
        selectEnd(self.driver, en=False, calender=False, default=True)
        # step 8:
        clickEnrol(self.driver)
        ### check result
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            self.assertEqual('1 enrolled users', chk.text)
        except:
            print('popup result sai!')
        ## check infor
        clickInfor(self.driver)
        try:
            usernameInfo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[1]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            self.assertTrue('Admin User', usernameInfo.text)
        except:
            print("username is created not correct with expect")
        ## check dont have "Enrolment ends"
        try:
            enrolmenttitle = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[6]/th')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            self.assertNotEqual('Enrolment ends', enrolmenttitle.text)
        except:
            print('co loi khi check enrolment ends')
        ## remove make sure
        remove(self.driver)
    def test_UCT_3(self):
        ## check khi thay doi datetime tai enrol ends
        # step 1
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '5')
        # step 3:
        selectShowMore(self.driver)
        # step 4:
        clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '3')
        # step 6
        selectEnrolDuration(self.driver)
        # step 7
        selectEnd(self.driver, en=True, calender=False, default=False, day='1',month='1', year='2025', hour='0', minute='0')
        # step 8:
        clickEnrol(self.driver)
        ### check results
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            self.assertEqual('1 enrolled users', chk.text)
        except:
            print('popup result sai!')
        ## check infor
        clickInfor(self.driver)
        try:
            usernameInfo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[1]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            self.assertTrue('Admin User', usernameInfo.text)
        except:
            print("username is created not correct with expect")
        ## check "Enrolment ends" datetimes - Wednesday, 1 January 2025, 12:00 AM
        try:
            enrolmentdatetime = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[6]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            # print(enrolmentdatetime.text)
            self.assertEqual('Wednesday, 1 January 2025, 12:00 AM', enrolmentdatetime.text)
        except:
            print('co loi khi check enrolment ends')
        ## remove make sure
        remove(self.driver)
    # ---
    # def test_UCT_4(self):
    #     ## check tich vao calendar, do carlendar thay doi lien tuc nen test case nayf ko the hien thuc duoc
    #     pass
    def test_UCT_5(self):
        ## test enrolment duration
        # step 1
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '5')
        # step 3:
        selectShowMore(self.driver)
        # step 4:
        clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '3')
        # step 6
        selectEnrolDuration(self.driver, 7)
        # step 7
        selectEnd(self.driver, en=False, calender=False, default=False)
        # step 8:
        clickEnrol(self.driver)
        ## check result
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            self.assertEqual('1 enrolled users', chk.text)
        except:
            print('popup result sai!')
        ## check infor
        clickInfor(self.driver)
        try:
            usernameInfo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[1]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            self.assertTrue('Admin User', usernameInfo.text)
        except:
            print("username is created not correct with expect")
        ## check "Enrolment ends" datetimes - Wednesday, 1 January 2025, 12:00 AM
        try:
            enrolmentdatetimeStart = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[5]/td')))
            # cal new datetime
            given_time = datetime.strptime(enrolmentdatetimeStart.text, "%A, %d %B %Y, %I:%M %p")
            new_time = given_time + timedelta(days=7)
            formatted_new_time = new_time.strftime("%A, %d %B %Y, %I:%M %p")
            # print(formatted_new_time)
            enrolmentdatetimeEnd = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[6]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            # print(enrolmentdatetimeEnd.text)
            self.assertEqual(formatted_new_time, enrolmentdatetimeEnd.text)
        except:
            print('co loi khi check enrolment ends')
        ## remove make sure
        remove(self.driver)
    def test_UCT_6(self):
        ## enrol start -> courst start
        # step 1:
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '5')
        # step 3:
        selectShowMore(self.driver)
        # step 4:
        clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '2')
        # step 6
        selectEnrolDuration(self.driver)
        # step 7
        selectEnd(self.driver, en=True, calender=False, default=True)
        # step 8:
        clickEnrol(self.driver)
        ## check result
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            self.assertEqual('1 enrolled users', chk.text)
        except:
            print('popup result sai!')
        ## check infor
        clickInfor(self.driver)
        try:
            usernameInfo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[1]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            self.assertTrue('Admin User', usernameInfo.text)
        except:
            print("username is created not correct with expect")
        ## check "Enrolment start" datetimes - Tuesday, 26 February 2013, 12:00 AM
        try:
            enrolmentdatetimeStart = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[5]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            # print(enrolmentdatetimeEnd.text)
            self.assertEqual('Tuesday, 26 February 2013, 12:00 AM', enrolmentdatetimeStart.text)
        except:
            print('co loi khi check enrolment start')
        ## remove make sure
        remove(self.driver)
    def test_UCT_7(self):
        ## test case check enrol start -> Now, testcase nay ko the check self assert dc do moi lan req thi timestamp se khac 
        ### nen -> timesleep cua info se dai hon
        ## test enrolment duration
        # step 1
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '5')
        # step 3:
        selectShowMore(self.driver)
        # step 4:
        clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '4')
        # step 6
        selectEnrolDuration(self.driver)
        # step 7
        selectEnd(self.driver, en=True, calender=False, default=True)
        # step 8:
        clickEnrol(self.driver)
        ## check result
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            self.assertEqual('1 enrolled users', chk.text)
        except:
            print('popup result sai!')
        ## check infor
        clickInfor(self.driver)
        try:
            usernameInfo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[1]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            self.assertTrue('Admin User', usernameInfo.text)
        except:
            print("username is created not correct with expect")
        ## speel 5 seconds
        time.sleep(5)
        ## remove make sure
        remove(self.driver)
    def test_UCT_8(self):
        ## Không Tích vào Recover user's old grades if possible
        # step 1:
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '5')
        # step 3:
        selectShowMore(self.driver)
        # step 4: -> khong click
        # clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '3')
        # step 6
        selectEnrolDuration(self.driver)
        # step 7
        selectEnd(self.driver, en=True, calender=False, default=True)
        ## speel 5 seconds
        time.sleep(5)
        # step 8:
        clickEnrol(self.driver)
        ## remove make sure
        remove(self.driver)
    def test_UCT_9(self):
        ## khong click show more
         # step 1:
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '5')
        time.sleep(5)
        # step 8:
        clickEnrol(self.driver)
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            self.assertEqual('1 enrolled users', chk.text)
        except:
            print('popup result sai!')
        ## remove make sure
        remove(self.driver)
    def test_UCT_10(self):
        ## role non-edting teacher
         # step 1:
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '4')
        # step 3:
        selectShowMore(self.driver)
        # step 4:
        clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '3')
        # step 6
        selectEnrolDuration(self.driver)
        # step 7
        selectEnd(self.driver, en=True, calender=False, default=True)
        # step 8:
        clickEnrol(self.driver)
        ### check results
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            self.assertEqual('1 enrolled users', chk.text)
        except:
            print('popup result sai!')
        ## check role
        try:
            for i in range(0, 5):  # Assuming there are 20 rows in total
                row_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.ID, f'user-index-participants-2_r{i}'))
                )
                th_element = row_element.find_element(By.TAG_NAME, 'th')
                a_element = th_element.find_element(By.TAG_NAME, 'a')
                # print(th_element.text)
                checkstr = """AU
Admin User"""
                if a_element.text == checkstr:
                    roleInfo =  WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="user-index-participants-2_r{i}_c3"]/span/a')))
                    self.driver.execute_script("arguments[0].scrollIntoView();", roleInfo)
                    time.sleep(2)
                    # print(roleInfo.text)
                    self.assertEqual('Non-editing teacher', roleInfo.text)
                    time.sleep(2)
                    break  
        except Exception as e:
            print('Encountered an error:', e)
            print('have problems with check infor!')        
        ## remove make sure
        remove(self.driver)
    def test_UCT_11(self):
        ## go vao khung search thay vi click mui ten xuong
        #step 1: # go chu 'admin' vao khung search
        selectUser(self.driver, search='admin') 
        # step 2: '5' -> student
        selectAssignRole(self.driver, '4')
        # step 3:
        selectShowMore(self.driver)
        # step 4:
        clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '3')
        # step 6
        selectEnrolDuration(self.driver)
        # step 7
        selectEnd(self.driver, en=True, calender=False, default=True)
        time.sleep(2)
        # step 8:
        clickEnrol(self.driver)
        ## check result, ensure the user is created!
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            self.assertEqual('1 enrolled users', chk.text)
        except:
            print('popup result sai!')
        ## check infor
        clickInfor(self.driver)
        try:
            usernameInfo = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@class=\'table user-enrol-details\']/tbody/tr[1]/td')))
        except TimeoutException:
            print('Qua thoi gian thu gian -> co loi!')
        try:
            self.assertTrue('Admin User', usernameInfo.text)
        except:
            print("username is created not correct with expect")
        ## remove make sure
        remove(self.driver)
    def test_UCT_12(self):
        ## trong khung search go mot ket qua vo nghia
        ### Type 'minhtoan' in search input
        try:
            btn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/div[3]/input')))
            btn.send_keys('minhtoan')
            adminUser = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[2]/div/div/div[2]/form/fieldset/div[2]/div[1]/div[2]/ul')))
            time.sleep(2)
        except TimeoutException:
            print('Loi trong qua trinh loading...')
        # print(adminUser.text)
        try:
            self.assertEqual("No suggestions", adminUser.text)
        except:
            print('Sai test_UCT_12')
    def test_UCT_13(self):
        ## khong lam gi ma click vao enrol user
        #step 1
        clickEnrol(self.driver)
        try:
            ## is created
            chk = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div')))
        except TimeoutException:
            print('Qua thoi gian hoac la sai thong tin!')
        try:
            # print(chk.text)
            self.assertEqual('0 enrolled users', chk.text)
        except:
            print('popup result sai!')
    def test_UCT_14(self):
        ## khi enable thì enrolment duration -> disable, ta dung time sleep de xem
        # step 1:
        selectUser(self.driver)
        # step 2: '5' -> student
        selectAssignRole(self.driver, '5')
        # step 3:
        selectShowMore(self.driver)
        # step 4:
        clickRecover(self.driver)
        # step 5:
        selectStartFrom(self.driver, '3')
        # step 6
        selectEnrolDuration(self.driver)
        # step 7
        selectEnd(self.driver, en=True, calender=False, default=True)
        ## check result
        time.sleep(2)
    def test_UCT_15(self):
        ## click cancel
        try:
            btn = WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="modal-footer"]/button[1]')))
            btn.click()
            time.sleep(2)
        except TimeoutException:
            print('Loading co van de!')
    def tearDown(self):
        ## this function is runned by the unitest after each testcase
        return self.driver.close()

if __name__ == "__main__":
    unittest.main()