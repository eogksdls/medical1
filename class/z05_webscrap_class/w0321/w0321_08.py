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
tr_top10 = tr_list[2:15]   # 1위에서 10위까지  중간에 빈공백 있음
for tr in tr_top10:
    td_list = tr.find_all("td")   # tr 내에 td가 존재함
    if len(td_list) > 1:      # 빈공백에서의 td는 1개만 존재하기 때문에 조건식 걸어주기
        print("순위 : ",td_list[0].text)
        print("종목명 : ",td_list[1].find("a").text)
        print("검색비율 : ",td_list[2].text)
        print("현재가 : ",td_list[3].text)
        print("PER: ",td_list[10].text)
        print("ROE: ",td_list[11].text)
        print('-'*50)
    

# with open("stock.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
# print(soup.prettify())