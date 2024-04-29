import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://flight.naver.com/"

# 브라우저 열기
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)
time.sleep(3)

# 스크롤
elem7 = browser.find_element(By.CLASS_NAME,'main_searchbox__3vrV3')
browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth',block:'start'});",elem7)
time.sleep(2)
# 박스클릭
elem7 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]')
elem7.click()
time.sleep(1)

start = 0
start += 200
# jquery injection
jquery = """
    javascript:(function(){
        // jquery script tag
        script = document.createElement('script');
        script.src = "https://code.jquery.com/jquery-3.7.1.min.js"
        document.body.appendChild(script);
    });

"""

browser.execute_script(jquery)
for _ in range(2):
    time.sleep(1)
    browser.execute_script(f'$(".awesome-calendar").animate({{scrollTop: {start}}},500);')
    start += 200

time.sleep(3)
browser.quit()


# # 날짜지정하기 위한 스크롤
# inner_box = browser.find_element(By.CLASS_NAME,'sc-jqUVSM ilolms awesome-calendar')
# inner_box.click()
# time.sleep(1)
# inner_box.send_keys(Keys.ARROW_DOWN)
# # 날짜지정
# elem7 = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[11]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[3]/td[3]/button')
# elem7.click()
# time.sleep(2)


# # 원본창[0], 새창[1], 그 다음 새창[2]
# # browser.switch_to.window(browser.window_handles[1])
