students = {"stuNo":1, "stuName":"홍길동", "kor":100}
# "key":"value ", key를 쓸 때는 반드시 " "로 묶어줘야 한다.
students["eng"] = 100 # 없는 키를 넣을 시 추가
students["kor"] = 50 # 이미 존재하는 키를 넣을 시 수정
del students["stuName"] # 딕셔너리 삭제
print(students)

# 타입 list, dict, int, float, str
print(students.keys()) #  딕셔너리의 키값만을 모두 뽑아내고 싶을 때
print(students.values()) # 딕셔너리 value 값만 모두 추출
print(students.items()) # 딕셔너리 key, value 토플 형태로 추출
# 토플: 수정, 삭제가 불가능
print(list(students.keys())) # 리스트 형태로


# list = [1,2,3]
# list.append(4)  # 리스트 추가
# print(list)
# del list[0]  # 리스트 삭제
# print(list)
# list[0] = 100  # 리스트 수정
# print(list)
# # list[3] = 1000   # 배열에 있는 공간을 벗어날 시, 오류를 출력한다.
# print(list)