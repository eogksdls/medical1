import oracledb
import requests
import time
import random
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

url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(2)
    
# #파일 불러오기
# with open("melon.html","r",encoding="utf-8") as f:
#     soup = BeautifulSoup(f,"lxml")

soup = BeautifulSoup(browser.page_source,'lxml')
calendar = soup.find("div","calendar_prid mt12")
ymd = calendar.find("span","yyyymmdd").span
hhmm = calendar.find("span","hhmm").span
print("[", ymd.text,hhmm.text, "멜론 차트 ]")
print("-"*50)

tb_list = soup.find("div",{"id":"tb_list"})
tbody = tb_list.find("tbody")
music_list1 = tbody.find_all("tr","lst50")
music_list2 = tbody.find_all("tr","lst100")
all = music_list1 + music_list2
# print("차트 개수 : ",len(all))  # 100개

# 1~100위 차트
for music in all[:83]:
    rank = music.find("span","rank").text
    print("순위 : ",rank,"위")
    #------------------------------------------------------------
    # 순위 변동
    if music.find("span","rank_wrap").span.span.text == "단계 상승":
        rank_change = music.find("span","bullet_icons rank_up")
        v_rank = '+'+music.find("span","up").text
        print("순위 변동 : ",rank_change.span.text)
        print("변동 폭 : ",v_rank)
    elif music.find("span","rank_wrap").span.span.text == "단계 하락":
        rank_change = music.find("span","bullet_icons rank_down")
        v_rank = '-'+music.find("span","down").text
        print("순위 변동 : ",rank_change.span.text)
        print("변동 폭 : ",v_rank)
    elif music.find("span","rank_wrap").span.span.text == "순위 진입":
        rank_change = music.find("span","bullet_icons rank_new")
        v_rank = '0'
        print("순위 변동 : ",rank_change.span.text)
        print("변동 폭 : ",v_rank)
    else:
        rank_change = music.find("span","bullet_icons rank_static")
        v_rank = '0'
        print("순위 변동 : ",rank_change.span.text)
        print("변동 폭 : ", v_rank)
    #-----------------------------------------------------------    
    image = music.find("img")['src']
    print("앨범 링크 : [",image,"]")
    
    song_info = music.find("div","wrap_song_info")
    title = song_info.find("div","ellipsis rank01").span.text.strip()
    print("곡 명 : ",title)
    singer = song_info.find("div","ellipsis rank02").a.text
    print("가수명 : ",singer)
    
    like = int(music.find("span","cnt").text[4:].replace('"','').replace(',',''))
    print("좋아요 수 : ",format(like,','),"개")
    
    print("-"*50)
    
    # DB저장
    sql = f"insert into melon values(melon_seq.nextval,{rank},'{v_rank}','{image}','{title}','{singer}',{like})"
    cursor.execute(sql)
    
conn.commit()
cursor.close()
conn.close()