import StuUpdate as st # StuUpdate라는 모듈을 사용하기 편하게 st라는 약칭을 붙여주는 것

student = [1,"홍길동",100,100,100,300,100.0,1]
sub = ['','국어','영어','수학']
while True:
    print("학생데이터: ",student)
    print("[ 학생성적 프로그램 ]")
    print('-'*55)
    print("3. 학생성적수정")
    ch = int(input("원하는 번호를 입력하세요:  "))
    print('-'*55)
    
    if ch == 3:
        st.stu_update(ch,sub,student)
        
    else:
        print("프로그램을 종료합니다.")
        break
