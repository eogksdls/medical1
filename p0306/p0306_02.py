import operator
# 리스트 안에 같은 단어가 몇 번 반복되어 써있는지 세볼 수 있는 코드
fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter = {}

for f in fruit:
    if f not in counter: # 딕셔너리에 키가 존재하는지 확인
        counter[f] = 0 # 딕셔너리 키가 없을 때 키 추가
    counter[f] += 1 # 키의 value 값 1 증가
    
print(counter)
