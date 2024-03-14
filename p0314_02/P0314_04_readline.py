# 파일 읽어오기

# 1. 파일 열기
# read() : 모든 문자열을 가져옴.
# readline() : 1줄씩 가져옴
# readlines() : 1줄씩 리스트 타입에 입력해서 모두 가져옴
# 3. 파일 닫기

# 파일 확인
import os
if os.path.exists("str1.txt"): # 파일 존재 확인
    # f = open("str.txt","r",encoding="utf-8")와 동일한 표현
    with open("str.txt","r",encoding="utf-8") as f:   # 변수명을 뒤에 쓴 경우
        txt_list = f.readlines()  ## readlines 는 중요해
        
        for txt in txt_list:
            print(txt, end='')
        print()
    # f.close() 생략 가능! (with 사용시)
    





# # readlines  # 1줄씩 리스트타임으로 가져옴
# f = open("str.txt","r",encoding="utf-8")
# # 1줄씩 리스트 타입으로 저장
# txt_list = f.readlines()
# print(txt_list)

# print(txt_list[0])
# f.close()



# readline
# # f = open("str.txt","r",encoding="utf-8")

# while True:
#     txt = f.readline()
#     if txt == "": break
    
#     print(txt,end="")
#     f.close()