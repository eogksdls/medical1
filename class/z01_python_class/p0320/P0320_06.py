# 퀴즈
# input 입력받은 데이터를
# p0320.txt 파일을 생성해서 저장하시오
# p_0320은 현재 날짜를 사용하시오

import datetime

now = datetime.datetime.now()
print(now.month)
print(now.day)

file_name = "P_"+now.strftime("%m%d")


f = open(f"{file_name}.txt","w",encoding="utf-8")
print("작성할 내용:")
print('-'*50)
while True:
    a = input("")
    if a == -1: break
    f.write(a+"\n")
f.close()
print("파일이 저장되었습니다.")