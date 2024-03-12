a_list = []
a_list.append(0) # 리스트 append 추가를 하게 되면 속도가 느림.
a_list.append(1)
a_list.append(2)
a_list[0] = 3 # 리스트에 값을 넣는 것이 속도면으로는 빠름
print(a_list)

# 공간을 만들어 놓고 for문을 사용
list = [0]*10 # 리스트 내 0이 10개가 들어감
for i in list:
    list[i] = i+1 # 데이터를 수정하는 방법을 이용 -> 속도면에서 빠름 
print(list) 

# 컴프리헨션을 사용하는 방법
list1 = [i+1 for i in range(10)]
print(list1)

arr = [[0]*3 for _ in range(3)]
