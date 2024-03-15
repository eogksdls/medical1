import P0315_02

member = P0315_02.idpw()
print(member)

# 파일 열기
f = open("member.txt","w",encoding="utf-8")

# 파일 쓰기
for m in member:
    f.write("{},{}\n".format(m[0],m[1]))


# 파일 닫기
f.close()

print("파일이 저장되었습니다.")