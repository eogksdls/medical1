import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#-----------------기본 구문--------------------------------------------

#type_sam_td = soup.find("td",{"class":"no"}) # class="no"인 첫번째가 samsung
#sam_info = type_sam_td.next_siblings
#for s in sam_info:
#    print(s.text.strip())


t_table = soup.find("table",{"class":"type_5"})
trs = t_table.find_all("tr") # t_table내 tr를 모두 찾아줘
samsung_tds = trs[2].find_all("td") 
for td in samsung_tds:
    print(td.text.strip())