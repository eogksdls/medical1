import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr/n/best?viewType=G&groupCode=G11&subGroupCode=S047&largeCategoryCode=100000013&mediumCategoryCode=200000683"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

#데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")

#with open("auction.html","w",encoding="utf-8") as f:
#    f.write(soup.prettify())
    
room_div = soup.find("div",{"class":"best-list"})
#print(room_div)
li01 = room_div.find("li",{"class":"first"})
print(li01)

print("순위 : ",li01.p.text)
print("장소 : ",li01.find("a",{"class":"itemname"}).text)
print("가격 : ", li01.find("div",{"class":"s-price"}).strong.span.text)

#--------------------------------------------------------------------------
lis = room_div.find_all("li")
for li in lis[0:5]:
    print("순위 : ",li.p.text)
    print("장소 : ",li.find("a",{"class":"itemname"}).text)
    print("가격 : ",li.find("div",{"class":"s-price"}).strong.span.text)
    print("-"*40)
