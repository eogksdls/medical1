'''
하나의 클래스 안에 변수와 함수 모두 구현 가능하다
객체 = 인스턴스 변수 ex) s1 = Student(a,b,c,..)에서 s1이 객체
인스턴스 필드에 직접 값을 대입하는 개념 ex) s1.name = "홍길동"
생성자: __init__(self)를 만들어주는 이유 -> 객체선언 시 코드 수를 줄이기 위함
class Student:
    a = ""
    b = ""
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def getName(self):
        return self.a       # 위에서 선언한 변수 a=""값에 들어가 클래스 변수가 된다.
객체 선언 : s1 = Student(a,b)          원래는 s1.a = ""
                                             s1.b = "" 이렇게 선언한 것과 동일
'''

class Car:
    count = 0  # 클래스변수 인식
    
    def __init__(self,color="black",speed=0):   # default로 키워드변수 넣어줌
        self.color = color  # init안에 변수선언 - 인스턴스 변수
        self.speed = speed
        # 클래스 변수 선언
        # Car.count = 0
        
# class를 사용하기 위해서는 인스턴스 선언
c1 = Car()  # 인스턴스 선언
c1.color = "white"
print("c1.color :",c1.color)
print("c1.speed :",c1.speed)
Car.count = 10 # 클래스변수 수정 -> count = 10이 된다.
print("c1.count :",c1.count)  # 10

c2 = Car()
c2.color = "red"
print("c2.color :",c2.color)  # red
print("c1.color :",c1.color)  # white
print("c2.count :",c2.count) # 10: 위 클래스 변수가 수정되었기 때문
# ------------------------------------
Car.count = 200
print("c1.count :",Car.count)  # 200
print("c2.count :",Car.count)  # 200
# -------------------------------------
c2.door = 4    # class내에 해당 변수가 없어도 선언은 가능하다. 단, 다른 객체엔 영향을 안줌
print("c2.door :",c2.door)
c2.count = 1 # 기존 클래스 변수를 지우고 인스턴스변수를 다시 생성
print("c1.count :",c1.count)   # 1
print("c2.count :",c2.count)   # 200: c2.count엔 영향 안줌

c3 = Car()
print("c3.count :",c3.count)   # 200