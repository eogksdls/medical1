# student 클래스 생성, 파일 불러와서 클래스에 저장 후 출력하시오

# --------------------------------------------------------------------
class Student:
    count = 1
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0:
            self.stuNo = Student.count   # 여기선 클래스변수 Student.count = 1
        else:
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = rank

    def __str__(self):
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"

f = open("stu.txt","r",encoding="utf-8")
students = []
while True:
    txt = f.readline().strip()    # 텍스트 파일을 한줄씩 읽어내려가다가
    if txt =="" : break           # 빈칸줄일 때 읽어내려가는 것을 중지
    txt_list = txt.split(",")     # 텍스트줄 내 ","을 기준으로 split하여 요소 하나하나씩 저장
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)            # students list에 한 묶음씩 저장
f.close()

# 학생화면---------------------------------------------------------------------
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
    
# 학생성적입력------------------------------------------------------------------
def stu_insert():
    while True:
            newName = input(f"{len(students)+1}번째 학생의 이름을 입력하세요(0.취소):  ")
            if newName == "0":
                print("[ 학생성적입력 ]을 종료합니다.")
                break
            n_kor = int(input("국어 성적 입력:  "))
            n_eng = int(input("영어 성적 입력:  "))
            n_math = int(input("수학 성적 입력:  "))
            n_stuNo = len(students)+1
            s_new = Student(newName,n_kor,n_eng,n_math,n_stuNo,0)    # class 객체선언
            students.append(s_new)   # 새롭게 입력된 값을 students list내에 저장
            print("-"*60)
            print("입력된 성적값: ", s_new)  # class 내 str 함수 형식으로 출력될 것
            print("-"*60)
# 학생성적출력 메인-----------------------------------------------------------------------------
def stu_print_main():
    print("\t\t[ 학생 성적출력 ]")
    print('-'*70)
    print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
    print('-'*70)
# 학생성적 파일 저장--------------------------------------------------------------------------------------
def stu_file():
    ff = open("stu.txt","w",encoding="utf-8")   # students 리스트에 저장되어있는 학생성적목록을 stu.txt란 텍스트파일에 새롭게 덮어쓰기(수정사항, 등수처리된 것도 반영됨)
    for i in range(len(students)):              # 출력시 students[i]만 작성하면, 주소값만 출력된다.
        ff.write("{},{},{},{},{},{},{},{}\n".format(students[i].stuNo,students[i].name,students[i].kor \
            ,students[i].eng,students[i].math,students[i].total,students[i].avg,students[i].rank))
    print("모든 내용이 파일에 저장되었습니다.")
    ff.close()
# 학생 검색------------------------------------------------------------------------------------------------
def stu_sear_title():
    print("[ 학생 검색 ]")
    print("-"*40)
    print("1. 학생 이름으로 검색")
    print("2. 점수이상 검색")
    print("3. 점수미만 검색")
    print("0. 종료")
    print('-'*40)
    choice = int(input("원하는 번호를 입력하세요:  "))
    return choice
        
search_txt = ["",
                "검색할 학생의 이름을 입력하세요:  ",
                "점수를 입력하세요:  ",
                "점수를 입력하세요:  "]      # 하나의 함수로 묶기 위해서 다르게 들어가는 멘트만 따로 정리 -> 이는 choice의 호출에 의해 각각의 주소 값이 호출된다.
def stu_search(choice):
    if choice == 1:
        search = input(search_txt[choice])   # 1. 학생이름으로 검색 : "검색할 학생의 이름을 입력하세요" 출력
    else:
        search = int(input(search_txt[choice]))   # 2,3. 점수이상,미만 검색 : "점수를 입력하세요" 출력
        
    # 전체리스트에서 학생검색
    s_list =[]
    for s in students:
        if choice == 1:    # 학생 이름으로 출력(일부 문자 포함시 모두 검색되는 함수식)
            if s.name.find(search) != -1: # find(): 특정문자를 포함하는 문자열 인덱스 출력 # 없으면 -1 출력하기 때문에, -1이 아닐때는 학생이 검색된 것
                s_list.append(s)   # s_list에 인덱스 값 추가
        elif choice == 2:   # 몇 점 이상인 학생 모두 검색
                if s.total >= search :
                    s_list.append(s)
        elif choice == 3:   # 몇 점 미만인 학생 모두 검색
                if s.total < search :
                    s_list.append(s)
    if len(s_list) != 0:   # s_list에 인덱스값이 추가됨 : 학생이 검색된 것, len(s_list) == 0이란 것은 학생을 찾을 수 없음
        stu_print_main()
        for i in s_list:
            print(i)    # ????
        print('-'*70)
        print()
    else:
        print("찾고자 하는 학생이 없습니다. 다시 검색하세요.")
# 성적 수정------------------------------------------------------------------------
sub = ["","국어","영어","수학"]
def stu_modify(chk):   # 합계 수정
    students[chk].total = students[chk].kor + students[chk].eng + students[chk].math
    students[chk].avg = float("{:.2f}".format(students[chk].total/3))
    stu_print_main()
    print(students[chk])
    
# 등수처리-------------------------------------------------------------------------
def stu_rank():
    print('[ 등수 처리 ]')
    print('-'*55)
    for i in students:
        rank_cnt = 1 # 등수 처리
        for j in students:
            if i.total < j.total:
                rank_cnt += 1 # 비교대상 크기가 더 크면 1증가(=순위 내려감)
        i.rank = rank_cnt # 등수 위치에 저장
    print('등수 처리가 완료되었습니다.')
    print('*'*55)

# 학생 삭제-------------------------------------------------------------------------
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
        for stu in students:
            if search == stu.name:
                break
            chk += 1
            
        print('삭제하고자 하는 학생의 위치: ', chk)
        
        if chk == len(students):
            print("검색된 학생이 없습니다.")
        else:
            print('{} 학생을 찾았습니다.'.format(search))
            print('-'*50)
            s_input = int(input(f'{search} 학생 성적을 삭제하시겠습니까?(1.실행, 0.취소):  '))
            # 삭제
            if s_input != 1:  # 1이 아닐경우 삭제 못하도록
                print("삭제를 취소합니다.")
                break
            else:
                del(students[chk])   # 인덱스 위치 리스트 삭제
                print(f'{search} 학생의 성적이 삭제되었습니다.')
                print('-'*50)
#----------------------------------------------------------------------------------
# 학생프로그램 구현
# ---------------------------------------------------------------------------------
while True:
    choice = stu_mainprint()
    # 1. 학생성적입력
    if choice == 1:
        stu_insert()
        
    # 2. 학생전체출력
    elif choice == 2:
        stu_print_main()
        for stu in students:
            print(stu)
        print('-'*70)
        
    # 3. 학생검색
    elif choice == 3:
        while True:
            choice = stu_sear_title()
            if choice == 0:
                print("[ 학생 검색 ]을 종료하고 이전화면으로 이동합니다.")
                break
            # 학생검색 프로그램 부분 
            stu_search(choice)
                           
    # 4. 학생수정
    elif choice == 4:
        while True:
            # 1. 학생 이름으로 검색
            search = input("찾고자하는 학생의 이름을 입력하세요.(0.취소):  ")
            chk = 0
            if search == "0":
                print("[ 학생수정 ]을 취소합니다.")
                break
            for stu in students:
                if stu.name == search:
                    break
                chk += 1
                
            if chk == len(students):
                print("조회된 학생이 없습니다. 다시 검색하세요.")
            else:
                print("찾고자 하는 학생의 위치 :",chk)
                stu_print_main()
                print(students[chk])
                print('*'*70)
                # 수정과목 선택
                print("\t[ 수정할 과목 선택 ]")
                print('-'*45)
                print("1. 국어\t2. 영어\t3. 수학")
                s_input = int(input("수정하고 싶은 과목을 고르세요(0.취소):  "))
                if s_input == 1:
                    print(f"[ {sub[s_input]} 성적 수정 ]")
                    print(f"현재 {sub[s_input]} 점수: {students[chk].kor}")
                    print('-'*45)
                    students[chk].kor = int(input(f"수정할 {sub[s_input]} 점수:  "))
                    print(">> 수정이 완료되었습니다.")
                    stu_modify(chk)
                elif s_input == 2:
                    print(f"[ {sub[s_input]} 성적 수정 ]")
                    print(f"현재 {sub[s_input]} 점수: {students[chk].eng}")
                    print('-'*45)
                    students[chk].eng = int(input(f"수정할 {sub[s_input]} 점수:  "))
                    print(">> 수정이 완료되었습니다.")
                    stu_modify(chk)
                elif s_input == 3:
                    print(f"[ {sub[s_input]} 성적 수정 ]")
                    print(f"현재 {sub[s_input]} 점수: {students[chk].math}")
                    print('-'*45)
                    students[chk].math = int(input(f"수정할 {sub[s_input]} 점수:  "))
                    print(">> 수정이 완료되었습니다.")
                    stu_modify(chk)
                else:
                    print("[ 과목 수정 ]을 취소합니다.")
                    break
    # 5. 등수처리
    elif choice == 5:
        stu_rank()
    # 6. 학생 삭제
    elif choice == 6:
        stu_del()
    # 7. 학생성적파일저장
    elif choice == 7:
        stu_file()
    # 0. 프로그램 종료
    elif choice == 0:
        print("프로그램을 종료합니다.")
        print('*'*40)
        break