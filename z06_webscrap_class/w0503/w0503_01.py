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

# DB연결부분
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

# 0. 다음 영화 페이지 이동
browser.get(url)
time.sleep(3)


# 1.
year = [2020,2021,2022,2023]

# with open("daum_movie.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
left = 630
num = 1
for i in range(len(year)):
    
    # 2. 스크롤
    pyautogui.scroll(-150)
    time.sleep(2)
    pyautogui.moveTo(left,380)
    time.sleep(1)
    pyautogui.click()
    pyautogui.scroll(-150)
    time.sleep(3)
    
    left -= 50
    
    #------------------------------------------------------------------
    print("[ ",year[i],"년 영화 순위 ]")
    print("-"*40)
    
    # 3. 웹스크래핑
    soup  = BeautifulSoup(browser.page_source,"lxml")

    movie_ul = soup.find("ul",{"class":"c-list-basic ty_flow35"})
    for li in movie_ul:
        rank = int(li.find("span",{"class":"badge-basic"}).text)
        print("순위 : ", rank)
        
        img = li.find("a",{"class":"thumb_bf"}).find("img")['src']
        print("이미지 링크 : [",img,"]")
        try :
            urllib.request.urlretrieve(img,str(num)+'.jpg')
            num += 1
        except:
            continue
        
        title = li.find("strong",{"class":"tit-g clamp-g"}).a.text
        print("영화 제목 : ",title)
        
        viewer = li.find("p",{"class":"conts-desc clamp-g"}).a.text
        print("관객수 : ",viewer)
        
        mdate = li.find("span",{"class":"conts-subdesc clamp-g"}).text.replace('.','')
        print("개봉날짜 : ",mdate)
        
        # DB저장
        sql = f"insert into daum_movie values(daum_seq.nextval, '{title}', '{img}', '{viewer}', to_date('{mdate}'))"
        cursor.execute(sql)
        
        print("-"*40)

conn.commit()  # 커밋
cursor.close()
conn.close()
