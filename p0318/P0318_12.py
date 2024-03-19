# Car class를 선언해서
# carCount 클래스 변수
# carNo 에는 carCount 숫자를 이용해서 carNo를 넣으시오
# color="white", door=5, tire=4, speed
# up_speed 함수를 호출하면 10씩 증가가 될 수 있게 하고
# down_speed 함수를 호출하면 -10씩 감소

# c1 - white,5,4,0 -> speed 30
# c2 - red,5,4,0 -> speed 100
# c3 - silver,5,4,0 -> speed 70
# car_list 추가하고

# car_list에 있는 모든 객체의 모든 color,door,tire,speed를 출력하세요
class Car:
    carNo = 0
    carCount = 0
    def __init__(self,color,door,tire,speed):
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        Car.carCount += 1   # 클래스 변수
        self.carNo = Car.carCount
    
    def up_speed(self):
        self.speed += 10
    def down_speed(self):
        self.speed -= 10

    def __str__(self):     # 이걸 미리 써두면, 출력이 편하다(형식 출력)
        return f"{self.carNo}\t{self.color}\t{self.door}\t{self.tire}\t{self.speed}"
# __str__(self): 클래스 자체의 내용을 출력하고 싶을 때 형식을 지정하는 메서드

# 객체 프린트-----------------------------------------------------
car_list = []

c1 = Car("white",5,4,0)
for i in range(3):
    c1.up_speed()
car_list.append(c1)

c2 = Car("red",5,4,0)
for i in range(10):
    c2.up_speed()
car_list.append(c2)

c3 = Car("silver",5,4,0)
for i in range(7):
    c3.up_speed()
car_list.append(c3)

# 출력------------------------------------------------------------
print("번호\tcolor\tdoor\ttire\tspeed")
print('-'*40)
for car in car_list:
    print(car)  # -> __str__에서 적어놓은 형식에 따라 출력
    
    # __str__(self): 안썼을 때
    # print(car_list[i].carNo, car_list[i].color, car_list[i].door \
    #     , car_list[i].tire, car_list[i].speed)