import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rozetka.com.ua")
driver.maximize_window()
time.sleep(5)

driver.quit()