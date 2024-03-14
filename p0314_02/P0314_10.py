# 4번방이 인원수

# 파일 열기
f = open("k001.csv","r",encoding="utf-8")

cnt = 0
con_list = []
# 파일 읽기
while True:
    content = f.readline()
    if cnt == 0:  # 헤드 삭제
        cnt += 1
        continue
    if content == "": break
    cc = content.split(",")
    con_list.append(cc)

print('-'*40)

sum = 0
for con in con_list:
    sum += int(con[4])
print(f"총 인원 수: {sum:,}명") 
print('-'*40)

# 파일 닫기
f.close()

    