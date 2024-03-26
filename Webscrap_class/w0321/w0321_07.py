import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# print(soup)
s_all = soup.find("div",{"class":"box_type_l"})
tr_list = s_all.find_all("tr")
# 타입 - list    
# print(len(tr_list)) : 50개
samsung = tr_list[2]   # 50개의 tr중 3번째가 삼성전자
td_list = samsung.find_all("td")  # tr 내에 td가 존재함
print("순위 : ",td_list[0].text)
print("종목명 : ",td_list[1].find("a").text)
print("검색비율 : ",td_list[2].text)
print("현재가 : ",td_list[3].text)

# print(tr_list[2])  # 삼성전자

# with open("stock.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
# print(soup.prettify())
