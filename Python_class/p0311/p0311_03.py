# 구구단 - 이중 for문을 사용하고 있음
temp = 0
for i in range(1,10):
    print(f'[ {i}단 ]')
    for j in range(1,10):
        if j == 5:
            temp = 1
            break
        print(f"{i} * {j} = {i*j}")
    if temp == 1: break