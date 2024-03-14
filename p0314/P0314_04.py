# 파일 1개 저장

# file open
file = open("memo.txt","w",encoding="utf-8")
try:
    # file write
    file.write("안녕하세요1.\n")
    file.write("안녕하세요2.\n")
    print(1/0) # 실행시 에러
    file.write("안녕하세요3.\n")
    file.write("안녕하세요4.\n")
except Exception as e:  # Exception: 예외에 대한 설명 출력. as e는 별칭 지정
    print("저장 시 에러가 났습니다.")
    print(e)
    # 파일닫기
finally:
    file.close()  # 중간에 에러가 생기면 file close가 되지 않음 
                  # -> delete를 해도 메모리 회수 불가
                  # 에러가 나도 무조건 file close를 할 수 있도록..