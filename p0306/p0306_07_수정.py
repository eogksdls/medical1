# students = [[S001,'홍길동',100,99,87,286,95.33,2],
            # [S002,'유관순',98,93,87,278,92.67,3],
            # [S003,'이순신',88,76,30,194,64.67,5],
            # [S004,'김구',100,100,100,300,100.00,1],
            # [S005,'강감찬',98,85,44,227,75.67,4]]

students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
    ]
subject = ['순번','학번','이름','국어','영어','수학','합계','평균','등수']
s_title = ['','국어','영어','수학']
cnt = len(students) + 1 # 학번, 이미 students안에 있는 학생 수에 + 1번째부터 시작

while True:
    # 찾는 부분 프로그램을 작성하세요.
    print("\t[ 학생 검색 ]")
    print('-'*50)
    chk = 0
    s_name = input("찾으시는 학생의 이름을 입력하세요(0.취소):  ")
    if s_name == "0":
        print("학생 검색을 취소하였습니다.")
        break
    for sear_dic in students:
        if s_name == sear_dic["name"]:
            break
        chk += 1
    print("찾고자하는 학생의 위치:",chk)
    
    if chk == len(students):
        print("{} 학생은 없습니다. 다시 입력하세요.")
        
    else:
        print('{} 학생을 찾았습니다.'.format(s_name))
        while True:
            print("\t[ 수정할 과목 선택 ]")
            print("-"*30)
            print("1. 국어\t2. 영어\t3. 수학")
            choice = int(input('수정하려는 과목을 선택하세요.(0.취소):  '))
            if choice == 1:
                s_1 = "kor"
                print("[ {} 수정 ]".format(s_title[choice]))
                print("현재 {} 점수: {}".format(s_title[choice],students[chk][s_1]))
                print('-'*25)
                score = int(input("수정할 {} 점수:  ".format(s_title[choice])))
                students[chk][s_1] = score
                # 합계 수정
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                print("{} 학생의 {}점수는 {}으로 수정되었습니다.".format(s_name,s_title[choice],students[chk]["kor"]))
                
            elif choice == 2:
                s_1 = "eng"
                print("[ {} 수정 ]".format(s_title[choice]))
                print("현재 {} 점수: {}".format(s_title[choice],students[chk][s_1]))
                print('-'*25)
                score = int(input("수정할 {} 점수:  ".format(s_title[choice])))
                students[chk][s_1] = score
                # 합계 수정
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                print("{} 학생의 {}점수는 {}으로 수정되었습니다.".format(s_name,s_title[choice],students[chk]["eng"]))
                
            elif choice == 3:
                s_1 = "math"
                print("[ {} 수정 ]".format(s_title[choice]))
                print("현재 {} 점수: {}".format(s_title[choice],students[chk][s_1]))
                print('-'*25)
                score = int(input("수정할 {} 점수:  ".format(s_title[choice])))
                students[chk][s_1] = score
                # 합계 수정
                students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
                students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
                print("{} 학생의 {}점수는 {}으로 수정되었습니다.".format(s_name,s_title[choice],students[chk]["math"]))
                
            else:
                print("과목 수정을 취소하셨습니다.")
                print('*'*40)
                break

        