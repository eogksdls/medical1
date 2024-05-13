
# 매개 변수로 리스트를 사용할 경우, return할 필요가 없음

# 함수 선언
def func1(a, a_list):
    a = 100  # 지역변수
    a_list[0] = 100 # 지역변수
    a_list = [100,200,300]
    return a # 지역변수를 전역변수로 바꾸어 선언

a = 10  # 전역변수
a_list = [1,2,3]
# 함수호출
a = func1(a,a_list)  # 2개 이상의 데이터를 저장하는 변수 - 주소값을 저장함

# 데이터 출력
print(a)
print(a_list)
