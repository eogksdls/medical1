
# 파일 열기
in_file = None
out_file = None

in_file = open("C:\workspace\medical1\member.txt","rb")
out_file = open("C:/aaaa/m1.jpg","wb")   # 폴더가 없으면 오류

# 파일 읽기, 쓰기
while True:
    bin = in_file.read(1)   # 1 byte씩 읽어오기
    if not bin: break
    out_file.write(bin)

# 파일 닫기   
in_file.close()
out_file.close()
print("복사가 완료되었습니다.")
        