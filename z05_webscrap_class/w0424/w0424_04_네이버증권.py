import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.naver.com"

browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)

elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[6]/a')
elem.click()
time.sleep(3)

# 새창으로 변경
browser.switch_to.window(browser.window_handles[1])

elem2 = browser.find_element(By.XPATH,'//*[@id="container"]/div[2]/div/div[3]/a')
time.sleep(random.randint(2,5))
elem2.click()

time.sleep(100)