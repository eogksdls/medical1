import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

t_table = soup.find("table",{"class":"type_5"})
tr_list = t_table.find_all("tr")

# 종목 1위~10위 출력하기
tr_top10 = tr_list[2:15]  #1위에서 10위까지 중간에 빈공백이 존재함
for tr in tr_top10:
    td_list = tr.find_all("td")
    if len(td_list) > 1:  #공백에서는 td가 1개만 존재함 조건 불충족
        print("순위 : ",td_list[0].text)
        print("종목명 : ",td_list[1].find("a").text)
        print("검색비율 : ",td_list[2].text)
        print("현재가 : ",td_list[3].text)
        print("PER : ",td_list[10].text)
        print("ROE : ",td_list[11].text)
        print("-"*50)
