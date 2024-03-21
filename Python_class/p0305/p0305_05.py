from random import *
# 1-25까지 숫자를 랜덤으로 섞은 가음
# 2차원 리스트에 넣어보세요

# [
#   [1,2,3,4,5],
# [6,7,8,9,10],
# [11,12,13,14,15],
# [16,17,18,19,20],
# [21,22,23,24,25],
# ]

# 랜덤으로 섞어서 출력하시오.
 
import random
num = random.randint(1,100)
print("정답: ",num)
# 숫자 맞추기 프로그램을 구현
# 1-10까지 숫자 랜덤으로 생성 후 숫자를 맞추는 프로그램입니다.
# 몇번째에 맞췄는지 출력하시오
save_num = []
cnt = 0
while True:
    in_num = int(input('1-100까지의 숫자를 입력하세요:  '))
    save_num.append(in_num)  # 저장
    if num > in_num:
        print('입력한 숫자보다 더 큽니다.')
    elif num < in_num:
        print('입력한 숫자보다 더 작습니다.')
    else:
        print('정답입니다.')
        print('{}회 만에 맞추셨습니다.'.format(cnt+1))
        break
    cnt += 1