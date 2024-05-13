def stu_print():
    print("[ 학생성적 프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')


# 성적점수부분 함수
def score_update(ch,sub,student):
    print(f"[ {sub[ch]}성적 수정]")
    print(f"현재 {sub[ch]}점수: ",student[ch+1])
    print('-'*30)
    student[ch+1] = int(input("수정 점수를 입력하세요:  "))
    print("수정된 점수: ", student[ch+1])
    student[5]=student[2]+student[3]+student[4]
    student[6] = float("{:.2f}".format(student[5]/3))
    print(f"{sub[ch]}점수가 수정되었습니다.")
    
def stu_update(ch,sub,student):
    print("[ 학생성적수정 ]")
    print("1. 국어  2.영어  3.수학")
    ch = int(input("원하는 번호를 입력하세요:  "))
    
    if ch == 1:
            score_update(ch,sub,student)
     
    elif ch == 2:
        score_update(ch,sub,student)
            
    elif ch == 3:
        score_update(ch,sub,student)
    
    return ch