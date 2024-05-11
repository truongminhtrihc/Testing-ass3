"""
    author: Pham Thanh Phong
    date: 2024:11:05
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
from selenium.webdriver.chrome.options import Options

## create decorator function
def log(func):
    def inner(*args, **kwargs):
        print(func.__name__, "is running")
        result = func(*args, **kwargs)
        return result
    return inner


def accessGradeDetail(driver):
	try:
		td_element = WebDriverWait(driver, 10, 2).until(EC.visibility_of_element_located(
		(By.XPATH, "//td[contains(@class, 'grade') and contains(@class, 'lastcol')]")))

		button = WebDriverWait(td_element, 10, 2).until(EC.element_to_be_clickable(
		(By.XPATH, ".//button[@data-toggle='dropdown']")))
		button.click()

		edit_grade = WebDriverWait(td_element, 10, 2).until(EC.element_to_be_clickable(
		(By.XPATH, ".//a[contains(text(), 'Edit')]")))
		edit_grade.click()
	
	except TimeoutException:
		print("Không tìm được thẻ tđ đó")

def changeDateHidden(driver, day, month, year, hour, minute):
	try:
		checkbox = WebDriverWait(driver, 10, 2).until(EC.element_to_be_clickable(
		(By.ID, "id_hiddenuntil_enabled")))
		if not checkbox.is_selected():
			checkbox.click()
	except TimeoutException:
		print("Không thấy check box")
	try:
		day_select = Select(WebDriverWait(driver, 20, 2).until(
		EC.element_to_be_clickable((By.ID, "id_hiddenuntil_day"))))
		day_select.select_by_value(day)

		year_select = Select(WebDriverWait(driver, 20, 2).until(
		EC.element_to_be_clickable((By.ID, "id_hiddenuntil_year"))))
		year_select.select_by_value(year)

		month_select = Select(WebDriverWait(driver, 20, 2).until(
		EC.element_to_be_clickable((By.ID, "id_hiddenuntil_month"))))
		month_select.select_by_value(month)

		hour_select = Select(WebDriverWait(driver, 20, 2).until(
		EC.element_to_be_clickable((By.ID, "id_hiddenuntil_hour"))))
		hour_select.select_by_value(hour)

		min_select = Select(WebDriverWait(driver, 20, 2).until(
		EC.element_to_be_clickable((By.ID, "id_hiddenuntil_minute"))))
		min_select.select_by_value(minute)
	except TimeoutException:
		print("Không thể sửa ngày tháng")

def editGradeInDetail(driver, score, day, month, year, hour, minute):
	accessGradeDetail(driver)
	changeDateHidden(driver, day, month, year, hour, minute)
 
	try:
		checkbox = WebDriverWait(driver, 10, 2).until(EC.element_to_be_clickable(
		(By.ID, "id_overridden")))
		if not checkbox.is_selected():
			checkbox.click()
			print("Đã nhấn vào checkbox.")
		else:
			print("Checkbox đã được chọn.")
	except TimeoutException:
		print("Không thấy check box")
	
	try:
		score_input = WebDriverWait(driver, 20, 2).until(
                EC.presence_of_element_located((By.ID, "id_finalgrade")))
		score_input.clear()
		score_input.send_keys(score)
		time.sleep(5)
	except TimeoutException:
		print("Không thấy ô điểm")
	
	try:
		save_button = WebDriverWait(driver, 20, 2).until(EC.element_to_be_clickable(
			(By.ID, "id_submitbutton")))
		save_button.click()
		time.sleep(0.5)
	except TimeoutException:
		print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")

def checkEsixtSkipTourForFindingStudent(driver):
	try:
		div_element = WebDriverWait(driver, 5, 2).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="tour-step-tool_usertours_3_14_1683276000-0"]/div')))
		print("Đã tìm thấy thẻ div cần thiết.")

		button = WebDriverWait(driver, 5, 2).until(
		EC.element_to_be_clickable((By.XPATH, './/button[contains(text(), "Skip")]')))
		print("Đã tìm thấy nút bấm có chứa chữ 'skip'.")

		button.click()
		print("Đã nhấn vào nút bấm.")
	except TimeoutException:
			print("Không có skip tour")

def checkEsixtSkipTour(driver):
	try:
		div_element = WebDriverWait(driver, 5, 2).until(
		EC.presence_of_element_located((By.XPATH, '//*[@id="tour-step-tool_usertours_3_10_1641972470-0"]/div')))
		print("Đã tìm thấy thẻ div cần thiết.")

		button = WebDriverWait(driver, 5, 2).until(
		EC.element_to_be_clickable((By.XPATH, './/button[contains(text(), "Skip")]')))
		print("Đã tìm thấy nút bấm có chứa chữ 'skip'.")

		button.click()
		print("Đã nhấn vào nút bấm.")
	except TimeoutException:
			print("Không có skip tour")


class Test_Edit_Grade_In_Detail(unittest.TestCase):
    def setUp(self):
        ## Preconditions for Test_NewEventWithEquivalence
        options = Options()
        options.add_argument("--start-maximized")
        service = Service(executable_path="./chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)
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
                # Access Dashboard
        
        #Access my course
        try:
            my_course = WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/my/courses.php']")))
            my_course.click()
            time.sleep(0.5)
        except TimeoutException:
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
            
            
            
        #Access first course
        try:
            first_course = WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/course/view.php?id=2']")))
            first_course.click()
            time.sleep(0.5)
        except TimeoutException:
            print("Vui lòng thực hiện lại chức năng vì thời gian load phần tử quá lâu.")
        
        
        checkEsixtSkipTour(self.driver)
        try:
            edit_mode  = WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable((By.XPATH, "//form[@action='https://sandbox.moodledemo.net/editmode.php']")))
            edit_mode.click()
        except TimeoutException:
            print("Không nhấn được edit mode")
		
  	
        checkEsixtSkipTour(self.driver)
        try:
            grade_link  =  WebDriverWait(self.driver, 20, 2).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[href='https://sandbox.moodledemo.net/grade/report/index.php?id=2']")))
            grade_link.click()
        except TimeoutException:
            print("Không vào được điểm")
        
        checkEsixtSkipTour(self.driver)
        checkEsixtSkipTourForFindingStudent(self.driver)
        self.scores = [['0'], ['1'], ['2'], ['3'], ['4'], ['4.5'],['5'], ['6'], ['7'], ['8'], ['9'], ['10']]
        self.Datetime = [
            				['10', '1', '2020', '5', '9'], 
            				['11', '2', '2020', '2', '22'], 
            				['12', '3', '2020', '3', '32'], 
            				['13', '4', '2020', '4', '41'], 
            				['14', '5', '2020', '5', '25'], 
            				['15', '6', '2020', '6', '36'], 
            				['16', '7', '2020', '7', '17'], 
            				['17', '8', '2020', '8', '18'], 
            				['18', '9', '2020', '9', '39'], 
            				['19', '10', '2020', '10', '32'], 
            				['20', '11', '2020', '11', '33'], 
            				['21', '12', '2020', '12', '13'], 
                        ]
    
    
    ## tests
    
    def test_grade_detail_0(self):
        data =  self.scores[0]
        score = data[0]
        dataTime = self.Datetime[0]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)
    
    
    def test_grade_detail_1(self):
        data =  self.scores[1]
        score = data[0]
        dataTime = self.Datetime[1]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_2(self):
        data =  self.scores[2]
        score = data[0]
        dataTime = self.Datetime[2]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_3(self):
        data =  self.scores[3]
        score = data[0]
        dataTime = self.Datetime[3]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_4(self):
        data =  self.scores[4]
        score = data[0]
        dataTime = self.Datetime[4]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_5(self):
        data =  self.scores[5]
        score = data[0]
        dataTime = self.Datetime[5]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_6(self):
        data =  self.scores[6]
        score = data[0]
        dataTime = self.Datetime[6]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_7(self):
        data =  self.scores[7]
        score = data[0]
        dataTime = self.Datetime[7]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_8(self):
        data =  self.scores[8]
        score = data[0]
        dataTime = self.Datetime[8]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_9(self):
        data =  self.scores[9]
        score = data[0]
        dataTime = self.Datetime[9]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_10(self):
        data =  self.scores[10]
        score = data[0]
        dataTime = self.Datetime[10]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)

    def test_grade_detail_11(self):
        data =  self.scores[11]
        score = data[0]
        dataTime = self.Datetime[11]
        day, month, year, hour, minute = dataTime[0], dataTime[1], dataTime[2], dataTime[3], dataTime[4]
        editGradeInDetail(self.driver, score,  day, month, year, hour, minute)
        time.sleep(0.5)
        
     

    

    def tearDown(self):
        ## this function is runned by the unitest after each testcase
        return self.driver.close()


if __name__ == "__main__":
    unittest.main()


