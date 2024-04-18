# 키워드 매개변수: 키워드 매개변수는 제일 뒤에 와야함
def cal(num1,num2=10):  
    num1 = num1+10  # 지역변수 num1,num2
    num2 = num2+20
    result = num1 +num2
    return result  # 전역변수로 호출

# ------------------------------

num1 = 5   # 전역변수
num2 = 7

result = cal(num1,num2)  # 함수 호출

print("현재 숫자: ",num1,num2,result)