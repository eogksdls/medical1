def jegob(val):
    return val**2
def func(val):
    return val>=3

def in_change(val):
    return int(val)


a_list = [1,2,3,4,5]
str_list= ["1","2","3","4","5"]

# map() : 리스트 전체에 값의 변경이 필요할 때
map_list = map(jegob,a_list)  # a_list내의 값이 jegob 함수 val값으로 하나씩 들어간다
print(map_list)  # <map object at 0x0000020F6D5C9C30> 주소값이 나옴
print(list(map_list))  # [1,4,9,16,25] -> 리스트로 타입을 변경해줘야함

ss_list = list(map(in_change,str_list))
print(ss_list)   # -> 문자열을 숫자(정수)로 전체 변경

ss_list2 = list(map(lambda val:int(val),str_list)) # 람다함수(이름없는 함수)에 return 값
print(ss_list2)   # 함수가 없어도 lambda 함수로 만들어 쓸 수 있음
#------------------------------------------------------------------------------------

# filter() : 조건에 맞는 값만 추출해낼 때
f_list = list(filter(func,a_list))  # a_list내 값이 func 함수 val값으로 들어가고
                                    # 함수 내 조건에 맞는 val값만 filtering되어 f_list에 들어간다.
print(f_list)  # [3,4,5]