# 함수 선언
def plus(n1,n2):  # def 이름(매개변수1, 매개변수2)
    result = 0
    result = n1 + n2
    print("결과값: ",result)

print("프로그램을 실행합니다.")
plus(1,2)  # 매개변수가 2개면 무조건 2개가 들어와야함. 아니면 에러
plus(10,20)  # 함수호출 : 함수이름(매개변수를 맞춰주면 됨.)
plus(50,100)

# n1,n2 = 1,2
# result = 0
# result = n1 + n2
# print("결과값: ",result)   # 함수 호출을 사용하지 않을 시, 코드 길이가 길어짐

# n1,n2 = 10,20
# result = 0
# result = n1 + n2
# print("결과값: ",result)