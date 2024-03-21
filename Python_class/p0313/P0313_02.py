# 퀴즈 .2
def cal(num1,num2):
    r_list = [0]*6
    r_list[0] = num1
    r_list[1] = num2
    r_list[2] = num1 + num2
    r_list[3] = num1 - num2
    r_list[4] = num1 * num2
    r_list[5] = float("{:.2f}".format(num1 / num2))
    return r_list
#
save_list = []

# 두 수를 입력받아 값을 리턴 받은 다음, 출력하세요.
while True:
    print(f">> {len(save_list)+1}번째 숫자 입력")
    num1 = int(input("1번째 숫자를 입력하세요(0.종료):  "))
    if num1 == 0 :
        break
    num2 = int(input("2번째 숫자를 입력하세요:  "))
    
    r_list= cal(num1,num2)
    # list일 경우 *list = list[0],list[1],list[2],list[3]
    ## save_list에 r_list를 저장
    print(f"{num1}, {num2} 결과 값: {r_list[2:]}")
    save_list.append(r_list)
    print('-'*55)

# 현재까지 입력한 숫자와 결과값을 모두 출력해보세요
print("[ 현재까지 입력한 숫자, 결과값 ]")
for i, save in enumerate(save_list):
    print("{}, {} 결과 값: {}".format(save_list[i][0],save_list[i][1],save_list[i][2:]))
# 10,20 결과값 : 30, -10, 200, 0.5