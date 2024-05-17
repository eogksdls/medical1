# 다음 역대관객순 -> 2019 ~ 2023 웹스크래핑 후 가져오기

import oracledb
import requests
import time
import random
import urllib.request
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

# 0. 다음 영화 페이지 이동
browser.get(url)
time.sleep(3)


# 1. blank 딕셔너리, 리스트 생성
movie_data = {}
year_list = [2019,2020,2021,2022,2023]
title_list = []
viewer_list = []
rating_list = []

# 2. 데이터 추출
# with open("daum_movie.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())


left = 680
num = 1
pyautogui.scroll(-150)
time.sleep(2)
for i in range(len(year_list)):
    
    # 3. 스크롤
    pyautogui.moveTo(left,380)
    time.sleep(1)
    pyautogui.click()
    pyautogui.scroll(-150)
    time.sleep(2)
    
    left -= 50
    
    #------------------------------------------------------------------
    
    # 4. 웹스크래핑
    soup  = BeautifulSoup(browser.page_source,"lxml")

    movie_ul = soup.find("ul",{"class":"c-list-basic ty_flow35"})
    
    movie = movie_ul.find_all("li")
    # print(len(movie))
    
    print("[ ",year_list[i],"년도 역대 관객순 1위 영화 ]")
    print("-"*40)
    rank = int(movie[0].find("span",{"class":"badge-basic"}).text)
    print("순위 : ", rank)
    
    title = movie[0].find("strong",{"class":"tit-g clamp-g"}).a.text
    print("영화 제목 : ",title)
    title_list.append(title)
    
    # 관객수, 평점 알기-------------------------------------------------------
    pyautogui.scroll(-150)
    time.sleep(2)   
    pyautogui.moveTo(460,500)
    time.sleep(2)
    pyautogui.click()
    
    soup  = BeautifulSoup(browser.page_source,"lxml")
    content_all = soup.find("dl",{"class":"conts-richx"})
    content = content_all.find_all("dd")
    
    viewer = int(content[5].text.replace(',','').replace('"','').replace('명',''))
    print("관객수 : ",format(viewer,','),"명")
    viewer_list.append(viewer)
    
    rating = content[4].find("span",{"class":"gem-star-point"}).text[2:5].replace('"','')
    print("평점 : ",rating)
    rating_list.append(rating)
    
    print("-"*40)
    
    #------------------------------------------------------------------------
    
    
    time.sleep(3)
    # 5. 이전 화면으로 돌아가기
    browser.back()
    time.sleep(3)


# 6. 딕셔너리 저장   
movie_data['year'] = year_list
movie_data['title'] = title_list
movie_data['viewer'] = viewer_list
movie_data['rating'] = rating_list
print(movie_data)

df = pd.DataFrame(movie_data)
print(df)
    


