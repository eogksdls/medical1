class Student:
    # self 있을 때만 total, avg, rank 없어도 출력 가능
    def __init__(self,stuNo=0,stuName="",kor=0,eng=0,math=0):
        self.stuNo = stuNo
        self.stuName = stuName
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = 0

# class를 선언해서
# 1,홍길동,100,100,100,300,100.0,1
# 2,유관순,100,100,99,299,99.97,1
# 3,이순신,100,87,99,286,95.33,1

s1 = Student()
s1.stuNo = 1
s1.stuName = "홍길동"
s1.kor = 100
s1.eng = 100
s1.math = 100
s1.total = s1.kor + s1.eng + s1.math
s1.avg = float("{:.2f}".format(s1.total / 3))
s1.rank = 1
print(f"1번 학생: {s1.stuNo},{s1.stuName},{s1.kor},{s1.eng},{s1.math},{s1.total},{s1.avg},{s1.rank}")
        
s2 = Student(2,"유관순",100,100,99)
print(f"2번 학생: {s2.stuNo},{s2.stuName},{s2.kor},{s2.eng},{s2.math},{s2.total},{s2.avg},{s2.rank}")

s3 = Student(3,"이순신",100,87,99)
print(f"3번 학생: {s3.stuNo},{s3.stuName},{s3.kor},{s3.eng},{s3.math},{s3.total},{s3.avg},{s3.rank}")


# 3명의 학생을 리스트에 추가
stu_list = [s1,s2,s3]


