#  함수 선언 def 이름() 정의
#  함수값은 return
#  함수호출: 이름()
#  매개변수: 함수로 데이터를 전달하는 변수,
#  개수는 함수선언과 함수호출 시 항상 같아야한다.
#  가변매개변수선언 *values, 가변매개변수는 개수가 일치하지 않아도 된다.
#  리스트, 딕셔너리 매개변수는 주소값이 전달이 된다.

# 퀴즈 .1
#  함수를 사용하여 두 수를 입력받아, 더하기,빼기,곱하기,나누기 결과값을 출력하시오

def cal(c,num1,num2):
    # 1. 더하기
    if c == 1:
        result = num1+num2
    
    # 2. 빼기
    elif c == 2:
        if num1 < num2:
            num1,num2 = num2,num1
        result = num1-num2
    
    # 3. 곱하기
    elif c == 3:
        result = num1*num2
    
    # 4. 나누기
    elif c == 4:
        result = num1/num2
    
    return result

list = ["","더한","뺀","곱한","나눈"]

# 두 수를 입력받아 값을 리턴 받은 다음, 출력하세요.
while True:
    num1 = int(input("1번째 숫자를 입력하세요:  "))
    num2 = int(input("2번째 숫자를 입력하세요:  "))
    print("[ 1. 더하기(+), 2. 빼기(-), 3. 곱하기(*), 4. 나누기(/) ]")
    c = int(input("원하는 사칙연산을 입력하세요:  "))
    
    result= cal(c,num1,num2)
    print(f"{list[c]} 값: {result}")
    print('-'*55)
