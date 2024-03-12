a = [1,2,3,4,5]
b = a # 얕은 복사
c = [*a] # 전개 연산자
# a와 b는 같은 리스트 주소를 사용하기 때문에, 수정값도 동일하게 반영된다.
a[1] = 20
print(b) # 변경이 됨
print(c) # 변경이 안됨

product = ["새우깡","90g",1200,3]

for i in product:
    print("상품 : {}, 무게 : {}, 가격 : {}, 유통기한 : {}".format(product[0],product[1],product[2],product[3]))
