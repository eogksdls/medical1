def func(a,*b):
    print(a,b)

func(1,2,3,4) # 1 (2,3,4): 가변매개변수인 b는 튜플형태로 출력
# 튜플은 수정, 삭제가 안되고 읽기만 가능하다
# 튜플 형태 -> 리스트와 같다
a_tu = (1,2,3)
print(a_tu)
print(list(a_tu)) # 튜플을 리스트 형태로

# 맞교환 가능
[a,b]=[10,20]
(c,d)=(10,20)


# ---------------------------------------------------------
# a = 123
# print(a[0])  # 오류


# 자리배열은 문자열만 가능, 숫자는 불가능
b = "123"
print(b[0])

#-----------------------------------------------------------
# 리스트 인덱스
list_a = ["안","녕","하","세","요"]
print(list_a[0:-1])   # 처음부터 끝에서 첫번째까지만 출력
# ['안', '녕', '하', '세']

list_reversed = reversed(list_a)
print(list(list_reversed))    # 리스트 순서 뒤집기
# ['요', '세', '하', '녕', '안']
print("".join(list_a))   # 리스트에 있는 문자열들을 하나의 문자열로 합쳐서 출력

#-----------------------------------------------------------
# 딕셔너리
dic_a = {
    "키A" : 10,
    "키B" : 20,
}
print(dic_a["키A"])  # 10

# key = input("접근하고자 하는 key:  ")    # 키 존재여부 확인

# if key in dic_a:
#     print(dic_a[key])   # dic_a[key]는 value 값
# else:
#     print("존재하지 않은 키에 접근하고 있습니다.")
    
for key in dic_a:      
    print(dic_a[key])
for key in dic_a.keys():   # 딕셔너리 내 모든 key값 출력
    print(key)
for val in dic_a.values():  # 딕셔너리 내 모든 value값 출력
    print(val)
for k,v in dic_a.items():  # 딕셔너리 내 모든 key : value 값 출력
    print(k,v)

#---------------------------------------------------------------
# 역반복문
for i in range(1,10+1,2):
    print(i)    # 1부터 10까지 2씩 증가하여 출력
    
for i in range(10,0,-1):
    print(i)    # 10부터 1까지 역순 출력

#--------------------------------------------------------------
# 함수
# 가변 매개변수
def print_n_times(n, *values):
    # n번 반복
    for i in range(n):
        # values 는 리스트처럼 활용
        for val in values:
            print(val)
        print()
# 함수 호출
print_n_times(3,"안녕하세요","즐거운","파이썬 프로그래밍")

# 함수 호출 시 기본 매개변수를 호출 안할때는, 기본 매개변수가 가변 매개변수보다 무조건 뒤에 와야한다.
def func(*val,n=2):
    for i in range(n):
        for v in val:
            print(v)
        print()
func("안녕","안녕하세요","반갑습니다")

# 키워드 매개변수 종류
# end = "", sep = "" 등등.. 이 또한 맨 뒤에 넣어줘야 함
# print(1,2,3,4,5, end="\t")

#----------------------------------------------------------------
# 재귀함수 : 자기자신 함수 호출, 가독성을 좋게 (근데 별로 쓰이진 않음)

#----------------------------------------------------------------
# 파일 열고 닫기
# f = open("파일경로","모드", encoding="utf-8")
# 모드 = "r"
# while True:
#     txt = f.readline().strip()
#     if txt == "": break
# f.close()

#----------------------------------------------------------------
# sort 함수로 오름차순 정렬
a = [52,273,103,32,57,272]
a.sort()
print(a)
# 내림차순
a.sort(reverse=True)
print(a)

#-----------------------------------------------------------------
# math 모듈
from math import sin,cos,tan,floor,ceil
print(sin(1))
print(cos(1))
print(tan(1))
print(floor(2.5))  # 내림
print(ceil(2.5))   # 반올림

# time 모듈 : time.sleep() 특정 시간동안 코드 진행을 정지할 때 사용
import time

print("지금부터 5초 동안 정지합니다.")
time.sleep(5)
print("프로그램을 종료합니다.")