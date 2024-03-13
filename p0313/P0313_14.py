import random

c_number = [0]*13
for i in range(13):
    c_number[i-1] = i
    

c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# 랜덤으로 2개의 숫자를 뽑아서 출력하세요
# 랜덤숫자 : 2 -> 1번방에 있습니다.
# 랜덤숫자 : 9 -> 8번방에 있습니다.
# 큰수 : 9, 작은수 : 2

ran_num = random.sample(c_number,k=2)
print(ran_num)
for i, s in enumerate(c_number):
    if ran_num[0] in c_number:
        print(f"랜덤숫자 : {ran_num[0]} -> {c_number[i]}번방에 있습니다.")
        print(f"랜덤숫자 : {ran_num[1]} -> {c_number[i]}번방에 있습니다.")

if ran_num[0] > ran_num[1]:
    print(f"큰 수: {ran_num[0]}, 작은 수: {ran_num[1]}") 
else:
    print(f"큰 수: {ran_num[1]}, 작은 수: {ran_num[0]}")
    
