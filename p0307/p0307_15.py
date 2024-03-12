# 크기가 10인 리스트를 생성하는데, 7개는 0으로 3개는 1로 채우시오.

list = [0]*10
for i in range(3):
    list[i] = 1  # 수정 사용
print(list)

import random

# 크기가 100인 리스트 생성, 10개는 1로 채우시오
# 랜덤으로 섞어서 출력하시오.
a_list = [0]*100
for i in range(10):
    a_list[i] = 1

print(a_list) # 파괴형태
random.shuffle(a_list) 
print(a_list)

# [10*10] 2차원 배열을 생성하시오.
b_list = [[0]*10 for _ in range(10)] 
print(b_list)

b_lists =[]
b_list = []
for i, j in enumerate(a_list): # i가 a_list의 인덱스
    if (i+1)%10 == 0:
        b_list.append(j)
        b_lists.append(b_list)
        b_list = [] # 100번 계속 처음으로 초기화
    else:
        b_list.append(j)
print()
# print(b_lists)

# [10*10] 2차원의 배열
newLists = [["추첨"]*10 for _ in range(10)]

cnt = 0 # 당첨횟수
lotto = 0
while True:
    print('[ 10 * 10 좌표]')
    print('-'*70)
    # print(b_list)
    print("",0,1,2,3,4,5,6,7,8,9,sep="      ")
    print('-'*70)
    for i,b in enumerate(newLists):
        print(i, end="  ")
        for bb in b:
            print(bb, end='   ')
        print()
    print('-'*70)
    x = int(input("가로 좌표를 입력하세요:  "))
    y = int(input("세로 좌표를 입력하세요:  "))
    # b_lists - 값을 비교, newLists - 표시
    
    if b_lists[x][y] == 1:
        newLists[x][y] = "당첨"
        print("선택하신 좌표는 [당첨] 입니다.")
        print('-'*70)
        cnt += 1
        lotto += 1

    else:
        newLists[x][y] = "[꽝]"
        print("선택하신 좌표는 [꽝] 입니다.")
        print('-'*70)
        cnt += 1
    if cnt == 10:
        print("뽑기 기회를 모두 사용하셨습니다.")
        print("당첨된 갯수 : {}개".format(lotto))
        print('프로그램이 종료됩니다.')
        print('*'*70)
        break