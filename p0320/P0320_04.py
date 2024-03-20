class Student:
    
    def __init__(self,name,total):
        self.name = name
        self.total = total

    # def __str__(self):
    #     return f"이름 : {self.name}, 총점 : {self.total}"
    
    def __del__(self):
        return "클래스가 소멸될 때 실행"
    
    def __add__(self,s):
        return self.total+s.total
    
    def __gt__(self,s): # 크거나 같다라고 비교할 때
        return self.total > s.total
    
    def __eq__(self,s):
        return self.name==s.name and self.total == s.total
             
        
#------------
s1 = Student("홍길동",100)
s2 = Student("유관순",90)
s3 = Student("이순신",95)
s4 = Student("홍길동",100)

print(s1)  # 원래는 주소값만 출력하지만, 함수에 str을 추가해줌으로써 제일 먼저 호출되어 형식대로 출력
print(s1+s2)  # 클래스를 더하기 할 때, add함수가 제일 먼저 호출

print(s1>s2)  # 클래스는 비교가 불가능한데, __gt__메소드를 생성하면 호출
print(s2>s3)  

# print(s1)   # 주소값: 0x000001DF6D2BA750
# print(s4)   # 주소값: 0x000001DF6D2BA690
print("s1==s4 :",s1==s4)  # eq 함수 부재시 False : 내부 값이 같아도, 서로 주소값이 다르기때문에 False를 출력
print("s1==s2 :",s1==s2)  # eq 함수 존재시 내부값을 비교하여 bool 출력
