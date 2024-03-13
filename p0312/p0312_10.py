import random

# 카드 종류: SPADE, DIAMOND, HEART, CLOVER 4종류
# 카드 숫자: A,2,3,4,5,6,7,8,9,10,J,Q,K 13장
# 카드 총 수: 52장

def card_creat(card_list,shape_list,num_list):
    print("[ 카드 생성 ]")
    cnt = 0
    for i in shape_list:
        for j in range(13):
            card_list[cnt] = [i,num_list[j]]
            cnt += 1
    print(card_list)
    print('-'*40)
            
def card_shuffle(card_list):
    print("[ 카드 섞기 ]")
    random.shuffle(card_list)
    print(card_list)
    print('-'*40)

def card_share(card_list,share_list):
    print("[ 카드 5장 나눠주기]")
    for i in range(5):
        share_list[i] = card_list[i]
    print(">> 카드 5장: ")
    print(share_list)
    print('-'*40)

def card_check(share_list):
    print("[ 카드 5장 확인하기]")
    print("내가 받은 카드 5장: ")
    print(share_list)
    print('-'*40)

#-------------------------------------------------------------
card_list = [[0]*2 for i in range(52)]
shape_list = ['SPADE', 'DIAMOND', 'HEART', 'CLOVER']
num_list = [0]*13
for i in range(1,14):
    num_list[i-1] = i
num_list[0] = "A"
num_list[10] = "J"
num_list[11] = "Q"
num_list[12] = "K"
share_list = [0]*5
#---------------------------------------------------------------

while True:
    print("\t[ 카드 프로그램 ]")
    print("1. 카드 생성")
    print("2. 카드 섞기")
    print("3. 카드 5장 나눠주기")
    print("4. 카드 5장 확인하기")
    print('-'*40)
    choice = int(input("원하는 번호를 입력하세요:  "))
    print('-'*40)

    if choice == 1:
        card_creat(card_list,shape_list,num_list)
        
    elif choice == 2:
        card_shuffle(card_list)
        
    elif choice == 3:
        card_share(card_list,share_list)
        
    elif choice == 4:
        card_check(share_list)
        
    else:
        print("프로그램을 종료합니다.")
        print("*"*40)
        break