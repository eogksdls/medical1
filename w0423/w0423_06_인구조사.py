#https://jumin.mois.go.kr/ageStatMonth.do

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
url = "https://jumin.mois.go.kr/ageStatMonth.do"
# 브라우저 페이지 열기
browser.get(url)
time.sleep(5)

soup = BeautifulSoup(browser.page_source,"lxml")
with open("popular.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())
    print("[ 총 인구 통계 ]")
    
    table_div = soup.find("div","section3")  # section3 은 단일
    # print(table_div)
    table_section = table_div.find("div","tab_section current_table title_table_div")
    table = table_section.find("table")
    
    td_list = table.find_all("td","td_admin th1")
    #------------------------------------------------------------------------
    # print(td_list)
    # 0,000,000 형식의 문자열에서 콤마 제거 후 int(정수형)으로 변환
    # seoul = int((td_list[1].find_next_sibling("td").text).replace(',',''))
    # # 다시 천단위 콤마 찍어주기
    # print("서울특별시 : ",format(seoul,','),"명")
    # busan = int((td_list[2].find_next_sibling("td").text).replace(',',''))
    # print("부산광역시 : ",format(busan,','),"명")
    # daegu = int((td_list[3].find_next_sibling("td").text).replace(',',''))
    # print("대구광역시 : ",format(daegu,','),"명")
    # incheon = int((td_list[4].find_next_sibling("td").text).replace(',',''))
    # print("인천광역시 : ",format(incheon,','),"명")
    # print("-"*40)
    # total = seoul+busan+daegu+incheon
    # print("통합 인구수 : ",format(total,','),"명")
    #-------------------------------------------------------------------------
    print("-"*40)
    total = 0
    for i in range(1,len(td_list)):
        num = int((td_list[i].find_next_sibling("td").text).replace(',',''))
        print(td_list[i].text,":",format(num,','),"명")
        total += num
    print("-"*40)
    print("전국 : ",format(total,','),"명")
    print("-"*40)
    
    seoul = int((td_list[1].find_next_sibling("td").text).replace(',',''))
    incheon = int((td_list[4].find_next_sibling("td").text).replace(',',''))
    gyeonggi = int((td_list[8].find_next_sibling("td").text).replace(',',''))
    print("수도권 : ",format(seoul+incheon+gyeonggi,','),"명")
    print("-"*40)