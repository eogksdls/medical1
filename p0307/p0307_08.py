import random

fruit = { 'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}

f_list = list(fruit.keys())
print(f_list)

# 랜덤 뽑기는 리스트 형태에서만 가능하다.
f_list_ran = random.sample(f_list,4)
print('랜덤추출 :', )
for f in f_list_ran:
    print(fruit[f],end=',')