import requests
from bs4 import BeautifulSoup
# ---------------------------------------------------------------------------------------------------
sum_all = 0
for y in range(2021,2024):
    url = f"https://search.daum.net/search?w=tot&q={y}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()   # 오류가 뜨면 코드 중지

    soup = BeautifulSoup(res.text,"lxml")

    movie_list = soup.find("ol",{"class":"movie_list"})

    # m_list는 30개
    m_list = movie_list.find_all("li")
    # print(type(m_list))  # 'bs4.element.ResultSet' 여러개로 묶여있다.
    sum = 0
    for i, m in enumerate(m_list):
        if i == 5: break    # 영화 이미지가 5개만 나오도록
        print("-"*50)
        print(f"[번호 {i+1}]")
        print("제목 : ",m.find("div",{"class":"info_tit"}).a.text)
        rate = float(m.find("em",{"class":"rate"}).text)
        print("평점 : ",rate)
        sum += rate
        
        img_screen = m.find("img")["data-original-src"]
        print(img_screen)
        # 파일로 저장하기
        # with open(f"movie_{y}_{i+1}.jpg","wb") as f:
        #     re_img = requests.get(img_screen)   # url링크를 다시 읽어와야 함.
        #     f.write(re_img.content)   # 파일이름의 내용을 저장
    print('-'*50)
    print(f"{y}년 Top5 평점 합계 : ",sum)
    print(f"{y}년 Top5 평점 평균 : ","{:.1f}".format(sum/5))
    sum_all += sum
    print('*'*50)

# ------------------------------------------------------------------------------
print("개수 : ",len(m_list))
print("2021~2023년 Top5 총 평점 합계: ",sum_all)
print("2021~2023년 Top5 총 평점 평균: ","{:.1f}".format(sum_all/15))
# print(movie_list)
print("종료")
print("파일이 저장되었습니다.")