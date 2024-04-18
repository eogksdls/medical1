import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/bestChallenge"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

with open("webtoon.html","w",encoding="utf-8") as f:
    f.write(soup.prettify()) # prettify는 html코드를 눈에 보기 이쁘게 정리