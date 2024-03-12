students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33,'rank': 1},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67,'rank': 1},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67,'rank': 1},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0,'rank': 1},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67,'rank': 1}
    ]

# 학생성적입력 부분 구현
cnt = len(students)+1 # 이미 students에 들어있는 학생 정보수 + 1부터 시작할 수 있도록

while True:
    print('[ 학생성적입력 ]')
    print('-'*55)
    name = input(f"{len(students)+1}번째 학생을 입력하세요(0.취소):  ")
    if name == "0":
        print('학생 입력을 취소합니다.')
        print('*'*55)
        break
    student = {}
    student["name"] = name # 딕셔너리에 추가하고 싶으면 dic["key 값"] = 넣고 싶은 값, 수정 시에도 동일한 코드
    student["stuNo"] = "S"+"{:03d}".format(cnt)
    kor = int(input('국어 점수 입력:  '))
    student["kor"] = kor
    eng = int(input("영어 점수 입력:  "))
    student["eng"] = eng
    math = int(input("수학 점수 입력:  "))
    student["math"] = math
    total = student["kor"]+student["eng"]+student["math"]
    student["total"] = total
    avg = total / 3
    student["avg"] = float("{:.2f}".format(avg))
    # list에 추가
    students.append(student)
    cnt += 1  # 학번 증가
    print('입력 데이터값: \t', student)
    
# 학생전체성적출력 구현
while True:
    print('\t[ 학생전체성적출력 ]')
    print('-'*65)
    ch = input('학생전체성적출력을 실행하시겠습니까?(1.실행, 0.취소):  ')
    if ch == "0":
        print('학생전체성적출력을 취소하셨습니다.')
        print('*'*65)
        break
    elif ch == "1":
        print('[ 학생전체성적출력 ]')
        print('-'*65)
        print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        for i_dic in students:
            for i in i_dic:  # 여기서 i는 value, i_dic은 key
                print(i_dic[i], end='\t')
            print()
        print('-'*65)
            
    
    