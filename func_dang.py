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

def log(func):
    def inner(*args, **kwargs):
        print(func.__name__, "is running")
        result = func(*args, **kwargs)
        return result
    return inner

def clickToGrades(driver):
    try:
        grades_nav_link = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
           (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/grade/report/index.php?id=2']")))
        grades_nav_link.click()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

def fillForm(driver, grade, total_grade):
    grade_input = WebDriverWait(driver, 20, 2).until(
            EC.element_to_be_clickable((By.ID, "grade_4_2")))
    grade_input.send_keys(grade)
    total_grade_input = WebDriverWait(driver, 20, 2).until(
            EC.element_to_be_clickable((By.ID, "grade_4_1")))
    total_grade_input.send_keys(total_grade)

    save_button = WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "gradersubmit")))
    save_button.click()
    WebDriverWait(driver, 20, 2).until(EC.invisibility_of_element_located(
        (By.ID, "gradersubmit")))
    try:
        driver.get(
            f"https://sandbox.moodledemo.net/grade/report/grader/index.php?id=2")
        time.sleep(2)
    except:
        pass


def toggleEditMode(driver):
    try:
        grades_nav_link = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
           (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/grade/report/grader/index.php?id=2']")))
        grades_nav_link.click()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")


class Test_Grade(unittest.TestCase):
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
            username.send_keys("teacher")
            password.send_keys("sandbox")
            password.submit()
            time.sleep(0.5)
        except TimeoutException:
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")\
        # Access My_courses
        try:
            dashboard_link = WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/my/courses.php']")))
            dashboard_link.click()
            time.sleep(0.5)
        except TimeoutException:
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
        # Access example course
        try:
            dashboard_link = WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/course/view.php?id=2']")))
            dashboard_link.click()
            time.sleep(0.5)
        except TimeoutException:
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
        # Access Grades
        try:
            dashboard_link = WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/grade/report/index.php?id=2']")))
            dashboard_link.click()
            time.sleep(0.5)
        except TimeoutException:
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
        self.lst = lst = [['0', '0'],
                          ['0', '5'],
                          ['0', '10'],
                          ['5', '0'],
                          ['5', '5'],
                          ['5', '10'],
                          ['10', '0'],
                          ['10', '5'],
                          ['10', '10']]
    
    ## tests
    def test_1(self):
            toggleEditMode(self.driver)
            data =  self.lst[0]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
    def test_2(self):
            toggleEditMode(self.driver)
            data =  self.lst[1]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
    def test_3(self):
            toggleEditMode(self.driver)
            data =  self.lst[2]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
    def test_4(self):
            toggleEditMode(self.driver)
            data =  self.lst[3]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
    def test_5(self):
            toggleEditMode(self.driver)
            data =  self.lst[4]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
    def test_6(self):
            toggleEditMode(self.driver)
            data =  self.lst[5]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
    def test_7(self):
            toggleEditMode(self.driver)
            data =  self.lst[6]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
    def test_8(self):
            toggleEditMode(self.driver)
            data =  self.lst[7]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
    def test_9(self):
            toggleEditMode(self.driver)
            data =  self.lst[8]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
    
    

    def tearDown(self):
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()

 