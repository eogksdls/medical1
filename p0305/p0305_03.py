# 리스트 공간을 먼저 생성
# a = [[],[],[],[],[]]
# 리스트 공간 초기화를 먼저 해줘야 함.
a = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
a = [[0]*5]*5

# for i in range(0,5):
#     for j in range(0,5):
#         a[i].append((5*i)+j+1)
# print(a)

value = 1
for i in range(0,5):
    for j in range(0,5):
        a[i][j] = value
        value += 1
print(a)