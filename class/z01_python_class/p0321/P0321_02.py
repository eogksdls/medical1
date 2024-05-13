class Student:    
    def __init__(self,name="",total=0):    #  생성자에 키워드 매개변수
        self.name = name
        self.__total = total
        
    def __str__(self):
        return f"이름: {self.name}, 합계: {self.__total}"
    
    def set_total(self,total,login_id):
        if login_id == "admin":  # 데이터 접근 제한, id가 같은 사람만 접근 가능
            self.__total = total
        else:
            print("admin 관리자가 아니면 수정이 불가능합니다.")
    
    def get_total(self):       # __total 변수 자체에 접근 불가
        return self.__total    # getter 함수를 통해 __total 변수에 접근할 수 있도록
        
    def stu_print(self):    # self를 꼭 써줘야한다.
        print("학생성적을 출력합니다.")
        
    # def __gt__(self,s):
    #     return self.total > s.total

# 객체 선언
s1 = Student("홍길동",95)  # 객체선언할 때 무조건 init()함수 호출
s2 = Student("유관순",100)

# print(s1)
# print(s2)
# # --------------
# # print(s1>s2)   # 주소값으로 비교하는 것이기 때문에 에러가 난다.
# # print(s1.total > s2.total)   # __gt__함수 추가 전 비교
# print(s1>s2)   # __gt__함수 추가 후 비교

s1.total = 300   #  변수로 직접접근 : 보안상 위험  -> __total으로 적어줌으로써 직접접근을 하지 못하도록
print(s1)    # total 값 안바뀜
s1.set_total(400,"aaa")   # 프라이빗 변수 사용, 관리자가 아니면 수정을 제한할 수 있도록
print(s1)    # total 값 안바뀜
s1.set_total(400,"admin")
print(s1)    # total 값 바뀜

# print(s.__total)   __total 변수 접근 불가
print(s1.set_total(300))  # __total 변수에 접근 가능. getter&setter가 없으면 __total에 접근 아예불가  -> 코드 관리자만이 접근가능해진다.