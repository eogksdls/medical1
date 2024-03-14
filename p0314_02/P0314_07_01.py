# str.txt 파일의 내용을 모두 출력하세요.

# str.txt 파일 내용을 읽어와서
# str1.txt에 그 내용을 추가해보세요.

# 파일 열기
f = open("str.txt","r",encoding="utf-8")

# 파일 읽기
while True:
    content = f.readline()
    if content.strip() == "": break  # 빈공백 enter키 삭제
    print(content, end="")  # end=''가 있어야 추가 시에 공백이 안생김!

f.close()
print('-'*40)

# 파일 쓰기(기존 파일에 추가)
f = open("str.txt","r",encoding="utf-8")
ff = open("str.txt","a",encoding="utf-8")
print("추가하고 싶은 내용을 작성하세요.")
print('-'*40)
while True:
    content = f.readline()  # 파일 내용을 읽어오기
    if content.strip() == "": break
    con_input = input('')
    if con_input == '-1': break
    ff.write(con_input+'\n')
print("str.txt 파일에 텍스트를 저장했습니다.")

ff.close()
print('-'*40)

# 파일 쓰기(새로운 파일에 추가)
new_file = input("새로운 파일명:  ")
fff = open(new_file,"w",encoding="utf-8")
print("작성할 내용")
print('-'*40)
while True:
    con_input = input('')
    if con_input == '-1': break
    fff.write(con_input+'\n')
print(f"{new_file} 파일에 텍스트를 저장했습니다.")

fff.close()
print('-'*40)

# 새롭게 만든 파일 읽기
fff = open(new_file,"r",encoding="utf-8")
print("파일명: ",new_file)
print('-'*40)
while True:
    content = fff.readline()
    if content == "": break  # 한줄씩 읽는데 이제 공백이 나오면 그만 읽기
    print(content, end='')
fff.close()
print('-'*40)
