import stu_file
# stu_file 파일 열기 호출
students = stu_file.stu_open()
s_title = ['','국어','영어','수학']
# 학생성적화면 함수
def stu_mainprint():
    print('-'*40)
    print('\t[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print("7. 학생성적 파일 저장")
    print('0. 프로그램 종료')
    print('-'*40)
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
    choice = int(choice)
    
    return choice
#--------------------------------------------------
# 학생성적입력 함수
def stu_insert():
    while True:   
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요(0.취소):  ")
        if name == "0":
            print("학생 입력을 취소합니다.")
            break
        student = {}
        student["stuNo"] = len(students)+1
        student["name"] = name  # 딕셔너리 추가
        kor = int(input("국어 점수를 입력하세요:  "))
        student["kor"] = kor
        eng = int(input("영어 점수를 입력하세요:  "))
        student["eng"] = eng
        math = int(input("수학 점수를 입력하세요:  "))
        student["math"] = math
        total = kor+eng+math
        student["total"] = total
        avg = total / 3
        student["avg"] = float("{:.2f}".format(avg))
        student["rank"] = 1
        # list에 추가
        students.append(student)
        print("입력 데이터 값: \t",student) # list -> dict
    return student
#------------------------------------------------------------------
# 학생성적상단출력 함수
def stu_top_print():
    print("[ 학생성적출력 ]")
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('-'*65)

# 학생성적전체출력 함수
def stu_grade_print(stu_list):
    stu_top_print() # 학생성적상단출력 함수호출
    for s_dic in stu_list:
        for s_key in s_dic:
            print(s_dic[s_key], end="\t")
        print()
    print('-'*65)
# -----------------------------------------------------------------
# 학생성적검색 함수
def stu_search():
# 학생 검색 -> 이름으로 검색을 해서 해당하는 학생이 있으면 해당학생만 출력
# 1명만 출력
    search_student = []
    print("[ 학생성적 검색 ]")
    search = input("찾고자 하는 학생 이름을 입력하세요:  ")
    
    search_cnt = 0
    for s in students:
        if s["name"] == search:
            break
        search_cnt += 1  # 마지막 학생이 있는 방번호는 len(students)-1
        
    if search_cnt == len(students):  # 방번호가 학생수보다 1 작기 때문
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요.")
    else:
        print("{} 학생을 찾았습니다. 성적을 출력합니다.".format(search)) 
    
        # 1명의 학생을 search_student 리스트에 추가해서
        search_student.append(students[search_cnt])
        stu_grade_print(search_student)  # 학생성적출력함수 호출
# ---------------------------------------------------------------------
# 학생수정함수
def stu_subjuct_update(choice,chk,s_1):
    print("[ {} 수정 ]".format(s_title[choice]))
    print("현재 {} 점수: {}".format(s_title[choice],students[chk][s_1]))
    print('-'*55)
    score = int(input("수정할 {} 점수:  ".format(s_title[choice])))
    students[chk][s_1] = score
    # 합계 수정
    students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
    students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))

    
def stu_update():
    while True:
        # 찾는 부분 프로그램을 작성하세요.
        print("\t[ 학생 검색 ]")
        print('-'*50)
        chk = 0
        s_name = input("성적수정을 원하는 학생의 이름을 입력하세요(0.취소):  ")
        if s_name == "0":
            print("학생성적 수정을 취소하였습니다.")
            break
        for sear_dic in students:
            if s_name == sear_dic["name"]:
                break
            chk += 1
        print("찾고자 하는 학생의 위치:",chk)
        
        if chk == len(students):
            print("{} 학생은 없습니다. 다시 입력하세요.".format(s_name))
        else:
            print('{} 학생을 찾았습니다.'.format(s_name))
            while True:
                print("\t[ 수정할 과목 선택 ]")
                print("-"*55)
                print("1. 국어\t2. 영어\t3. 수학")
                choice = int(input('수정하려는 과목을 선택하세요.(0.취소):  '))
                if choice == 1:
                    s_1 = "kor"
                    stu_subjuct_update(choice,chk,s_1)
                elif choice == 2:
                    s_1 = "eng"
                    stu_subjuct_update(choice,chk,s_1)
                elif choice == 3:
                    s_1 = "math"
                    stu_subjuct_update(choice,chk,s_1)
                else:
                    print("과목 수정을 취소하셨습니다.")
                    print('*'*55)
                    break
                print("{} 학생의 {}점수는 {}으로 수정되었습니다.".format(s_name,s_title[choice],students[chk]["kor"]))
                print(students[chk])
    return s_name
# -----------------------------------------------------------------
# 등수처리함수
def stu_rank():
    print('[ 등수 처리 ]')
    print('-'*55)
    for i, i_dic in enumerate(students):
        rank_cnt = 1 # 등수 처리
        for j_dic in students:
            if i_dic["total"] < j_dic["total"]:
                rank_cnt += 1 # 비교대상 크기가 더 크면 1증가(=순위 내려감)
        i_dic["rank"] = rank_cnt # 등수 위치에 저장
    print('등수 처리가 완료되었습니다.')
    print('*'*55)
#------------------------------------------------------------------------
# 학생삭제함수
def stu_del():
    while True:
        # 찾는 부분 프로그램을 작성하세요.
        print("\t[ 학생 검색 ]")
        print('-'*50)
        chk = 0
        search = input("삭제하고자 하는 학생의 이름을 입력하세요(0.취소):  ")
        if search == "0":
            print("학생 검색을 취소하였습니다.")
            break
        for sear_dic in students:
            if search == sear_dic["name"]:
                break
            chk += 1
            
        print('삭제하고자 하는 학생의 위치: ', chk)
        
        if chk >= len(students):
            print("검색된 학생이 없습니다.")
        else:
            print('{} 학생을 찾았습니다.'.format(search))
            s_input = input('{} 학생 성적을 삭제하시겠습니까?(1.실행, 0.취소):  '.format(search))
            # 삭제
            if s_input != "1":
                print("삭제를 취소합니다.")
                break
            else:
                del(students[chk])
                print('{} 학생의 성적이 삭제되었습니다.'.format(search))
                
    return chk
# -----------------------------------------------------------------------
# 학생성적 파일 저장 함수
def stu_save():
    f = open("stu.txt","w",encoding="utf-8")
    for stu in students:
        f.write("{},{},{},{},{},{},{},{}\n".format(stu["stuNo"],stu["name"],stu["kor"],
                                             stu["eng"],stu["math"],stu["total"],
                                             stu["avg"],stu["rank"]))
    print("모든 내용이 파일에 저장되었습니다.")

    f.close()
# ----------------------------------------------------------------------
# 프로그램 시작
# ----------------------------------------------------------------------

cnt = len(students)+1   # 5 + 1 = 6
# 학생번호 사용
while True:
    # 학생성적화면함수 호출
    choice = stu_mainprint()
    
    # 1. 학생성적입력 프로그램
    if choice == 1:
        stu_insert() # 학생성적입력함수 호출

    # 2. 학생성적전체출력 프로그램
    elif choice == 2 :
        stu_grade_print(students)  # 학생성적전체출력 함수 호출
          
    # 3. 학생 검색
    elif choice == 3 :
        stu_search() # 학생성적검색함수 호출
            
    # 4. 학생 수정   
    elif choice == 4:
        stu_update() # 학생성적수정함수 호출
    
    # 5. 학생 등수처리           
    elif choice == 5:
        stu_rank()
    
    # 6. 학생 삭제
    elif choice == 6:
        search = stu_del()
    # 7. 학생 파일저장
    elif choice == 7:
        stu_save()
    
    elif choice == 0:
        print('프로그램을 종료합니다.')
        break  # 반복문 종료
    else:
        print('선택된 서비스가 없습니다.')
# ---------------------------------------------------------------------