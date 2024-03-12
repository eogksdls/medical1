list = [
    [0,0,0],[0,0,0],[0,0,0]
]

for i in list:
    for f in i:
        print(f, end="\t")
    print()
 
# 1차원 리스트에 1-9까지의 숫자를 입력하세요.
list = []
for i in range(9):
    list.append(i+1)
print('list =',list)

list2 = [n+1 for n in range(9)]
print('list2 =',list2)

list3 = [[n+1]*3 for n in range(3)]
print("list3 =",list3)

numList = [num*num for num in range(1,6)] # 제곱근
print("numList =",numList)


# 1-9까지의 2차원 리스트에 숫자를 입력하세요
# list = []
# l = []
# for i in range(1,10):
#     if i % 3 == 0:
#         l.append(i)
#         list.append(l)
#         l = []
#     else:
#         l.append(i)
# print(list)
# # 또는
# lists = []
# for i in range(3):
#     list = []
#     for j in range(3):
#         list.append((3*i)+j+1) # i가 0,1,2의 값을 순차적으로 가짐
#     lists.append(list)
# print(lists)
