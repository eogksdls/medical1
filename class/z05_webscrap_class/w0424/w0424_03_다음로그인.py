import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.daum.net"

# 크롬브라우저 열기
browser = webdriver.Chrome()

# 다음 페이지로 이동
browser.get(url)
time.sleep(random.randint(2,5))
elem = browser.find_element(By.XPATH,'//*[@id="loginMy"]/div/div[1]/div/a')
# 로그인 버튼 클릭
elem.click()
time.sleep(random.randint(2,5))

# # 자동화 방지를 위한 자바스크립트 활용 데이터 입력
# input_js = 'document.getElementById("loginId--1").value="{id}"; \
#             document.getElementById("password--2").value="{pw}"; \
#             '.format(id='01053807159',pw='ivy000914')
# time.sleep(random.randint(2,5))

# # 자바스크립트 명령어 실행
# browser.execute_script(input_js)
# time.sleep(random.randint(2,5))

# 새창
browser.switch_to.window(browser.window_handles[1])

# 아이디 입력
elem2 = browser.find_element(By.XPATH,'//*[@id="loginId--1"]')
id = "01053807159"
elem2.send_keys(id)
time.sleep(random.randint(2,5))
# 패스워드 입력
elem3 = browser.find_element(By.XPATH,'//*[@id="password--2"]')
pw = "ivy000914"
elem3.send_keys(pw)
time.sleep(random.randint(2,5))

# 로그인 버튼 클릭
elem4 = browser.find_element(By.XPATH,'//*[@id="mainContent"]/div/div[1]/form/div[4]/button[1]')
time.sleep(random.randint(2,5))
elem4.click()
time.sleep(5)


# 로봇이 아닙니다.
elem5 = browser.find_element(By.XPATH,'//*[@id="recaptcha-anchor"]')
elem5.click()
time.sleep(random.randint(2,5))
elem4 = browser.find_element(By.XPATH,'//*[@id="mainContent"]/div/div[1]/form/div[4]/button[1]')
elem4.click()

time.sleep(100)
           