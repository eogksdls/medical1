# import Lottodef  -> 함수 호출 시: Lottodef.함수이름()
# from Lottodef import screen
# 바로 screen 함수호출 가능: screen() 이렇게 하면 된다.
# from Lottodef import * : 모든 함수 바로 사용가능
# from Lottodef import *   # *: 함수1,함수2,함수3,..
import Lottodef as lt      # 모듈 이름이 길 경우, 닉네임을 부여하여 짧게 사용 가능

lotto = [0]*45           # 모듈.함수이름()에서 '모듈.' 생략 가능
# while True:
#     lt.screen()
lt.num_generate(lotto)

import math as m
# ceil - 올림
print(m.ceil(12.2)) # 13
# floor - 버림
print(m.floor(12.2)) # 12
# 반올림
print(round(12.6))  #13 # 반올림은 너무 많이 써서 아예 따로 만듦

print(dir(m))