import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
time.sleep(30)
first_name = driver.find_element_by_css_selector('[placeholder="First Name"]')
first_name.send_keys('Sonya')
last_name = driver.find_element_by_css_selector('[placeholder="Last Name"]')
last_name.send_keys('Ivanova')
email = driver.find_element_by_css_selector('[type="email"]')
email.send_keys('schash1@mail.ru')
phone = driver.find_element_by_css_selector('[type="tel"]')
phone.send_keys('9175407244')
gender = driver.find_element_by_css_selector('[value="FeMale"]')
gender.click()
year = driver.find_element_by_id('yearbox')
select_year = Select(year)
select_year.select_by_visible_text('2000')
month = driver.find_element_by_css_selector('[ng-model="monthbox"]')
select_month = Select(month)
select_month.select_by_visible_text('May')
day = driver.find_element_by_id('daybox')
select_day = Select(day)
select_day.select_by_visible_text('31')
password = driver.find_element_by_css_selector('[ng-model="Password"]')
password.send_keys('Asdfgh1')
confirm_password = driver.find_element_by_css_selector('[ng-model="CPassword"]')
confirm_password.send_keys('Asdfgh1')
photo = ('C:\Софья\Фотки\IMG_0622.jpg')
upload_photo = driver.find_element_by_id('imagesrc')
upload_photo.send_keys(photo)
driver.execute_script("window.scrollBy(0, 300);")
submit = driver.find_element_by_id('submitbtn')
submit.click()
time.sleep(5)
driver.quit()
