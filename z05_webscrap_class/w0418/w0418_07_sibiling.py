import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
type_tr = soup.find("tr",{"class":"type1"})

print("th : ",type_tr.th) #첫 번째 것만 출력
print("find_next_sibiling : ",type_tr.th.find_next_sibling("th")) #첫 번째 다음 형제 th출력
print("next1 : ",type_tr.th.next) #순위
print("next2 : ",type_tr.th.next.next) # 
print("next3 : ",type_tr.th.next.next.next) #<th>종목명</th>
# next는 다음 th가 아닌 바로 뒤에 있는 요소를 찾아준다 (</th>도 센다)