numbers = [1,2,3,4,5,6,7,8,9,10]

# index list에 존재하면 위치값을 리턴
# 리스트 내에 없는 숫자를 호출할 때
# 1.
print(numbers.index(5))
try:
    print(numbers.index(11))
except Exception as e:
    print("존재하지 않습니다.")
    print(e)   # 11 is not in list
# 2.
if 11 in numbers:
    print("리스트에 존재합니다.")
else:
    print("리스트에 없습니다.")