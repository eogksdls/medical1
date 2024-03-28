# 함수선언
def sum(num1,num2):
    return num1+num2
# 함수 선언 시, 함수 정의가 선언보다 먼저 나와야 에러가 발생하지 않는다.(코드를 위에서 아래로 읽기 때문)

num1 = int(input("숫자를 입력하세요:  "))
num2 = int(input("숫자를 입력하세요:  "))

print("두 수의 합:  ",sum(num1,num2))

