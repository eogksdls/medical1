class Student:
    stuCount = 0
    stuNo = 0  # 클래스 변수
    
    def __init__(self,name,kor,eng,math):  # 생성자
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total / 3))
        self.rank = 0
        Student.stuCount += 1 # 클래스 변수 선언! => 클래스명.변수명
        self.stuNo = Student.stuCount
        
    # 객체를 print하면 __str__함수를 제일 먼저 호출함    
    def __str__(self):
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"

stu_list = []       
print("[ 학생성적전체출력 ]")
print('-'*60)
print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
# 홍길동 학생 성적 넣기
s1 = Student("홍길동",100,100,100)   # 매개 변수가 있는 객체(인스턴스) 선언
stu_list.append(s1)

s2 = Student("유관순",100,93,88)
stu_list.append(s2)

s3 = Student("이순신",88,95,79)
stu_list.append(s3)

for i in range(len(stu_list)):
    print(stu_list[i])    # __str__을 사용하니 출력이 편하다...