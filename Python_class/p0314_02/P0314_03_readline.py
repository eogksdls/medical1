# stu.txt 파일을 출력하시오

file = open("stu.txt","r",encoding="utf-8")  # open: 통로, file=: 통로를 변수로 받는 것

while True:
    txt = file.readline()   # 파일 내 문자열들을 list로 저장 후 1개씩 출력
    if txt == "": break
    stu_list = txt.split(",")
    # for i in range(len(stu_list)-1):
    #       stu_list[i] = int(stu_list[i].strip())
    # stu_list[6] = float(stu_list[i].strip())
    print(stu_list)
    

    for i in stu_list:
        print(i, end='\n')

file.close()

# # 파일 읽어오기

# file = open("str.txt","r",encoding="utf-8")
# while True:
#     txt = file.readline() # 파일 1줄 읽어오기
#     if txt == "":
#         break
#     print(txt,end="")
    
# file.close()





# # 파일 저장
# file = open("str.txt","w",encoding="utf8")

# file.write("안녕하세요. 반갑습니다.\n")
# file.write("저는 홍길동입니다.\n")
# file.write("파이썬 수업을 열심히 듣고 있습니다.\n")

# file.close()
# print("파일이 저장되었습니다.")