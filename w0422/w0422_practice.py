import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr/n/list?category=200000734&gate_id=54D23BA5-A58E-4768-946D-E1D90CA50617"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# 데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")

product_div = soup.find("div",{"class":"section__module-wrap"})
product_list = product_div.find_all("div",{"class":"box__component box__component-itemcard box__component-itemcard--general"})

for i, item in enumerate(product_list[0:10]):
    print("[ ",i+1,"번 째 상품 ]")
    product_info = item.find("div",{"class":"box__information"})
    
    title_div = product_info.find("div",{"class":"box__item-title"}).a
    title = title_div.find("span",{"class":"text__item"}).text
    print("상품명 : ",title)
    
    price_div = product_info.find("div",{"class":"box__item-price"})
    price = product_div.find("strong",{"class":"text text__value"}).text
    print("가격 : ",)
    print("-"*40)
