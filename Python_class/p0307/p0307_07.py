import random

fruit = { 'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

print('개수: ',len(fruit))
# 랜덤으로 4개를 출력
# 랜덤은 리스트
# key를 리스트 타입으로 변경
fru = list(fruit.keys())
print(random.sample(fru,4))
# 또는 
print(random.sample(list(fruit.keys()),4))

# 4개의 랜덤 key를 출력하시오
f_list = random.sample(list(fruit.key()),4)
print(list(f_list))

f_list2 = ["kiwi","grapes","peach","pear"]

print(fruit[f_list2[0]]) # 키위
print(fruit[f_list2[1]]) # 포도
print(fruit[f_list2[2]]) # 복숭아
print(fruit[f_list2[3]]) # 배


# value값을 전체 출력
for key in fruit:
    print(fruit[key])