import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.naver.com"

# 크롬브라우저 열기
browser = webdriver.Chrome()

# 네이버 페이지로 이동
browser.get(url)
time.sleep(3) # 정보 읽는 시간
elem = browser.find_element(By.XPATH,'//*[@id="account"]/div/a')
# 로그인 버튼 클릭
elem.click()

time.sleep(random.randint(2,5))

# 제이쿼리에선 : $("#id"), 자바스크립트 : document.getElementById("id").value
# input_js = ''.format("aaa","1111") 형식으로 써야함

# 자동화 방지를 위한 자바스크립트 활용 데이터 입력
input_js = 'document.getElementById("id").value="{id}"; \
            document.getElementById("pw").value="{pw}"; \
            '.format(id="ivy0914", pw="Dlsgk5527N!")
time.sleep(random.randint(2,5))
# 자바스크립트 명령어 실행
browser.execute_script(input_js)

#-----------------------------------------------------------
# # 아이디 입력창 선택
# elem2 = browser.find_element(By.ID,'id')
# # id 창에 글자 입력
# elem2.send_keys("ivy0914")
# time.sleep(random.randint(2,5))

# elem3 = browser.find_element(By.ID,'pw')
# elem3.send_keys("1111")
#-------------------------------------------------------------

time.sleep(random.randint(2,5))
elem4 = browser.find_element(By.XPATH,'//*[@id="log.login"]')
time.sleep(random.randint(2,5))
# 로그인 버튼 클릭
elem4.click()


time.sleep(100)