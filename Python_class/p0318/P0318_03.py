class Car():   
    c_name = ""
    color = ""
    door = 0
    length = 0
    width = 0     # 값이 초기화된 class에 직접 입력값을 넣어 사용할 수 있다.
    speed = 0
    
    # 생성자   # 주문제작 클래스
    def __init__(self,c_n,c,d,l,w,s):  # 위 변수와 다른 변수임(헷갈리지 않게 변수이름 다르게...)
        self.c_name = c_n
        self.color = c
        self.door = d
        self.length = l
        self.width = w
        self.speed = s
    
    def up_speed(self,s): # class 내부에 있는 변수를 언급해줄 때
        self.speed += s
        
# 생성자를 사용한 객체선언 = 인스턴스 선언
c1 = Car("드뉴아반떼","white",5,2000,1000,60)
print("철수의 차 성능: ",c1.c_name,c1.color,c1.door,c1.length,c1.width,c1.speed)

c2 = Car("드뉴아반떼","green",5,2000,1000,100)
print("영희의 차 성능: ",c2.c_name,c2.color,c2.door,c2.length,c2.width,c2.speed)

c3 = Car("디올뉴그랜저","white pearl",2500,1400,150)
print("반장의 차 성능: ",c3.c_name,c3.color,c3.door,c3.length,c3.width,c3.speed)

# 기본생성자를 사용한 객체선언
c4 = Car()
c4.c_name = "드뉴아반떼"
c4.color = "white"
c4.door = 5
c4.length = 2000
c4.width = 1000
print("기본 성능: ",c4.c_name,c4.color,c4.door,c4.length,c4.width,c4.speed)
# c1.up_speed(60)  # 현재 speed에서 60을 더해줌  -> 60
# c1.up_speed(40)  # 현재 speed에서 40을 더해줌  -> 100
# c1.up_speed(50)  # 현재 speed에서 50을 더해줌  -> 150
# c1.speed = 50    # 현재 speed는 얼마? -> 50, 값 자체에다 50을 넣은 경우

# c2 = Car()
# c2.c_name = "드뉴아반떼"
# c2.color = "green"
# c2.door = 5
# c2.length = 2000
# c2.width = 1000
# c2.speed = 100

# c3 = Car()
# c3.c_name = "디올뉴그랜저"
# c3.color = "white pearl"
# c3.door = 5
# c3.length = 2500
# c3.width = 1400
# c3.speed = 150

# # # 철수의 차를 1대 생산
# # car_name = "드뉴아반떼"
# # color = "white"
# # door = 5
# # length = 2000
# # width = 1000
# # speed = 0

# # color = "red"
# # speed = 60


# print("반장의 차: ",c3.c_name,c3.color,c3.door,c3.length,c3.width,c3.speed)