# 파일 열기
file = open("memo.txt","r",encoding='utf-8')

# 파일 읽기
content = file.read()  # .strip() 바로 붙여줘도 됨
content = content.strip() # 문자열 빈공백제거 strip()
# 1, 홍길동, 100,100,100,300,100.0,1 split(",") :  문자열을 쉼표로 분리 -> list
print(content)
stuNo,name,kor,eng,math, = content.split("\n")
c_list = [0]*5
c_list[0] = int(stuNo)
c_list[1] = name
c_list[2] = int(kor)
c_list[3] = int(eng)
c_list[4] = int(math)
print(c_list)


# 파일 닫기
file.close()
