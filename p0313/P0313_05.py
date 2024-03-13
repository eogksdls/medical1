import random

# * 모든 것.
from random import * # random 모듈명을 안붙여도 됨

# 0.00000 - 0.999999 랜덤으로 float 결과값 리턴
print(random())  # random은 0-1사이의 난수(실수) 생성

# 10-20사이의 랜덤 소수점의 결과값을 리턴
print(uniform(10,20))

# 1-2까지의 랜덤숫자 리턴
print(randrange(1,3))

# 리스트 내에 랜덤 선택
print(choice([1,2,3,4,5]))
# 리스트 내에 랜덤으로 k개를 선택, k가 리스트 개수보다 많으면 에러
print(sample([1,2,3,4,5],k=2))

# 리스트의 요소를 랜덤으로 섞음
a_list = [1,2,3,4,5]
shuffle(a_list) # 출력을 하는 것이 아니라, a_list 결과를 저장시켜줌
print(a_list)

# 1-10 범위(10포함) 내 랜덤 int를 선택
print(randint(1,10))





# import math

# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))