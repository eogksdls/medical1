
def calc(input1, input2):
    result1 = input1 + input2
    result2 = input1 - input2
    result3 = input1 * input2
    result4 = input1 / input2
        
    return result1,result2,result3,result4

# 함수의 return을 사용해서 입력된 두 수의 사칙연산 결과값을 출력하세요.
# 20, 10
# 결과값:3,10,200,2
input1 = int(input("1번 째 숫자를 입력하세요:  "))
input2 = int(input("2번 째 숫자를 입력하세요:  "))
result1, result2, result3, result4 = calc(input1,input2)
print(f"{input1}와 {input2}의 더하기 값: ",result1)
print(f"{input1}와 {input2}의 빼기 값: ",result2)
print(f"{input1}와 {input2}의 곱하기 값: ",result3)
print(f"{input1}와 {input2}의 나누기 값: ",result4)
