# 두 수를 입력받아, 두 수 사이의 합계를 구하시오.
# 파이썬 언어는 인터프린터 언어: 코드 한 줄씩 기계어로 변환 후 실행
# 자바는 컴파일러 언어: 전체 소스 코드를 한 번에 기계어로 변환 후에 실행파일을 만든다.
def cal(s_list):
    # sum = 0   # 지역변수
    # 더하기
    for i in range(s_list[0],s_list[1]+1):
        s_list[2] += i
    # 빼기
        s_list[3] -= i
    # 곱하기
        s_list[4] *= i

# 두수 입력
sum = 0
minus = 0
multi = 1
num1 = int(input("1번째 숫자를 입력하세요:  "))
num2 = int(input("2번째 숫자를 입력하세요:  "))
s_list = [num1,num2,sum,minus,multi]
# 함수 호출
cal(s_list)   # 전역변수

print("합계: {}".format(s_list[2]))
print("빼기: {}".format(s_list[3]))
print("곱하기: {}".format(s_list[4]))
