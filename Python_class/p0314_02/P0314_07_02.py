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
#---------------------------------------------------------------------
# 파일 쓰기(기존 파일에 추가)
f = open("str.txt","r",encoding="utf-8")
ff = open("str2.txt","a",encoding="utf-8")
print("추가하고 싶은 내용을 작성하세요.")
print('-'*40)
while True:
    content = f.readline()  # 파일 내용을 읽어오기
    if content.strip() == "": break
    ff.write(content)  # 파일 내용 추가하기

f.close()
ff.close()
print('-'*40)
#------------------------------------------------------------------------
# 파일 쓰기(새로운 파일에 추가)
fff = open(str.txt,"r",encoding="utf-8")

fff.close()
print('-'*40)

