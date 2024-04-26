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
    time.sleep(0.5)
    # month
    month_dropdown = Select(WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "id_timestart_month"))))
    month_dropdown.select_by_value(month)
    time.sleep(0.5)
    # date
    day_dropdown = Select(WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "id_timestart_day"))))
    day_dropdown.select_by_value(day)
    time.sleep(0.5)
    hour_dropdown = Select(WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "id_timestart_hour"))))
    hour_dropdown.select_by_value(hour)
    time.sleep(0.5)
    min_dropdown = Select(WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "id_timestart_minute"))))
    min_dropdown.select_by_value(minute)
    time.sleep(0.5)

    save_button = WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
    save_button.click()
    time.sleep(0.5)
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
    except:
        print('---------------------------------')
    print('------------------end this test!--------------')

class Test_NewEventWithEquivalence(unittest.TestCase):
    def setUp(self):
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

    def test_1(self):
        clickToNewevent(self.driver)
        data =  self.lst[0]
        title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
        fillForm(self.driver, title, day, month, year, hour, minute)


    def tearDown(self):
        for i in range(3):
            print(f"sleeping for {i} seconds")
            time.sleep(1)
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()







# def selectdate(day, month, year, hour, minute):
#     try:
#         # year
#         print("Testcase create new event for day:month:year:hour:minute",
#               day, month, year, hour, minute, "is Running", sep='-')
#         year_dropdown = Select(WebDriverWait(driver, 20, 2).until(
#             EC.element_to_be_clickable((By.ID, "id_timestart_year"))))
#         year_dropdown.select_by_value(year)
#         time.sleep(0.5)
#         # month
#         month_dropdown = Select(WebDriverWait(driver, 20, 2).until(
#             EC.element_to_be_clickable((By.ID, "id_timestart_month"))))
#         month_dropdown.select_by_value(month)
#         time.sleep(0.5)
#         # date
#         day_dropdown = Select(WebDriverWait(driver, 20, 2).until(
#             EC.element_to_be_clickable((By.ID, "id_timestart_day"))))
#         day_dropdown.select_by_value(day)
#         time.sleep(0.5)
#         hour_dropdown = Select(WebDriverWait(driver, 20, 2).until(
#             EC.element_to_be_clickable((By.ID, "id_timestart_hour"))))
#         hour_dropdown.select_by_value(hour)
#         time.sleep(0.5)
#         min_dropdown = Select(WebDriverWait(driver, 20, 2).until(
#             EC.element_to_be_clickable((By.ID, "id_timestart_minute"))))
#         min_dropdown.select_by_value(minute)
#         time.sleep(0.5)

#         save_button = WebDriverWait(driver, 20, 2).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
#         save_button.click()
#         time.sleep(0.5)
#         WebDriverWait(driver, 20, 2).until(EC.invisibility_of_element_located(
#             (By.XPATH, "//button[contains(text(),'Save')]")))
#         try:
#             d = datetime.datetime(int(year), int(month), int(day))
#         except:
#             d = datetime.datetime(int(year), int(
#                 month)+1 if int(month) != 12 else 1, 1)
#         try:
#             driver.get(
#                 f"https://sandbox.moodledemo.net/calendar/view.php?view=month&time={int(d.timestamp())}")
#         except:
#             print('---------------------------------')
#         print('------------------end this test!--------------')
#         time.sleep(3)
#     except TimeoutException:
#         print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")


# def selectDateTime(lst):
#     for data in lst:
#         title, day, month, year, hour, minute = data[0], data[1], data[2], data[3], data[4], data[5]
#         try:
#             clickToNewevent()
#             # title
#             name_input = WebDriverWait(driver, 20, 2).until(
#                 EC.element_to_be_clickable((By.ID, "id_name")))
#             name_input.send_keys(title)
#             time.sleep(0.5)
#             selectdate(day, month, year, hour, minute)

#             # time.sleep(3)
#         except TimeoutException:
#             print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")


# # def start(title, day, month, year, hour, minute):
# #     login("student", "sandbox")
# #     clickToNewevent()
# #     selectDateTime(title, day, month, year, hour, minute)


# def test_equivalent_class_New_Event():
#     # try:
#     lst = [['test-1', '15', '4', '2000', '10', '10'],
#            ['test-2', '29', '4', '2000', '10', '10'],
#            ['test-3', '30', '4', '2000', '10', '10'],
#            ['test-4', '31', '4', '2000', '10', '10'],
#            ['test-5', '15', '4', '1900', '10', '10'],
#            ['test-6', '15', '4', '2004', '10', '10'],
#            ['test-7', '15', '4', '1901', '10', '10'],
#            ['test-8', '29', '4', '1900', '10', '10'],
#            ['test-9', '29', '4', '2004', '10', '10'],
#            ['test-10', '30', '4', '1900', '10', '10'],
#            ['test-11', '30', '4', '2004', '10', '10'],
#            ['test-12', '30', '4', '1901', '10', '10'],
#            ['test-13', '31', '4', '1900', '10', '10'],
#            ['test-14', '31', '4', '2004', '10', '10'],
#            ['test-15', '31', '4', '1901', '10', '10'],
#            ['test-16', '15', '1', '2000', '10', '10'],
#            ['test-17', '29', '1', '2000', '10', '10'],
#            ['test-18', '30', '1', '2000', '10', '10'],
#            ['test-19', '31', '1', '2000', '10', '10'],
#            ['test-20', '15', '1', '1900', '10', '10'],
#            ['test-21', '15', '1', '2004', '10', '10'],
#            ['test-22', '15', '1', '1901', '10', '10'],
#            ['test-23', '29', '1', '1900', '10', '10'],
#            ['test-24', '29', '1', '2004', '10', '10'],
#            ['test-25', '29', '1', '1901', '10', '10'],
#            ['test-26', '30', '1', '1900', '10', '10'],
#            ['test-27', '30', '1', '2004', '10', '10'],
#            ['test-28', '30', '1', '1901', '10', '10'],
#            ['test-29', '31', '1', '1900', '10', '10'],
#            ['test-30', '32', '1', '2004', '10', '10'],
#            ['test-31', '31', '1', '1901', '10', '10'],
#            ['test-32', '15', '2', '2000', '10', '10'],
#            ['test-33', '29', '2', '2000', '10', '10'],
#            ['test-34', '30', '2', '2000', '10', '10'],
#            ['test-35', '31', '2', '2000', '10', '10'],
#            ['test-36', '15', '2', '1900', '10', '10'],
#            ['test-37', '15', '2', '2004', '10', '10'],
#            ['test-38', '15', '2', '1901', '10', '10'],
#            ['test-39', '29', '2', '1900', '10', '10'],
#            ['test-40', '29', '2', '2004', '10', '10'],
#            ['test-41', '29', '2', '1901', '10', '10'],
#            ['test-42', '30', '2', '1900', '10', '10'],
#            ['test-43', '30', '2', '2004', '10', '10'],
#            ['test-44', '30', '2', '1901', '10', '10'],
#            ['test-45', '31', '2', '1900', '10', '10'],
#            ['test-46', '31', '2', '2004', '10', '10'],
#            ['test-47', '31', '2', '1901', '10', '10']]

#     login('student', 'sandbox')
#     accessToDashboard()
#     selectDateTime(lst)
#     # except :
#     #     print("Đường truyền mạng có vấn đề hoặc server đang có lỗi vui lòng thử lại!")
