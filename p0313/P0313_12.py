# 람다식 함수
def sum(num1,num2):  # 함수는 변수로 사용할 수 없다.
    return num1+num2

print(sum(10,20))


def sum(num1,num2):
    return num1+num2
a = lambda num1,num2:num1+num2  # 람다식 함수는 변수지정 가능
print(a(10,20))