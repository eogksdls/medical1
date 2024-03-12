students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33, "rank": 1},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67,"rank": 1},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67,"rank": 1},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0,"rank": 1},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67,"rank": 1}
    ]
# Json 형태(딕셔너리 in 리스트), csv 형태(,로 구분되어있음)
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        continue # 반복문 계속실행
    choice = int(choice)
    
    # 1. 학생성적입력 
    if choice == 1:
        while True:
            cnt = len(students)+1
            ask = input("[  학생성적입력 ]을 선택하셨습니다.(1. 진행, 0.취소):  ")
            print(f">> {cnt}번째 학생 입력")
            if ask == "1":
                stu = {}
                print("[ 학생성적입력 ]")
                print('-'*55)
                stu["stuNo"] = "S"+"{:03d}".format(cnt)
                name= input("학생 이름을 입력하세요:  ")
                stu["stuName"] = name
                kor = int(input("국어 성적 입력:  "))
                stu["kor"] = kor
                eng = int(input("영어 성적 입력:  "))
                stu["eng"] = eng
                math = int(input("수학 성적 입력:  "))
                stu["math"] = math
                total= kor + eng + math
                stu["total"] = total
                avg = '{:.2f}'.format(total/3)
                stu["avg"] = avg
                stu["rank"] = 1
                students.append(stu)
                cnt += 1
                print("입력한 학생 데이터 값: {}".format(stu))    
            else:
                print("[ 학생성적입력 ]을 취소합니다.")
                print('*'*70)
                break
    
    # 2. 학생성적전체출력
    elif choice == 2:
        while True:
            ask = input("[ 학생성적전체출력 ]을 선택하셨습니다.(1.진행, 0.취소):  ")
            if ask == "1":
                print("\t\t[ 학생성적전체출력 ]")
                print('-'*70)
                print("학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
                print('-'*70)
                for i_dic in students:
                    for i_key in i_dic:
                        print(i_dic[i_key],end= '\t')
                    print()
                print('-'*70)
            else:
                print("[ 학생성적전체출력 ]을 취소합니다.")
                print('*'*70)
                break
    
    # 3. 학생 검색
    elif choice == 3:
        while True:
            ask = input("[ 학생 검색 ]을 선택하셨습니다.(1.진행, 0.취소):  ")
            if ask == "1":
                print("[ 학생 검색 ]")
                print('-'*70)
                searName = input("검색하실 학생의 이름을 입력해주세요:  ")
                for i, sear_dic in enumerate(students):
                    if sear_dic["name"] == searName:
                        print("검색하신 학생의 성적 정보를 조회합니다.")
                        print('-'*70)
                        print(f">> 찾은 위치 : {i}")
                        print("학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
                        print('-'*70)
                        for i_key in sear_dic:
                            print(sear_dic[i_key], end='\t')
                        print()
                        cnt += 1
                    else:
                        print("검색한 학생의 성적정보가 없습니다.")
                print('-'*70)
            else:
                print("[ 학생 검색 ]을 취소합니다.")
                print('*'*70)
                break
    
    # 4. 학생수정
    elif choice == 4:
        while True:
            ask = input("[ 학생수정 ]을 선택하셨습니다.(1.진행, 0.취소)")
            if ask == "1":
                print("[ 학생 수정]")
                print("-"*70)
                reName = input("수정할 학생의 이름을 입력하세요:  ")
                for i, sear_dic in enumerate(students):
                    if sear_dic["name"] == reName:
                        print("검색하신 학생의 성적 정보를 조회합니다.")
                        print('-'*70)
                        print(f">> 찾은 위치 : {i}")
                        print("학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
                        print('-'*70)
                        for i_key in sear_dic:
                            print(sear_dic[i_key], end='\t')
                        print()
                        print('-'*70)
                        print('[1.국어\t2.영어\t3.수학]')
                        ask1 = input("수정하고 싶은 과목을 선택하세요(0.취소):  ")
                        if ask1 == "1" or ask1 == "국어":
                            print(">> 국어 수정")
                            print('-'*55)
                            print("{} 학생의 현재 국어 점수: {}".format(reName,sear_dic["kor"]))
                            re_kor = int(input("수정할 국어 점수:  "))
                            sear_dic["kor"] = re_kor
                            print("수정 완료된 {} 학생의 국어 점수: {}".format(reName,sear_dic["kor"]))
                        elif ask1 == "2" or ask1 == "영어":
                            print(">> 영어 수정")
                            print('-'*55)
                            print("{} 학생의 현재 영어 점수: {}".format(reName,sear_dic["eng"]))
                            re_eng = int(input("수정할 영어 점수:  "))
                            sear_dic["eng"] = re_eng
                            print("수정 완료된 {} 학생의 영어 점수: {}".format(reName,sear_dic["eng"]))
                        elif ask1 == "3" or ask1 == "수학":
                            print(">> 수학 수정")
                            print('-'*55)
                            print("{} 학생의 현재 수학 점수: {}".format(reName,sear_dic["math"]))
                            re_math = int(input("수정할 수학 점수:  "))
                            sear_dic["math"] = re_math
                            print("수정 완료된 {} 학생의 수학 점수: {}".format(reName,sear_dic["math"]))
                        else:
                            print("[ 학생 성적 수정 ]을 취소하셨습니다.")
                            break
                        
                        sear_dic["total"] = sear_dic["kor"] + sear_dic["eng"] + sear_dic["math"]
                        sear_dic["avg"] = "{:.2f}".format(sear_dic["total"]/3)
                        
                    else:
                        print("해당 학생의 성적정보를 조회할 수 없습니다.")
                        
            else:
                print("[ 학생 수정 ]을 취소하셨습니다.")
                print("*"*55)
                break
                    
    
    # 5. 등수처리
    elif choice == 5:
        while True:
            ask = input("[ 등수처리 ]를 선택하셨습니다.(1.진행, 0.취소):  ")
            if ask == "1":
                print("[ 등수 처리 ]")
                print("-"*55)
                for i, i_dic in enumerate(students):
                    rank_cnt = 1 # 등수 처리
                    for j_dic in students:
                        if i_dic["total"] < j_dic["total"]:
                            rank_cnt += 1 # 비교대상 크기가 더 크면 1증가(=순위 내려감)
                    i_dic["rank"] = rank_cnt  # 등수 위치에 저장
                print("[ 등수 처리 ]가 완료 되었습니다.")
            else:
                print("[ 등수 처리 ]를 취소합니다.")
                print('*'*55)
                break
    
    # 6. 학생 삭제
    elif choice == 6:
        while True:
            ask = input("[ 학생 삭제 ]를 선택하셨습니다.(1.진행, 0.취소):  ")
            if ask == "1":
                print("[ 학생 삭제 ]")
                print('-'*55)
                delName = input("성적 정보 삭제를 원하는 학생을 입력하세요:  ")
                for i, i_dic in enumerate(students):
                    if delName == i_dic["name"]:
                        print(f"{delName} 학생을 찾은 위치: {i}")
                        ask1 = int(input("해당 학생의 성적정보를 삭제하시겠습니까?(1.예 0.아니오):  "))
                        if ask1 == "1":
                            print(f"{delName} 학생의 성적정보를 삭제합니다.")
                            del students[i]
                            print('-'*55)
                        else:
                            print("해당 학생의 성적정보 삭제를 취소합니다.")
                            break
                    else:
                        print("해당 학생의 성적정보를 조회할 수 없습니다.")
            else:
                print("[ 학생 삭제 ]를 취소하셨습니다.")
                print('*'*55)
                break
    
    # 0. 프로그램 종료
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break
                