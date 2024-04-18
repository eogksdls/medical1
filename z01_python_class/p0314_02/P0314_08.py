# medical_1.csv 파일을 읽어와서 출력하시오..!!

# 파일 열기
f = open("medical_1.csv","r",encoding="utf-8")

# 파일 읽기
cnt = 0
con_list = []
while True:
    content = f.readline()
    if cnt == 0:  # 헤드는 삭제
        cnt += 1
        continue
    if content == "": break
    cc = content.split(",")
    con_list.append(cc)   # 텍스트를 리스트로 변경해서 추가하기

sum = 0
for con in con_list:
    print(con[1])
    sum += int(con[1])
print(f"8년간 기초생활보장수급자 총 인원: {sum:,} 명")  # 천 단위 ,표시
    
# 파일 닫기
f.close()
