"""
    author: Nguyen Minh Toan
    date: 2024:27:04
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

## create decorator function
def log(func):
    def inner(*args, **kwargs):
        print(func.__name__, "is running")
        result = func(*args, **kwargs)
        return result
    return inner


def clickToNewevent(driver):
    try:
        new_event_button = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-action='new-event-button']")))
        new_event_button.click()
        WebDriverWait(driver, 20, 2).until(
            EC.visibility_of_element_located((By.ID, "id_name")))
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
def fillForm(driver, title, day, month, year, hour, minute):
    ## fill title
    name_input = WebDriverWait(driver, 20, 2).until(
            EC.element_to_be_clickable((By.ID, "id_name")))
    name_input.send_keys(title)
    ## select dateTime
    ### seleect year
    year_dropdown = Select(WebDriverWait(driver, 20, 2).until(
            EC.element_to_be_clickable((By.ID, "id_timestart_year"))))
    year_dropdown.select_by_value(year)
    # month
    month_dropdown = Select(WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "id_timestart_month"))))
    month_dropdown.select_by_value(month)
    # date
    day_dropdown = Select(WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "id_timestart_day"))))
    day_dropdown.select_by_value(day)
    hour_dropdown = Select(WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "id_timestart_hour"))))
    hour_dropdown.select_by_value(hour)
    min_dropdown = Select(WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "id_timestart_minute"))))
    min_dropdown.select_by_value(minute)

    save_button = WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
    save_button.click()
    WebDriverWait(driver, 20, 2).until(EC.invisibility_of_element_located(
        (By.XPATH, "//button[contains(text(),'Save')]")))
    try:
        d = datetime.datetime(int(year), int(month), int(day))
    except:
        d = datetime.datetime(int(year), int(
            month)+1 if int(month) != 12 else 1, 1)
    try:
        driver.get(
            f"https://sandbox.moodledemo.net/calendar/view.php?view=month&time={int(d.timestamp())}")
        time.sleep(2)
    except:
        # print('hàm timestamp bị lỗi không biết nguyên nhân với một số ngày nhất định')
        pass

class Test_NewEventWithEquivalence(unittest.TestCase):
    def setUp(self):
        ## Preconditions for Test_NewEventWithEquivalence
        service = Service(executable_path="./chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        # Login account
        self.driver.get("https://sandbox.moodledemo.net/login/index.php")
        try:
            username = WebDriverWait(self.driver, 20, 2).until(
                EC.presence_of_element_located((By.NAME, "username")))
            password = WebDriverWait(self.driver, 20, 2).until(
                EC.presence_of_element_located((By.NAME, "password")))
            username.send_keys("student")
            password.send_keys("sandbox")
            password.submit()
            time.sleep(0.5)
        except TimeoutException:
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")\
                # Access Dashboard
        try:
            dashboard_link = WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/my/']")))
            dashboard_link.click()
            time.sleep(0.5)
        except TimeoutException:
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
        self.lst = lst = [['test-1', '15', '4', '2000', '10', '10'],
                          ['test-2', '29', '4', '2000', '10', '10'],
                          ['test-3', '30', '4', '2000', '10', '10'],
                          ['test-4', '31', '4', '2000', '10', '10'],
                          ['test-5', '15', '4', '1900', '10', '10'],
                          ['test-6', '15', '4', '2004', '10', '10'],
                          ['test-7', '15', '4', '1901', '10', '10'],
                          ['test-8', '29', '4', '1900', '10', '10'],
                          ['test-9', '29', '4', '2004', '10', '10'],
                          ['test-10', '30', '4', '1900', '10', '10'],
                          ['test-11', '30', '4', '2004', '10', '10'],
                          ['test-12', '30', '4', '1901', '10', '10'],
                          ['test-13', '31', '4', '1900', '10', '10'],
                          ['test-14', '31', '4', '2004', '10', '10'],
                          ['test-15', '31', '4', '1901', '10', '10'],
                          ['test-16', '15', '1', '2000', '10', '10'],
                          ['test-17', '29', '1', '2000', '10', '10'],
                          ['test-18', '30', '1', '2000', '10', '10'],
                          ['test-19', '31', '1', '2000', '10', '10'],
                          ['test-20', '15', '1', '1900', '10', '10'],
                          ['test-21', '15', '1', '2004', '10', '10'],
                          ['test-22', '15', '1', '1901', '10', '10'],
                          ['test-23', '29', '1', '1900', '10', '10'],
                          ['test-24', '29', '1', '2004', '10', '10'],
                          ['test-25', '29', '1', '1901', '10', '10'],
                          ['test-26', '30', '1', '1900', '10', '10'],
                          ['test-27', '30', '1', '2004', '10', '10'],
                          ['test-28', '30', '1', '1901', '10', '10'],
                          ['test-29', '31', '1', '1900', '10', '10'],
                          ['test-30', '32', '1', '2004', '10', '10'],
                          ['test-31', '31', '1', '1901', '10', '10'],
                          ['test-32', '15', '2', '2000', '10', '10'],
                          ['test-33', '29', '2', '2000', '10', '10'],
                          ['test-34', '30', '2', '2000', '10', '10'],
                          ['test-35', '31', '2', '2000', '10', '10'],
                          ['test-36', '15', '2', '1900', '10', '10'],
                          ['test-37', '15', '2', '2004', '10', '10'],
                          ['test-38', '15', '2', '1901', '10', '10'],
                          ['test-39', '29', '2', '1900', '10', '10'],
                          ['test-40', '29', '2', '2004', '10', '10'],
                          ['test-41', '29', '2', '1901', '10', '10'],
                          ['test-42', '30', '2', '1900', '10', '10'],
                          ['test-43', '30', '2', '2004', '10', '10'],
                          ['test-44', '30', '2', '1901', '10', '10'],
                          ['test-45', '31', '2', '1900', '10', '10'],
                          ['test-46', '31', '2', '2004', '10', '10'],
                          ['test-47', '31', '2', '1901', '10', '10']]
    ## tests
    
    def test_1(self):
            clickToNewevent(self.driver)
            data =  self.lst[0]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)
    

    
    def test_2(self):
            clickToNewevent(self.driver)
            data =  self.lst[1]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_3(self):
            clickToNewevent(self.driver)
            data =  self.lst[2]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_4(self):
            clickToNewevent(self.driver)
            data =  self.lst[3]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_5(self):
            clickToNewevent(self.driver)
            data =  self.lst[4]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_6(self):
            clickToNewevent(self.driver)
            data =  self.lst[5]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_7(self):
            clickToNewevent(self.driver)
            data =  self.lst[6]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_8(self):
            clickToNewevent(self.driver)
            data =  self.lst[7]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_9(self):
            clickToNewevent(self.driver)
            data =  self.lst[8]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_10(self):
            clickToNewevent(self.driver)
            data =  self.lst[9]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_11(self):
            clickToNewevent(self.driver)
            data =  self.lst[10]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_12(self):
            clickToNewevent(self.driver)
            data =  self.lst[11]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_13(self):
            clickToNewevent(self.driver)
            data =  self.lst[12]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_14(self):
            clickToNewevent(self.driver)
            data =  self.lst[13]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_15(self):
            clickToNewevent(self.driver)
            data =  self.lst[14]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_16(self):
            clickToNewevent(self.driver)
            data =  self.lst[15]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_17(self):
            clickToNewevent(self.driver)
            data =  self.lst[16]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_18(self):
            clickToNewevent(self.driver)
            data =  self.lst[17]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_19(self):
            clickToNewevent(self.driver)
            data =  self.lst[18]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_20(self):
            clickToNewevent(self.driver)
            data =  self.lst[19]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_21(self):
            clickToNewevent(self.driver)
            data =  self.lst[20]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_22(self):
            clickToNewevent(self.driver)
            data =  self.lst[21]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_23(self):
            clickToNewevent(self.driver)
            data =  self.lst[22]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_24(self):
            clickToNewevent(self.driver)
            data =  self.lst[23]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_25(self):
            clickToNewevent(self.driver)
            data =  self.lst[24]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_26(self):
            clickToNewevent(self.driver)
            data =  self.lst[25]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_27(self):
            clickToNewevent(self.driver)
            data =  self.lst[26]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_28(self):
            clickToNewevent(self.driver)
            data =  self.lst[27]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_29(self):
            clickToNewevent(self.driver)
            data =  self.lst[28]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_30(self):
            clickToNewevent(self.driver)
            data =  self.lst[29]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_31(self):
            clickToNewevent(self.driver)
            data =  self.lst[30]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_32(self):
            clickToNewevent(self.driver)
            data =  self.lst[31]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_33(self):
            clickToNewevent(self.driver)
            data =  self.lst[32]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_34(self):
            clickToNewevent(self.driver)
            data =  self.lst[33]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_35(self):
            clickToNewevent(self.driver)
            data =  self.lst[34]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_36(self):
            clickToNewevent(self.driver)
            data =  self.lst[35]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_37(self):
            clickToNewevent(self.driver)
            data =  self.lst[36]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_38(self):
            clickToNewevent(self.driver)
            data =  self.lst[37]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_39(self):
            clickToNewevent(self.driver)
            data =  self.lst[38]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_40(self):
            clickToNewevent(self.driver)
            data =  self.lst[39]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_41(self):
            clickToNewevent(self.driver)
            data =  self.lst[40]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_42(self):
            clickToNewevent(self.driver)
            data =  self.lst[41]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_43(self):
            clickToNewevent(self.driver)
            data =  self.lst[42]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_44(self):
            clickToNewevent(self.driver)
            data =  self.lst[43]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_45(self):
            clickToNewevent(self.driver)
            data =  self.lst[44]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_46(self):
            clickToNewevent(self.driver)
            data =  self.lst[45]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)


    
    def test_47(self):
            clickToNewevent(self.driver)
            data =  self.lst[46]
            title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
            fillForm(self.driver, title, day, month, year, hour, minute)
    

    def tearDown(self):
        ## this function is runned by the unitest after each testcase
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()


