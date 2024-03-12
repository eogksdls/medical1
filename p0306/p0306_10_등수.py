students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33,'rank': 1},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67,'rank': 1},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67,'rank': 1},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0,'rank': 1},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67,'rank': 1}
    ]

'''
# 등수처리는 합계를 가지고 처리함.
for i, i_dic in enumerate(students):
    rank_cnt = 1 # 등수 처리
    for j_dic in students:
        if i_dic["total"] < j_dic["total"]:
            rank_cnt += 1 # 비교대상 크기가 더 크면 1증가(=순위 내려감)
    i_dic["rank"] = rank_cnt # 등수 위치에 저장
print(students)
'''          
    
while True:
    call = input('등수처리를 실행하시겠습니까?(1.실행, 0.취소):  ')
    if call == "0":
        print('등수 처리를 취소합니다.')
        print('*'*55)
        break
    elif call == "1":
        print('[ 등수 처리 ]')
        print('-'*55)
        for i, i_dic in enumerate(students):
            rank_cnt = 1 # 등수 처리
            for j_dic in students:
                if i_dic["total"] < j_dic["total"]:
                    rank_cnt += 1 # 비교대상 크기가 더 크면 1증가(=순위 내려감)
            i_dic["rank"] = rank_cnt # 등수 위치에 저장
    else:
        print('잘못 입력하셨습니다. 다시 입력해주세요.')
    print('등수 처리가 완료되었습니다.')
    print('*'*55)
