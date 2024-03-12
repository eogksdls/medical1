# 컨프리헨션
numList = [n*n for n in range(10)] # append 하는 기능이나, 더 빠르다
num = [n for n in range(1,21) if n%3==0 ] # 조건까지 가능
print(num)

list = [1,2,3]
# alist = list # 같은 주소를 사용함, 얕은 복사
alist = [*list] # 깊은 복사1 - 메모리 공간의 크기를 복사
alist = list[:] # 깊은 복사2
list[0] = 100 # alist의 값도 변하게 된다.

print(alist)

a = 100
b = a # b는 b의 공간을 따로 만들기 때문에, 병렬적으로 바뀌지 않는다
a = 10
print(b) # 100
