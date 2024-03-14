print("프로그램 실행")
try:   # 예외가 발생할 가능성이 있는 코드
    print(1)
    print(2)
    print(1/0) # 에러가 발생
    print(3)
except:  # 예외가 발생했을 때 실행할 코드
    print(4)
    print(5)
else:
    print(6)  # 예외가 발생하지 않으면 실행되는 코드
finally:
    print(7)  # 무조건 실행되는 코드(예외 발생 유무 안따짐)
    
print("프로그램 종료")
