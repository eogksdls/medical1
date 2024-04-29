import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://flight.naver.com/"

# 1. 네이버 페이지 이동
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

# #-----------------------------------------------------------------
# # 2. 검색창 : 네이버 항공권 입력
# time.sleep(3)
# elem = browser.find_element(By.XPATH,'//*[@id="query"]')
# elem.send_keys("네이버 항공권")
# time.sleep(2)

# #-----------------------------------------------------------------
# # 3. 검색 엔터키 입력
# elem.send_keys(Keys.ENTER) 
# time.sleep(3)

# #-----------------------------------------------------------------
# # 4. 네이버항공권 클릭 -> 페이지 이동
# elem2 = browser.find_element(By.CLASS_NAME,'direct_link')
# elem2.click()
# time.sleep(4)
# browser.switch_to.window(browser.window_handles[1])  # 새창으로 이동

#-----------------------------------------------------------------
# 5. 출발지역 선택 : 김포
elem3 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[1]')
elem3.click()
time.sleep(1)
elem3 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[1]/div/input')
elem3.send_keys("김포")
time.sleep(2)
elem4 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[2]/section/div/a')
elem4.click()
time.sleep(3)

#-----------------------------------------------------------------
# 6. 도착지역 선택 : 제주
elem5 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[2]')
elem5.click()
time.sleep(1)
elem5 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[1]/div/input')
elem5.send_keys("제주")
time.sleep(2)
elem6 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[2]/section/div/a')
elem6.click()
time.sleep(3)

#-----------------------------------------------------------------
# 7.가는날 지정 : 5월 14일
# 스크롤
elem7 = browser.find_element(By.CLASS_NAME,'main_searchbox__3vrV3')
browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth',block:'start'});",elem7)
time.sleep(2)
# 박스클릭
elem7 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]')
elem7.click()
time.sleep(1)

# start = 0
# start += 200
# # jquery injection
# jquery = """
#     javascript:(function(){
#         // jquery script tag
#         script = document.createElement('script');
#         script.src = "https://code.jquery.com/jquery-3.7.1.min.js"
#         document.body.appendChild(script);
#     });

# """

# browser.execute_script(jquery)
# for _ in range(2):
#     time.sleep(1)
#     browser.execute_script(f'$(".awesome-calendar").animate({{scrollTop: {start}}},500);')
#     start += 200

# time.sleep(3)

# 날짜지정 : 5월 14일
# 여러개의 14일 중 5월 14일만 선택
elem7 = browser.find_elements(By.XPATH,'//b[text()="14"]')
print("14일 개수",len(elem7))
elem7[1].click()
time.sleep(2)

#-----------------------------------------------------------------
# 8. 오는날 지정 : 5월 15일
# 여러개의 15일 중 5월 15일만 선택
elem8 = browser.find_elements(By.XPATH,'//b[text()="15"]')
print("15일 개수 : ",len(elem8))
elem8[1].click()
time.sleep(3)

#-----------------------------------------------------------------
# 9. 성인 2명 선택
elem9 = browser.find_element(By.XPATH,'//button[contains(text(),"성인")]')
elem9.click()
time.sleep(2)
elem10 = browser.find_element(By.XPATH,'//button[@class="searchBox_outer__9n6IB"]')
time.sleep(2)
elem10.click()
elem9.click()
time.sleep(2)

#-----------------------------------------------------------------
# 10. 항공권 검색
elem11 = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
elem11.click()

#-----------------------------------------------------------------
# 11. 검색하는 동안 대기
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 최대 30초까지 대기
elem12 = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))
print(elem12[0].text)
#-----------------------------------------------------------------------------------------------------------
# 12. 검색된 항공권 스크롤해서 하단 이동 반복
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이: ",prev_height)
time.sleep(3)
while True:
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
    print("현재 높이 : ",curr_height)

#-----------------------------------------------------------------
# 13. 13만원 이하인 항공권 정보저장
soup = BeautifulSoup(browser.page_source,"lxml")
# with open("popular.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
time.sleep(5)
ticketList = soup.find_all("div",'domestic_Flight__sK0eA')
print(len(ticketList))
for i,ticket in enumerate(ticketList):
    price_div = ticket.find("div","domestic_prices__3N88F")
    price = price_div.find("b","domestic_price__1qAgw")
    price_int = int(price.i.text.strip().replace(',',''))
    # 10만원권 이하의 항공권만 출력-------------------------------------
    if price_int < 100000: 
        print("[ 10만원 이하의 항공권입니다. ]")
        plane_div = ticket.find("div","domestic_schedule__1Whiq")
        airline = plane_div.find("span","airline_text__28jl7").b.text
        print("[",i,"]")
        print("항공사 : ",airline)
        #---------------------------------------------------------------
        departure = plane_div.find("span","route_airport__3VT7M")
        print("출발 시간 : ",departure.b.text)
        #----------------------------------------------------------------
        arrival = departure.find_next_sibling("span")
        print("도착 시간 : ",arrival.b.text)
        #----------------------------------------------------------------
        during = arrival.find_next_sibling("i")
        print("소요 시간 : ",during.text)
        #-----------------------------------------------------------------
        print("티켓 유형 : ", price.span.text)
        print("가격 : ",price.i.text,"원")
        print("-"*40)

#-----------------------------------------------------------------
# 웹드라이버 종료    
browser.quit()