class Student:
    name = ""
    kor = 0
    
    def __init__(self,name):    #  생성자에 매개변수가 없으면
        self.name = name
        
    def stu_print(self):    # self를 꼭 써줘야한다.
        print("학생성적을 출력합니다.")

class Lotto:
    pass


        
def s_print():
    print("class 밖에 있는 함수")     # self의 존재여부에 따라 클래스 내부/외부 함수를 구별할 수 있다.
        
s = Student("")  # 객체선언할 때 무조건 init()함수 호출
print(s)  
l = Lotto()

s_print()  # 클래스 외부 함수 호출

s.stu_print()  # 클래스 내부함수 호출 시, 객체선언을 해야 사용할 수 있다.

if isinstance(l,Student):
    print("Student 클래스 변수입니다.")
elif isinstance(l,Lotto):
    print("Lotto 클래스 변수입니다.")
    
print(type(l))