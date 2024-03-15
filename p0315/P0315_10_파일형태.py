# 파일에서 리스트 형태로 학생정보 가져오기
students = []
f = open("stu.txt","r",encoding="utf-8")
while True:
    txt = f.readline().strip()
    if txt == "": break
    stu_list = txt.split(",")  # csv 파일을 ,으로 분리
    s_dic = {
        "stuNo":int(stu_list[0]),"name":stu_list[1],"kor":int(stu_list[2]),
        "eng":int(stu_list[3]),"math":int(stu_list[4]),"total":int(stu_list[5]),
        "avg":float(stu_list[6]),"rank":int(stu_list[7])
    }
    students.append(stu_list)
f.close()
# 학생성적화면 함수
def stu_main():
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
    choice = int(choice)
    
    return choice

# 학생성적입력함수 ------------------------------------------------------------------
def stu_insert():
    f = open("stu.txt","a",encoding="utf-8")
        
    while True:   
        name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요(0.취소):  ")
        if name == "0":
            print("학생 입력을 취소합니다.")
            break
        ss_dic = {}
        ss_dic["stuNo"] = len(students)+1
        ss_dic["name"] = name  # 딕셔너리 추가
        kor = int(input("국어 점수를 입력하세요:  "))
        ss_dic["kor"] = kor
        eng = int(input("영어 점수를 입력하세요:  "))
        ss_dic["eng"] = eng
        math = int(input("수학 점수를 입력하세요:  "))
        ss_dic["math"] = math
        total = kor+eng+math
        ss_dic["total"] = total
        avg = total / 3
        ss_dic["avg"] = float("{:.2f}".format(avg))
        ss_dic["rank"] = 1
        # 파일에 추가
        f.write("{},{},{},{},{},{},{},{}\n".format(ss_dic["stuNo"],ss_dic["name"],ss_dic["kor"],
                                                    ss_dic["eng"],ss_dic["math"],ss_dic["total"],
                                                    ss_dic["avg"],ss_dic["rank"]))
        students.append(ss_dic)
        print("입력 데이터 값: \t",ss_dic)
        f.close()
# -------------------------------------------------------------------------------
# 학생성적상단출력 함수
# ---------------------------------------------------------------------------------------------------------
# 프로그램 구현
# ----------------------------------------------------------------------------
cnt = len(students)+1   # 5 + 1 = 6
# 학생번호 사용
while True:
    choice = stu_main()
    # 1. 학생성적입력 프로그램
    if choice == 1:
        stu_insert()

    # 2. 학생성적전체출력 프로그램
    elif choice == 2 :
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
    # # 3. 학생 검색
    # elif choice == 3 :
    #     pass
    # # 4. 학생 수정   
    # elif choice == 4:
    #     s_title = ['','국어','영어','수학']

    #     while True:
    #         # 찾는 부분 프로그램을 작성하세요.
    #         print("\t[ 학생 검색 ]")
    #         print('-'*50)
    #         chk = 0
    #         s_name = input("찾으시는 학생의 이름을 입력하세요(0.취소):  ")
    #         if s_name == "0":
    #             print("학생 검색을 취소하였습니다.")
    #             break
    #         for sear_dic in students:
    #             if s_name == sear_dic["name"]:
    #                 break
    #             chk += 1
    #         print("찾고자하는 학생의 위치:",chk)
            
    #         if chk == len(students):
    #             print("{} 학생은 없습니다. 다시 입력하세요.".format(s_name))
                
    #         else:
    #             print('{} 학생을 찾았습니다.'.format(s_name))
    #             while True:
    #                 print("\t[ 수정할 과목 선택 ]")
    #                 print("-"*55)
    #                 print("1. 국어\t2. 영어\t3. 수학")
    #                 choice = int(input('수정하려는 과목을 선택하세요.(0.취소):  '))
    #                 if choice == 1:
    #                     s_1 = "kor"
    #                     print("[ {} 수정 ]".format(s_title[choice]))
    #                     print("현재 {} 점수: {}".format(s_title[choice],students[chk][s_1]))
    #                     print('-'*55)
    #                     score = int(input("수정할 {} 점수:  ".format(s_title[choice])))
    #                     students[chk][s_1] = score
    #                     # 합계 수정
    #                     students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
    #                     students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
    #                     print("{} 학생의 {}점수는 {}으로 수정되었습니다.".format(s_name,s_title[choice],students[chk]["kor"]))
    #                     print(students[chk])
                        
    #                 elif choice == 2:
    #                     s_1 = "eng"
    #                     print("[ {} 수정 ]".format(s_title[choice]))
    #                     print("현재 {} 점수: {}".format(s_title[choice],students[chk][s_1]))
    #                     print('-'*55)
    #                     score = int(input("수정할 {} 점수:  ".format(s_title[choice])))
    #                     students[chk][s_1] = score
    #                     # 합계 수정
    #                     students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
    #                     students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
    #                     print("{} 학생의 {}점수는 {}으로 수정되었습니다.".format(s_name,s_title[choice],students[chk]["eng"]))
    #                     print(students[chk])
                        
    #                 elif choice == 3:
    #                     s_1 = "math"
    #                     print("[ {} 수정 ]".format(s_title[choice]))
    #                     print("현재 {} 점수: {}".format(s_title[choice],students[chk][s_1]))
    #                     print('-'*55)
    #                     score = int(input("수정할 {} 점수:  ".format(s_title[choice])))
    #                     students[chk][s_1] = score
    #                     # 합계 수정
    #                     students[chk]["total"] = students[chk]["kor"] + students[chk]["eng"] + students[chk]["math"]
    #                     students[chk]["avg"] = float("{:.2f}".format(students[chk]["total"]/3))
    #                     print("{} 학생의 {}점수는 {}으로 수정되었습니다.".format(s_name,s_title[choice],students[chk]["math"]))
    #                     print(students[chk])
                        
    #                 else:
    #                     print("과목 수정을 취소하셨습니다.")
    #                     print('*'*55)
    #                     break
    
    # elif choice == 5:
    #     while True:
    #         call = input('등수처리를 실행하시겠습니까?(1.실행, 0.취소):  ')
    #         if call == "0":
    #             print('등수 처리를 취소합니다.')
    #             print('*'*55)
    #             break
    #         elif call == "1":
    #             print('[ 등수 처리 ]')
    #             print('-'*55)
    #             for i, i_dic in enumerate(students):
    #                 rank_cnt = 1 # 등수 처리
    #                 for j_dic in students:
    #                     if i_dic["total"] < j_dic["total"]:
    #                         rank_cnt += 1 # 비교대상 크기가 더 크면 1증가(=순위 내려감)
    #                 i_dic["rank"] = rank_cnt # 등수 위치에 저장
    #         else:
    #             print('잘못 입력하셨습니다. 다시 입력해주세요.')
    #         print('등수 처리가 완료되었습니다.')
    #         print('*'*55)
    
    # elif choice == 6:
    #     while True:
    #         # 찾는 부분 프로그램을 작성하세요.
    #         print("\t[ 학생 검색 ]")
    #         print('-'*50)
    #         chk = 0
    #         search = input("삭제하고자 하는 학생의 이름을 입력하세요(0.취소):  ")
    #         if search == "0":
    #             print("학생 검색을 취소하였습니다.")
    #             break
    #         for sear_dic in students:
    #             if search == sear_dic["name"]:
    #                 break
    #             chk += 1
                
    #         print('삭제하고자 하는 학생의 위치: ', chk)
            
    #         if chk >= len(students):
    #             print("검색된 학생이 없습니다.")
    #         else:
    #             print('{} 학생을 찾았습니다.'.format(search))
    #             s_input = input('{} 학생 성적을 삭제하시겠습니까?(1.실행, 0.취소):  '.format(search))
    #             # 삭제
    #             if s_input != "1":
    #                 print("삭제를 취소합니다.")
    #                 break
    #             else:
    #                 del(students[chk])
    #                 print('{} 학생의 성적이 삭제되었습니다.'.format(search))
    #                 print(students)
    
    # elif choice == 0:
    #     print('프로그램을 종료합니다.')
    #     break  # 반복문 종료
    # else:
    #     print('선택된 서비스가 없습니다.')