# 파일에서 리스트 형태로 학생정보 가져오기
students = []
f = open("stu.txt","r",encoding="utf-8")
while True:
    txt = f.readline().strip()
    if txt == "": break
    stu_list = txt.split(",")  # csv 파일을 ,으로 분리
    s_dic = {
        "stuNo":stu_list[0],"name":stu_list[1],"kor":int(stu_list[2]),
        "eng":int(stu_list[3]),"math":int(stu_list[4]),"total":int(stu_list[5]),
        "avg":float(stu_list[6]),"rank":int(stu_list[7])
    }
    students.append(stu_list)
f.close()

cnt = len(students)+1   # 5 + 1 = 6
# 학생번호 사용
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
    
    if choice == 2 :
        while True:
            count = input('학생전체 출력을 하시겠습니까?(1.확인, 0.취소):  ')
            if count == "1":
                print("[ 학생성적전체출력 ]")
                print('-'*65)
                print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
                print('-'*65)
                for s_dic in students:
                    for s_key in s_dic:
                        print(s_dic[s_key], end="\t")
                    print()
                print('-'*65)
            elif count == "0":
                print("학생전체 출력을 취소하셨습니다.")
                break
    
  