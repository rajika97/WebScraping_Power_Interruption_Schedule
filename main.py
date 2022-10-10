from selenium import webdriver
import time
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
web.get("http://lecoapp.leco.lk:8091/LecoWebViews/Outage2022")
time.sleep(1)

Account_no = "0507853401"

searchBar = web.find_element("id", "username")
searchBar.send_keys(Account_no)

Click_find = web.find_element(By.XPATH, "/html/body/div[2]/main/div/div[1]/div/form/div/div[3]/input")
Click_find.click()

text = web.find_element(By.CSS_SELECTOR, "table").text
print (text)

