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

    if laptop_info.find("ul",{"class":"list--score"}).text =="":
        print("구매 이력이 없습니다.")
    else:
        laptop_score = laptop_info.find("ul",{"class":"list--score"})
        try:
            score = float(laptop_score.find("li",{"class":"item awards"}).span.text[5:-1])
            if score > 4.5:
                print("후기 평점 :",score)
            else:
                print("후기 평점: 미달")
            
            review = laptop_score.find("li",{"class":"item reviewcnt"}).span
            print("후기 : ",review.text[3:],"건")
        except:
            print("평점이 존재하지 않습니다.")
                
        buy = laptop_score.find("li",{"class":"item buycnt"}).span
        print("구매 : ",buy.text[3:],"건")
    print("-"*50)
