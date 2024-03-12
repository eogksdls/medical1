# 리스트 복사는 같은 주소값을 가진다

# 리스트에 1,25까지 숫자를 입력해보세요!
list = []
for i in range(1,26,1):
    list.append(i)

print(list)
print('-'*40)

# [[1,2,3,4,5],[6,7,8,9,10],...,[21,22,23,24,25]]
list_a = []
a = []
for i in range(1,26):
    if i % 5 == 0:
        a.append(i) #[1,2,3,4,5]
        list_a.append(a)
        a = []
    else:
        a.append(i) #[1,2,3,4]
print(list_a)

b = [[],[],[],[],[]]
for i in range(0,5):
    for j in range(0,5):
        b[i].append((5*i)+j+1)
print(b)