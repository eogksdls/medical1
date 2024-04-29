import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://flight.naver.com/"

# 1. 네이버 페이지 이동
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)


# 박스 클릭
elem7 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]')
elem7.click()
time.sleep(1)

# 날짜지정 : 5월 14일
calendar_div = browser.find_element(By.CLASS_NAME,'sc-jqUVSM ilolms awesome-calendar')
calendar = calendar_div.find_elements(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[3]/td[3]/button')

time.sleep(2)


