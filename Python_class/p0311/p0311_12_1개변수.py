def stu_update(stuNo,name,kor,eng,math): # 지역변수
    stuNo = 2
    name = "유관순"
    total = kor+eng+math  # 지역변수
    avg = total/3         # 지역변수
    return stuNo,name,total,avg
    # 변수가 한 개씩 따로 존재할 때, 반드시 return을 선언해야함
    



# 프로그램 구현
stuNo = 1
name = "홍길동"
kor = 100
eng = 100
math = 100
total = 0
avg = 0

# 함수호출
stuNo,name,total,avg = stu_update(stuNo,name,kor,eng,math)  # 전역변수

print("학생1: ",stuNo,name,kor,eng,math,total,avg)
