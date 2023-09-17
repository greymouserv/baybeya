from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

un = 'deltac1537@gmail.com'
psw = '8YbYaZwE!7*+fez'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.kleinanzeigen.de/m-einloggen.html')
sleep(0.1)
driver.find_element(By.XPATH, '//*[@id="login-form"]/div[1]/div/div/input').send_keys(un)
sleep(0.1)
driver.find_element(By.XPATH, '//*[@id="login-form"]/div[2]/div/div/input').send_keys(psw)
sleep(15)
driver.find_element(By.XPATH, '//*[@id="login-submit"]').click()
sleep(10)
