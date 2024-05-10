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

def clickToMyCourses(driver):
    try:
        my_courses = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/my/courses.php']")))
        my_courses.click()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

def clickToMyFirstCourse(driver):
    try:
        my_first_course = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/course/view.php?id=2']")))
        my_first_course.click()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.") 

def toggleEditMode(driver):
    try:
        edit_link = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "//form[@action='https://sandbox.moodledemo.net/editmode.php']")))
        edit_link.click()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

def addQuiz(driver):
    try:
        add_button = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-sectionid='1']")))
        add_button.click()
        WebDriverWait(driver, 20, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    try:
        quiz_link = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
           (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/course/mod.php?id=2&add=quiz&section=1&beforemod=0']")))
        quiz_link.click()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    try:
        name = WebDriverWait(driver, 20, 2).until(
            EC.presence_of_element_located((By.NAME, "name")))
        name.send_keys("quiz1")
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    try:
        save_button = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
            (By.ID, "id_submitbutton2")))
        save_button.click()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    

def clickToGrades(driver):
    try:
        grades_nav_link = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
           (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/grade/report/index.php?id=2']")))
        grades_nav_link.click()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

def removeTotalGrade(driver):
    try:
        input_field = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
            (By.ID, "grade_4_1")))
        input_field.clear()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    try:
        save_button = WebDriverWait(driver, 20, 2).until(
            EC.element_to_be_clickable((By.ID, "gradersubmit")))
        save_button.click()
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

def removeGrade(driver):
    try:
        input_field = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
            (By.XPATH, f'/html/body/div[4]/div[5]/div/div[3]/div/section/div/form/div/div[1]/table/tbody/tr[3]/td[2]/div/div[1]/div[1]/input')))
        input_field.clear()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    try:
        save_button = WebDriverWait(driver, 20, 2).until(
            EC.element_to_be_clickable((By.ID, "gradersubmit")))
        save_button.click()
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
     
def removeQuiz(driver):
    try:
        option = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
            (By.XPATH, f'/html/body/div[4]/div[5]/div/div[3]/div/section/div/div/div/ul/li[2]/div[1]/div[2]/ul/li/div[2]/div[2]/div[4]/div/div/div/div/a')))
        option.click()
        WebDriverWait(driver, 20, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-menu menu dropdown-menu-right show")))
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    try:
        delete_link = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
           (By.XPATH, f'/html/body/div[4]/div[5]/div/div[3]/div/section/div/div/div/ul/li[2]/div[1]/div[2]/ul/li/div[2]/div[2]/div[4]/div/div/div/div/div/a[8]')))
        delete_link.click()
        WebDriverWait(driver, 20, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    try:
        submit_link = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
           (By.XPATH, f'/html/body/div[8]/div[2]/div/div/div[3]/button[2]')))
        submit_link.click()
        time.sleep(0.5)
    except TimeoutException:
        print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
    

def fillForm(driver, grade, total_grade):
    grade_input = WebDriverWait(driver, 20, 2).until(
            EC.element_to_be_clickable((By.XPATH, f'/html/body/div[4]/div[5]/div/div[3]/div/section/div/form/div/div[1]/table/tbody/tr[3]/td[2]/div/div[1]/div[1]/input')))
    grade_input.send_keys(grade)
    total_grade_input = WebDriverWait(driver, 20, 2).until(
            EC.element_to_be_clickable((By.ID, "grade_4_1")))
    total_grade_input.send_keys(total_grade)

    save_button = WebDriverWait(driver, 20, 2).until(
        EC.element_to_be_clickable((By.ID, "gradersubmit")))
    save_button.click()





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
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
        self.lst = lst = [['0','0'],
                          ['0','5'],
                          ['0','10'],
                          ['5','0'],
                          ['5','5'],
                          ['5','10'],
                          ['10','0'],
                          ['10','5'],
                          ['10','10']]
    
    ## tests

    def test_1(self):
            clickToMyCourses(self.driver)
            clickToMyFirstCourse(self.driver)
            toggleEditMode(self.driver)
            addQuiz(self.driver)
            clickToGrades(self.driver)
            data =  self.lst[0]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
            removeGrade(self.driver)
            removeTotalGrade(self.driver)
    def test_2(self):
            clickToMyCourses(self.driver)
            clickToMyFirstCourse(self.driver)
            toggleEditMode(self.driver)
            clickToGrades(self.driver)
            data =  self.lst[1]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
            removeGrade(self.driver)
            removeTotalGrade(self.driver)
    def test_3(self):
            clickToMyCourses(self.driver)
            clickToMyFirstCourse(self.driver)
            toggleEditMode(self.driver)
            clickToGrades(self.driver)
            data =  self.lst[2]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
            removeGrade(self.driver)
            removeTotalGrade(self.driver)
    def test_4(self):
            clickToMyCourses(self.driver)
            clickToMyFirstCourse(self.driver)
            toggleEditMode(self.driver)
            clickToGrades(self.driver)
            data =  self.lst[3]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
            removeGrade(self.driver)
            removeTotalGrade(self.driver)
    def test_5(self):
            clickToMyCourses(self.driver)
            clickToMyFirstCourse(self.driver)
            toggleEditMode(self.driver)
            clickToGrades(self.driver)
            data =  self.lst[4]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
            removeGrade(self.driver)
            removeTotalGrade(self.driver)
    def test_6(self):
            clickToMyCourses(self.driver)
            clickToMyFirstCourse(self.driver)
            toggleEditMode(self.driver)
            clickToGrades(self.driver)
            data =  self.lst[5]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
            removeGrade(self.driver)
            removeTotalGrade(self.driver)
    def test_7(self):
            clickToMyCourses(self.driver)
            clickToMyFirstCourse(self.driver)
            toggleEditMode(self.driver)
            clickToGrades(self.driver)
            data =  self.lst[6]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
            removeGrade(self.driver)
            removeTotalGrade(self.driver)
    def test_8(self):
            clickToMyCourses(self.driver)
            clickToMyFirstCourse(self.driver)
            toggleEditMode(self.driver)
            clickToGrades(self.driver)
            data =  self.lst[7]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
            removeGrade(self.driver)
            removeTotalGrade(self.driver)
    def test_9(self):
            clickToMyCourses(self.driver)
            clickToMyFirstCourse(self.driver)
            toggleEditMode(self.driver)
            clickToGrades(self.driver)
            data =  self.lst[8]
            grade, total_grade = data[0], data[1]
            fillForm(self.driver, grade, total_grade)
            removeGrade(self.driver)
            removeTotalGrade(self.driver)
    
    

    def tearDown(self):
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()

 