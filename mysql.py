from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

import mysql.connector


options = uc.ChromeOptions()
options.add_argument("--start-maximized")
options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
browser = webdriver.Chrome(options = options, service = Service("chromedriver.exe"))
browser.get("https://www.woolmart.in/")
time.sleep(5)


mens=browser.find_element(By.XPATH , "//a[@href='/categories/mens']")
mens.click()
time.sleep(5)


acces=browser.find_element(By.XPATH , "//span[contains(text(), 'Accessories')]")
browser.execute_script("arguments[0].scrollIntoView();",acces)
time.sleep(5)
acces.click()
time.sleep(random.randint(5,10))

cap=browser.find_element(By.XPATH , "//span[contains(text(), 'Caps')]")
cap.click()
time.sleep(5)

text_list = []

all_name=browser.find_elements(By.CLASS_NAME,"teaser-name")

for element in all_name:
    
    #dic_={}
    #text_list.append(element.text)
    #dic_["product name"] = element.text
    text_list.append(element.text)
    


all_prize=browser.find_elements(By.CLASS_NAME,"actual-price")

for element in all_prize:
    
    text_list.append(element.text)


mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE TABLE kano (product_name VARCHAR(255), product_prize VARCHAR(255))")
except:
    pass


for item in range(len(text_list)//2):

    sql = "INSERT INTO kano (product_name, product_prize) VALUES (%s, %s)"
    val = (text_list[item],text_list[item+15])
    mycursor.execute(sql, val)


mydb.commit()

browser.quit()
