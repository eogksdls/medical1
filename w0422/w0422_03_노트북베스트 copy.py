import requests
from bs4 import BeautifulSoup

url = "https://browse.auction.co.kr/list?category=22160000&k=31&p=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

#데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")

#with open("auction.html","w",encoding="utf-8") as f:
#    f.write(soup.prettify())
  
laptop_lis = soup.find_all("div",{"class":"component component--item_card type--general"})
# print(laptop_div)
#print(laptop01)
#------------------------------------------------------------------------------
for i, li in enumerate(laptop_lis[0:15]):
    print("[ ",i+1,"번째 상품 ]")
    laptop = li.find("div",{"class":"section--itemcard"})
    laptop_info = laptop.find("div",{"class":"section--itemcard_info"})
    #print(laptop_info)
    print("브랜드 명 : ",laptop_info.find("span",{"class":"text--brand"}).text)
    print("상품명 : ",laptop_info.find("span",{"class":"text--title"}).text)

    laptop_price = laptop_info.find("div",{"class":"area--itemcard_price"})
    #price = int(laptop_price.find("span",{"class":"box__price-seller"}).strong.text).replace(",","")
    price = laptop_price.find("span",{"class":"box__price-seller"}).strong.text
    print("가격 : ",price,"원")
    
    list_score = laptop_info.find("ul",{"class":"list--score"})
    lis = list_score.find_all("li")
    
    print("li 개수 : ",len(lis))
    if len(lis)==0:
        print("후기평점, 구매건수 : 없음")
    elif len(lis) == 1:
        buy = list_score.find("li",{"class":"item buycnt"}).span.text[3:]
        print("구매 : ",buy,"건")
    else:
        score = float(list_score.find("li",{"class":"item awards"}).span.text[5:-1])
        print("후기 평점 : ",score)
        buy = list_score.find("li",{"class":"item buycnt"}).span.text[3:]
        print("구매 : ",buy,"건")
    
    print("-"*40)