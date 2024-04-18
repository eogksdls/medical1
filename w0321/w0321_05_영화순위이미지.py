import requests
from bs4 import BeautifulSoup
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%98%81%ED%99%94"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

movie_list = soup.find("ol",{"class":"movie_list"})

# m_list는 30개
m_list = movie_list.find_all("li")
# print(type(m_list))  # 'bs4.element.ResultSet' 여러개로 묶여있다.
for i, m in enumerate(m_list):
    if i == 5: break    # 영화 이미지가 5개만 나오도록
    print("-"*50)
    print(f"[번호 {i+1}]")
    img_screen = m.find("img")["data-original-src"]
    print(img_screen)
    # 파일로 저장하기
    with open(f"movie_{i+1}.jpg","wb") as f:
        re_img = requests.get(img_screen)   # url링크를 다시 읽어와야 함.
        f.write(re_img.content)   # 파일이름의 내용을 저장

print("개수 : ",len(m_list))

# print(movie_list)
print("종료")
print("파일이 저장되었습니다.")