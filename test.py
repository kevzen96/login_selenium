from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = "Username123"
password = "123456"

# เปิด Browser
driver = webdriver.Chrome()

# เปิด web page
driver.get('http://127.0.0.1:5500/index.html#')

# ระบุบตำแหน่ง
time.sleep(2)
login = driver.find_element(By.XPATH, '/html/body/button') # ปุ่ม login
login.click()

time.sleep(2)
user = driver.find_element(By.XPATH, '//*[@id="id01"]/form/div[2]/input[1]')
pas = driver.find_element(By.XPATH, '//*[@id="id01"]/form/div[2]/input[2]')
user.send_keys(username)
time.sleep(1)
pas.send_keys(password + Keys.ENTER)



