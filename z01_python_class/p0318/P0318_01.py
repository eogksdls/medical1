# 사용자 정의 변수, 함수 ->  클래스
# 클래스 첫글자 대문자 사용
# 클래스 : 설계도

# 클래스 선언
class Car:
    color = "white"
    door = 5
    length = 4710
    width = 1800
    displace = 1600


    def upSpeed(self,speed):
        self.speed += speed
    
    def downSpeed(self,sp):
        self.speed -= sp
        

c1 = Car() # 클래스 객체선언 : Car 클래스에 있는 모든 변수를 사용함
print("색상 : ",c1.color) # 위에 한 번 선언을 해놓으면 한 번에 class내 여러 개의 데이터 호출 가능
c1.color = "red"
print("변경 후 색상 : ",c1.color)

c2 = Car() # 객체 선언을 할 때마다 제품이 한 개씩 생산(서로 다른 제품)
print("색상 : ",c2.color)
c3 = Car() 
