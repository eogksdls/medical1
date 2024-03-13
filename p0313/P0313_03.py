# 랜덤으로 숫자 1개 생성
# 입력한 숫자보다 크면 작은수를 입력하세요
# 입력한 숫자보다 작으면 큰수를 입력하세요. 하고 멘트가 나오게
# 정답을 맞추면
# 총 입력한 횟수 : n회
# 현재까지 입력한 숫자 : 1,5,7,6,8,4,...
# 현재까지 입력했던 숫자를 모두 출력하시오

import random

ran_num = random.randint(1,100)
num_list = []

while True:
    print("[ 랜덤숫자 맞추기 게임 ]")
    print(f">> {len(num_list)+1}번째 도전 !!")
    my_num = int(input("1~100사이의 숫자 하나를 골라주세요:  "))
    print('-'*55)
    
    if my_num > ran_num:
        print("입력한 숫자보다 작은 수를 입력하세요.")
        print('-'*55)
        
    elif my_num < ran_num:
        print("입력한 숫자보다 큰 수를 입력하세요.")
        print('-'*55)
        
    else:
        print(">>~ 정답입니다. ~<<")
        print('-'*55)
        break
    num_list.append(my_num)

# -----종료 후-----
print("총 입력한 횟수: ",len(num_list)+1)
print("현재까지 입력한 숫자 : {}".format(num_list))
print('*'*55)