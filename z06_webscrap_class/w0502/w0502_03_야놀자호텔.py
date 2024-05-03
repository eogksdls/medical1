import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.yanolja.com/?utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-327025203539&gad_source=1&gclid=CjwKCAjw88yxBhBWEiwA7cm6pY3AYuYxAUqEUvhpLlhqK_DmXd4Nzo5sP99ZdbN9nwV1-Yai-QV8SBoCejAQAvD_BwE"

browser = webdriver.Chrome()
browser.maximize_window()

# 1. 야놀자 홈페이지 이동
browser.get(url)
time.sleep(3)

# 2. 검색창에 호텔 입력
elem1 = browser.find_element(By.XPATH,'//*[@id="__next"]/section/header/section/a[2]/div/div')
elem1.click()
time.sleep(2)
elem1 = browser.find_element(By.XPATH,'//*[@class="SearchInput_input__342U2"]')
elem1.send_keys("호텔")
time.sleep(2)

# 3. 날짜 선택
elem2 = browser.find_element(By.XPATH,'//button[@class="NavFilterButton_container__20Hr2 NavFilterButton_collapse__3JGvV SearchInput_calendarButton__3sNMZ"]')
elem2.click()
time.sleep(2)
# 4. 6월 5일 ~ 6월 6일 클릭 
elem3 = browser.find_elements(By.XPATH,'//table[@class="CalendarMonth_table CalendarMonth_table_1"]/tbody/tr[2]/td[4]')
elem3[1].click()
time.sleep(1)
elem3 = browser.find_elements(By.XPATH,'//table[@class="CalendarMonth_table CalendarMonth_table_1"]/tbody/tr[2]/td[5]')
elem3[1].click()
time.sleep(2)
# 5. 확인 버튼
elem4 = browser.find_element(By.XPATH,'//button[text()="확인"]')
elem4.click()
time.sleep(1)
# 6. 검색창 클릭 -> enter 키 입력
elem1 = browser.find_element(By.XPATH,'//*[@class="SearchInput_input__342U2"]')
elem1.click()
elem1.send_keys(Keys.ENTER)

# 7. 검색 진행
time.sleep(3)

# 8. 스크롤 이동 반복
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 : ",prev_height)
time.sleep(2)
for i in range(20):  # 정보량이 많아서 20번만 스크롤
    # 0에서부터 현재 높이만큼 밑으로 스크롤하겠다
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # 페이지 로딩 대기
    time.sleep(2)
    # 현재 높이 다시 계산
    curr_height = browser.execute_script("return document.body.scrollHeight")
    # 이전높이와 현재높이의 비교
    if prev_height == curr_height:
        break # 같으면 중단 하고 빠져나옴
    # 같지 않으면 스크롤을 다시 진행
    prev_height = curr_height
    # print("현재 높이 : ",curr_height)
    
# 9. 정보창이 띄워지면, 이미지, 제목, 평점, 평가수, 금액 저장하기
soup = BeautifulSoup(browser.page_source,"lxml")

# with open("yanolja.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
time.sleep(5)
print("[ 검색결과 ]")
print("*"*40)

placeList = soup.find_all("div","PlaceListItemText_container__fUIgA text-unit")

for place in placeList:
        # 호텔명
        placeContent = place.find("div","PlaceListItemText_area__3l67D")
        title = placeContent.find("div","PlaceListTitle_container__qe7XH").strong.text
        print("호텔명 : ",title)
        
        # 이미지
        img = place.find("div","PlaceListImage_container__t-mGF")['url']
        
        # 평점
        placeScore = placeContent.find("div","PlaceListScore_container__2-JXJ PlaceListItemText_score__1O-nW")
        rating = placeScore.find("span","PlaceListScore_rating__3Glxf").text.replace('"','')
        print("평점 : ",rating)
        # 후기 수
        review = placeScore.find("span","PlaceListScore_reviewInfo__3QSCU").text.replace('"','').strip()
        print("후기 수 : ",review.replace(")","").replace("(",""),"개")
        
        # 금액
        price = placeContent.find("div","PlacePriceInfoV2_bottomInfo__2h62q")
        if price.span.text == "예약마감":
            print("숙소 가격 : 예약마감")
        else:
            print("숙소 가격 : ",price.find("span","PlacePriceInfoV2_discountPriceContainer__1O-F6").text)
        print("-"*40)
        
        insert_data = '''
                    insert into yanolja values()
        '''
        
# yanolja 테이블(oracle)
# yno,img,title,grade, grade_num, price

