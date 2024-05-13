a = 10
b = a  # 변수 복사
b = 100
print(a)
print(b)

a_list = [1,2,3]
b_list = a_list  # 리스트 복사 a와 b가 같은 주소를 사용하게 됨
b_list[0] = 200
print(a_list[0]) # 값? = 200
print(b_list[0]) # 200
