import operator
# 리스트 안에 같은 단어가 몇 번 반복되어 써있는지 세볼 수 있는 코드
fruit = [ '바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과','바나나','바나나',
    '바나나','딸기','배','사과','딸기',
    '딸기','딸기','딸기','사과']

counter = {}

# 딕셔너리 추가
counter['복숭아'] = 5 # 딕셔너리 추가
counter['바나나'] = 4 # 딕셔너리 추가
counter['바나나'] = 1 # 딕셔너리 수정
# print(counter['딸기']) # 딕셔너리에 없는 키값을 출력할 때 에러
print(counter['바나나'])

if '딸기' not in counter:# 키가 존재하는지 확인
    counter['딸기'] = 0 # 없으면 키 생성
else:
    print(counter['딸기']) # 키의 value값을 출력

del counter['복숭아'] # 딕셔너리 삭제

print(counter)

print(counter.keys())
print(counter.values())
print(counter.items())

a_list = [3,5,7,4,1,2,6]
print(sorted(a_list))

# 변수: 1개 값 저장 타임
# 리스트: 복수개를 저장 타입 [] - append, remove, del
# 딕셔너리: 복수개를 저장 타입 {}
# (key,value)
