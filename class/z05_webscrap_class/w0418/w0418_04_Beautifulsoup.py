import requests
from bs4 import BeautifulSoup # text를 html로 변경해주기 위함
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml") # text를 html으로 파싱
#print(type(soup.prettify())) #html소스를 정렬해서 출력해줌.

# 정보를 가져오려면, soup.태그명
print("<title> : ",soup.title) #태그를 입력 - > 태그정보를 가져옴
print("<title> text : ",soup.title.get_text()) #태그의 글자만 가져옴
print("<title> text : ",soup.title.text) #태그의 글자만 가져옴
print("<a> 태그 : ",soup.a) # a태그가 많을 시 가장 첫 번째것만 가져온다
print("<a> 글자 : ", soup.a.text)
print("<a> 속성전체 : ",soup.a.attrs) #a 태그의 '속성':'속성값' 모두 가져오기

print("<a>[속성] : ",soup.a["href"]) # 태그의 href 속성값 가져옴(1개의 특정 속성값만을 알고 싶을 때)

