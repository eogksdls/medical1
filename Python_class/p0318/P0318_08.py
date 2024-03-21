class Card:   # 4개의 변수 : kind,number,width,height
    width = 0 # 클래스 변수
    height = 0 # 클래스 변수
    
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
        Card.width = 100
        Card.height = 200
    

# 52장 카드 생성
shape = ["SPADE","DIAMOND","HEART","CLOVER"]
number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_list = []
for i in range(4):
    for j in range(13):
        c = Card(shape[i],number[j])  # 객체선언
        card_list.append(c)  # 리스트 추가
        

for i in range(52):
    c = card_list[i]  # c = Card 객체
    print("카드 출력: ", c.kind, c.number)
    
# 클래스 5개를 생성해서 kind = "spade", number = 1,2,3,4,5
# 클래스를 출력하시오

card_list = []
card_list.append(Card("SPADE","A"))
for i in range(2,11):
    card_list.append(Card("SPADE",i))
    # card_list.append(Card("SPADE","A"))
    # card_list.append(Card("SPADE","2"))
    # ...
    # card_list.append(Card("SPADE","J"))
    # card_list.append(Card("SPADE","Q"))
    # card_list.append(Card("SPADE","K"))
card_list.append(Card("SPADE","J"))
card_list.append(Card("SPADE","Q"))
card_list.append(Card("SPADE","K"))
print(f"리스트 개수: {len(card_list)}")
for i in range(13):
    print("리스트 출력: ",card_list[i].kind, card_list[i].number)


