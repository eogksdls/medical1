# student = ['K1','K2','K3']
students = []
cnt = 1
# 학번, 이름, 국어, 영어, 수학, 합계, 평균 입력하는 프로그램
while True:
    chk = input("학번을 추가하시겠습니까?(1.추가, 0.취소)")
    if chk == '1':
        stu = {}
        stuNo = "K"+ "{:03d}".format(cnt)
        name = input("이름을 입력하세요:  ")
        kor = int(input("국어 점수를 입력하세요:  "))
        eng = int(input("영어 점수를 입력하세요:  "))
        math = int(input("수학 점수를 입력하세요:  "))
        total = kor+eng+math
        avg = '{:.2f}'.format(total/3)
        print("학번이 추가되었습니다.")
        stu["stuNo"] = stuNo
        stu["name"] = name
        stu["eng"] = eng
        stu["math"] = math
        stu["total"] = total
        stu["avg"] = avg
        students.append(stu)
        # 최종 저장은 딕셔너리 형태로
        cnt += 1
        print(students)
    else:
        print("학번 추가를 종료합니다.")
        break