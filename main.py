from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')

elem_username = browser.find_element(By.ID, 'username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element(By.ID, 'password')
elem_password.send_keys('kohei')

elem_login_btn = browser.find_element(By.ID, 'login-btn')
elem_login_btn.click()

time.sleep(5)
browser.quit()
