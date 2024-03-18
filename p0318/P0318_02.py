class Car():
    c_name = ""
    color = ""
    door = 0
    length = 0
    width = 0            # 값이 초기화된 class에 직접 입력값을 넣어 사용할 수 있다.
    speed = 0
    
    def up_speed(self,s): # class 내부에 있는 변수를 언급해줄 때
        self.speed += s
c1 = Car()
c1.c_name = "드뉴아반떼"
c1.color = "white"
c1.door = 5
c1.length = 2000
c1.width = 1000
c1.up_speed(60)  # 현재 speed에서 60을 더해줌  -> 60
c1.up_speed(40)  # 현재 speed에서 40을 더해줌  -> 100
c1.up_speed(50)  # 현재 speed에서 50을 더해줌  -> 150
# c1.speed = 50    # 현재 speed는 얼마? -> 50, 값 자체에다 50을 넣은 경우

c2 = Car()
c2.c_name = "드뉴아반떼"
c2.color = "green"
c2.door = 5
c2.length = 2000
c2.width = 1000
c2.speed = 100

c3 = Car()
c3.c_name = "디올뉴그랜저"
c3.color = "white pearl"
c3.door = 5
c3.length = 2500
c3.width = 1400
c3.speed = 150

# # 철수의 차를 1대 생산
# car_name = "드뉴아반떼"
# color = "white"
# door = 5
# length = 2000
# width = 1000
# speed = 0

# color = "red"
# speed = 60

print("철수의 차 성능: ",c1.c_name,c1.color,c1.door,c1.length,c1.width,c1.speed)
print("영희의 차 성능: ",c2.c_name,c2.color,c2.door,c2.length,c2.width,c2.speed)
print("반장의 차: ",c3.c_name,c3.color,c3.door,c3.length,c3.width,c3.speed)