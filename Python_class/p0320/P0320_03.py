class Car:
    value = "부모의 값 1"
    
    def car_func(self):
        print("부모의 값을 출력합니다.")
#-----------------------------------------------------      
class Am(Car):
    value = "자식의 값 2"
    
    def car_func(self):
        print("[ 자식 클래스에서 값 출력 ]")
        # 부모의 값을 출력하고 싶을 때 super() 사용
        super().car_func()  # "부모의 값을 출력합니다." 호출
        print("부모의 값 :", super().value)
        print("자식의 값 :", self.value)
#-----------------------------------------------------

a1 = Am()
a1.car_func()