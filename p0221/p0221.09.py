# 두 수를 입력 받아서 사칙연산을 출력해보세요
# 예: 30, 6을 입력받아서
# 출력 :
# 30 + 6 = 36
# 30 - 6 = 24
# 30 * 6 = 180
# 30 / 6 = 5.0
n1 = int(input("첫 번째 숫자를 입력하세요 >> "))  # int로 형변환 (문자열>숫자로!!)
n2 = int(input("두 번째 숫자를 입력하세요 >> "))
print(n1,'+',n2,'=',n1+n2)
print(n1,'-',n2,'=',n1-n2)
print(n1,'*',n2,'=',n1*n2)
print(n1,'/',n2,'=',n1/n2)

# 또는
a = input("첫 번째 값을 입력하세요 >> ")
b = input("두 번째 값을 입력하세요 >> ")
print("두 수의 합:", int(a)+int(b))
print("두 수의 차:", int(a)-int(b))
print("두 수의 곱:", int(a)*int(b))
print("두 수의 나눗셈:", int(a)/int(b))