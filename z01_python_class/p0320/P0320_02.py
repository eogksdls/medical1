'''
클래스의 상속(Inheritance):
기존 클래스에 있는 필드와 메서드를 그대로 물려받는 클래스를 만드는 것

상속을 했을 때 단점:
부모 클래스가 바뀌면 자식 클래스 내 필드와 메서드에 영향을 줌
따라서 상속보다는 객체선언을 하여 따로 하는 것이 낫다.
'''

class Car:
    count = 0
    
    def __init__(self,color="white",door=5,tire=4,speed=0):
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
    
    def up_speed(self):
        self.speed += 10
        
    def down_speed(self):
        self.speed -= 10
    
    def stop_speed(self):
        self.speed = 0
 
# 1. Car 클래스 상속 -> class Car 내의 필드와 메서드가 모두 상속된다.(공통 메서드가 필요할때 유용함)
class Ambul_car(Car):
    # Car클래스의 모든 것을 가져옴
    
    def up_speed(self):          # 부모 클래스와 다르게 up_speed 함수 재정의
        self.speed += 20         # 오버라이딩
        # return super().up_speed()
        
    def up_speed2(self):         # 기존 부모 클래스내 함수를 호출하고 싶을때
        return super().up_speed()   # 부모의 요소를 가져올 때 super()
           
    def siren(self):
        print("싸이렌이 울리는 기능이 추가됩니다.")
        
# 2.         
class Fire_car(Car):
    
    def water(self):
        print("물을 뿌리는 기능이 추가됩니다.")


a1 = Ambul_car("white")
print("Ambul car 현재속도 :",a1.speed)
a1.up_speed()   # 자식의 오버라이딩 된 함수를 호출
print("Ambul car 속도 업 :",a1.speed)
a1.up_speed2()  # 부모의 함수 호출
print("Ambul car 속도 업업 :",a1.speed)

a1.stop_speed()
print("Ambul car 브레이크 :",a1.speed)
print("Ambul car 색상 :",a1.color)