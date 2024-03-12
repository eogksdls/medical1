import random
# 1. 0으로 25개 1차원 리스트 만들기
list = [0]*25

# 2. 0으로 20개, 1로 5개 넣기
for i in range(5):
    list[i] = 1

# 3. 랜덤 섞기
random.shuffle(list)
print(list)

# 4. 5*5 2차원 리스트에 넣기
checkList = [[0]*5 for i in range(5)] # 5*5자료 만들기
print(checkList)
for i in range(5):
    for j in range(5):
        checkList[i][j] = list[5*i+j]

# 5. 추첨 5*5 2차원 배열
viewList = [["추첨"]*5 for _ in range(5)]


# 8. count 출력, 당첨 갯수
cnt = 0
lotto = 0 
while True:
 # 6. 출력
    print("\t[ 5*5 viewList 좌표 ]")
    print('-'*40)
    print('',0,1,2,3,4,sep="\t")
    print('-'*50)

    for i in range(5):
        print(i, end='\t')
        for j in range(5):
            print(viewList[i][j], end='\t')
        print()
    print('-'*50)

 # 7. 좌표입력 후 확인
    x = int(input("가로 좌표를 입력하세요:  "))
    y = int(input("세로 좌표를 입력하세요:  "))
    if checkList[x][y] == 1:
        viewList[x][y] = "당첨"
        lotto += 1
        cnt += 1
        if lotto == 5:
            print("축하합니다! 모두 당첨되었습니다.")
            print("프로그램을 종료합니다.")
            print("*"*50)
            break
    else:
        viewList[x][y] = "[꽝]"
        cnt += 1
 # 9. cnt 소진 후, 게임 재개 의사 묻기(한 번 결제 당, 5번의 기회)
    if cnt % 5 == 0:
        print('-'*50)
        print(">> 5번의 기회를 모두 사용하셨습니다. <<")
        coin = input("* 결제를 진행하시겠습니까?(예/아니오):  ")
        if coin == "예":
            pay = input("* 결제 방법을 선택해주세요.(카드/현금):  ")
            if pay == "카드":
                print("카드 결제를 선택하셨습니다.")
                print('-'*50)
                print(">> 추첨을 시작합니다.")
            elif pay == "현금":
                print("현금 결제를 선택하셨습니다.")
                print('-'*50)
                print(">> 추첨을 시작합니다.")
            continue
        else:
            print("다음 기회에 다시 만나요!")
            print('*'*50)
            break
    print("당첨 갯수: {} / 남아있는 당첨 갯수: {}".format(lotto,5-lotto))
    print("도전한 횟수: {}".format(cnt))
    
    