import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

def main():
    # selenium으로 정보 가져오기
    browser = webdriver.Chrome()
    browser.get("https://comic.naver.com/bestChallenge")
    time.sleep(3)

    soup = BeautifulSoup(browser.page_source,"lxml")
    with open("webtoons2.html","w",encoding="utf-8") as f:
        f.write(soup.prettify())
        bestweb_ul = soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
        # print(bestweb_ul)

        lis = bestweb_ul.find_all("li")

        # print(len(lis))

        for li in lis:
            #1. 순위
            ranking = li.find("div",{"class":"AsideList__raking_area--aQX3C"}).strong.text
            print("순위 : ",ranking)
            
            #2. 제목
            info_wrap = li.find("div",{"class":"AsideList__info_area--PVPwn"})
            title = info_wrap.find("span",{"class":"ContentTitle__title--e3qXt"}).span.text
            print("제목 : ",title)
            
            # 3. 작가명
            writer = info_wrap.find("a",{"class":"ContentAuthor__author--CTAAP"}).text
            print("작가명 : ",writer)
            
            #4. 사진
            img_url = li.find("img")['src']
            print("이미지 링크 : ", img_url)
            img_poster = requests.get(img_url)
            with open('{}.jpeg'.format(title),'wb') as f:
                f.write(img_poster.content)
            print("-"*40)
    #print("완료")
main()
#------------------------------------------------------------------------------

    