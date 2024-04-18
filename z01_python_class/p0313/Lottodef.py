import random

# 화면출력함수 -------------------------------------------
def screen():
    print("[ 로또번호 맞추기 프로그램 ]")
    print("1. 번호 생성 ")
    print("2. 번호 섞기 ")
    print("3. 나의 로또번호 입력 ")
    print("4. 번호 확인 ")
    print('-'*30)
    choice = int(input("원하는 번호를 입력하세요:  "))
    return choice

# 번호 생성 함수
def num_generate(lotto):
    print("[ 번호 생성 ]")
    for i in range(0,45):
        lotto[i] = i+1
    print(lotto)
    print('-'*30)
    
# 번호 섞기 함수
def shuffle(lotto):
    print("[ 번호 섞기 ]")
    random.shuffle(lotto)
    print(lotto)
    print('-'*30)

# 번호 입력 함수
def enter(my_lotto):
    print("[ 나의 로또번호 입력 ]")
    for i in range(6):
        my_num = int(input(f"{i+1}번째 로또 번호를 입력하세요:  "))
        my_lotto[i] = my_num
    print("내가 입력한 번호: ",my_lotto)
    print('-'*30)
    return my_num

# 번호 확인 함수
def check(lotto,lucky_lotto,my_lotto,win_num,win_amount):
    for i in range(6):
        lucky_lotto[i] = lotto[i]
    print("[ 번호 확인 ]")
    print(">> 로또번호 : ",lucky_lotto)
    print(">> 내가 입력한 번호: ", my_lotto)
    
    right = 0
    for i in lucky_lotto:
        if i in my_lotto:
            win_num.append(i)
            right += 1
            
    print("내가 맞춘 번호 개수: ", right)
    print("당첨된 번호: ", win_num)
    print('-'*30)
    # 당첨금액 출력
    print("당첨금액 : {:,} 원".format(win_amount[right]))
    print('-'*30)
    return right

# ---------------------------------------------------------