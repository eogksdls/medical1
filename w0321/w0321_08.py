import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
stock = soup.find("table",{"class":"type_5"})
# print(stock)
stock_list = stock.find_all("tr")
for i, s in enumerate(stock_list):
    if i == 1: break
    print("제목 : ",s.find("td",{"class":"tltle"}))
    print("검색비율: ",s.find("td",{"class":"number"}))
    print("현재가 : ",s.find("td",{"class":"number"}))
