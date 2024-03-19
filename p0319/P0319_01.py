import random


class Card:
    kind = ""
    number = ""
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        
    def __str__(self):
        return f"{self.kind} {self.number}"

kind_list = ["SPADE","DIAMOND","HEART","CLOVER"]
number_list = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_list = []


def random_one():
    num = random.choice(range(52))
    return card_list[num]


# 52장의 카드 만들기
for i in range(4):
    for j in range(13):
        c = Card(kind_list[i],number_list[j])
        card_list.append(c)
# for card in card_list:
#     print("카드 :",card)
# for i in range(52):
#     print("카드 :",card_list[i].kind, card_list[i].number)

# 생성된 카드 중에서 랜덤으로 1장 뽑기
random_one()

# 1. 랜덤카드 5장을 뽑는데, 중복이 되지 않게 하시오.
random5 = []
num_5 = random.sample(range(52),5)   # 0~51 사이의 랜덤 숫자 5개 뽑기
print(num_5)
print('-'*40)
for i in num_5:
    random5.append(Card(card_list[i].kind, card_list[i].number))
for i, ran in enumerate(random5):
    print(f"{i+1}번째 랜덤카드 :", ran)

# 2번째 방법  (같은 카드가 뽑힐수도 있음 -> 확인 후 temp_list에 넣어주기)
temp_list = []

cnt = 0
while True:
    if cnt == 5: break # 랜덤뽑기 카드가 5장일 경우 종료
    c = random_one()
    if cnt > 0 :
        for i in temp_list:
            if c.kind == i.kind and c.number == i.number:  # 같은 카드가 있으면 
                                                           # 다음(다시 랜덤 하나 뽑기)으로 진행
                continue

    # 중복 카드가 없으면 추가
    temp_list.append(c)
    cnt += 1
for i in temp_list:
    print("랜덤1장 뽑기 카드 : ", i.kind, i.number)
