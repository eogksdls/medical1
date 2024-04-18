class Student:
    count = 0  # 클래스 변수
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0):
        if stuNo == 0 :
            self.stuNo = Student.count   # 클래스 변수 사용
        else:
            self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor + eng + math
        self.avg = float("{:.2f}".format(self.total)/3)
        if rank != 0:
            self.rank = rank
    
    def __str__(self):
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math} \
    \t{self.total}\t{self.avg}\t{self.rank}"

# 파일 불러오기
students = []    
f = open("stu.txt","r",encoding="utf-8")
# 파일 읽기
while True:
    txt = f.readline().strip()
    if txt =="": break
    txt_list = txt.split(",")   # 텍스트를 리스트 형태로 변경
    s = Student(txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7]))
    students.append(s)
    
print("번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수")
print('-'*70)
for stu in students:
    print(stu)

f.close()