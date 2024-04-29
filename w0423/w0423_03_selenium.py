import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# selenium은 자동화 프로그램

browser = webdriver.Chrome()
url = "https://www.naver.com/"
# 브라우저 페이지 열기
browser.get(url)

# 네이버 로그인 버튼을 클릭
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
elem.click() # 로그인 버튼을 클릭한 것과 동일
time.sleep(3) ##### 
browser.back() # 뒤로 가기, browser.forward() 앞으로 가기
browser.refresh() # F5 새로고침


# 네이버 검색부분에 검색어를 입력
elem = browser.find_element(By.ID,'query') # id가 query인 요소 선택
elem # 선택되어 있는 elem 요소들을 보여줌.
elem.click()
elem.send_keys("주식")



# 100초 대기
time.sleep(100)   # 얘 안쓰면 안됨, 정보를 못끌어온다


soup = BeautifulSoup(browser.page_source,"lxml")
with open("naver.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())
    
