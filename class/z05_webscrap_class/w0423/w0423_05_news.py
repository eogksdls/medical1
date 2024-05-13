import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# selenium은 자동화 프로그램

browser = webdriver.Chrome()
url = "https://news.naver.com/"
# 브라우저 페이지 열기
browser.get(url)
time.sleep(3)

# 네이버 뉴스화면에서 랭킹 버튼 클릭
elem = browser.find_element(By.XPATH,'/html/body/section/header/div[2]/div/div/div/div/div/ul/li[8]/a')
elem.click()
time.sleep(3)
soup = BeautifulSoup(browser.page_source, "lxml")
# print(soup.prettify())
with open("news.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())
    print("언론사별 랭킹뉴스")
    officeCard = soup.find("div","_officeCard _officeCard0")
    rankingNews_box = officeCard.find("div","rankingnews_box")
    news_ul = rankingNews_box.find("ul","rankingnews_list")
    # print(news_ul)
    lis = news_ul.find_all("li")
    for li in lis:
        # 1. 순위
        ranking = li.find("em").text
        print("순위 : ", ranking)
        # 2. 제목
        title = li.find("div","list_content").a.text
        print("제목 : ", title)
        # 3. 사진
        img_url = li.find("img")['src']
        print("이미지 링크 : ",img_url)
        print("-"*40)
time.sleep(100)