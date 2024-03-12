def stu_update(student): # 지역변수 ->  주소값이 저장
    student["stuNo"] = 2
    student["name"] = "유관순"
    student["total"] = student["kor"]+student["eng"]+student["math"]  # 지역변수
    student["avg"] = student["total"]/3         # 지역변수
    



# 프로그램 구현
student = {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33}  # 2개 이상의 변수, 주소값 저장
# 딕셔너리 형태로 변수값이 2개 이상

# 함수호출
stu_update(student)  # 전역변수, return 받을 필요 없다.

print("학생1: ",student) # 1,홍길동,100,100,100,300,100.0