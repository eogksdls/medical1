class Car:
    def __init__(self,color,door,tire,speed):
        self.color = color
        self.door = door
        self.tire = tire
        self.__speed = speed   # __:클래스 내부에서만 접근이 가능하게(접근 제한)
                               # 변수의 캡슐화 : 값이 한 번에 바뀌는 것을 방지
        
    def up_speed(self,smartkey):
        if smartkey == "0x1100":  # 스마트키(비밀번호) 지정 => 스마트키가 일치할 때만 조절 가능
            self.__speed += 10
        else:
            print("smartkey가 다릅니다.")
        
    def down_speed(self):
        self.__speed -= 10
    
    def get_speed(self):
        return self.__speed
    
    def set_speed(self,speed):
        self.__speed = speed
        

c1 = Car("white",5,4,0)  # speed = 0
c1.up_speed("0x1100")    # speed = 10
c1.up_speed("0x1111")    # speed 오르지 않음
c1.set_speed(500)
c1.speed = 500

# 클래스의 변수에 직접적으로 접근이 안됨
# get을 통해서만 접근 가능
print(c1.get_speed()) 



c2 = Car("red",4,4,0)