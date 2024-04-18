# 자바같은 경우 매개변수 개수에 따라 다른 함수 인정
# 파이썬은 함수 이름 무조건 다르게 해야함 


# def func(num1):
#     print(num1)
    
# def fucn2(num1,num2,num3):
#     print(num1,num2)
    

# func(1)
# func2(1,2)   # 매개변수 개수가 달라서 에러처리

def func2(num1,num2=10,num3=3):   # 키워드 매개변수 
    print(num1,num2,num3)         # => 값이 들어오지 않으면 default값으로 설정
    
func2(1)