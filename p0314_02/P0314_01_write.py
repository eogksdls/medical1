''' 파일 열기
 읽기용: 변수명 = open("파일명","r") "r": 읽기모드, 기본값(생략 가능)
 "r+": 읽기/쓰기 겸용 모드
 쓰기용: 변수명 = open("파일명","w") 
 "a"는 기존의 파일에 이어서 추가로 저장
 "w"는 기존에 파일이 있으면 덮어서 새롭게 저장
 '''
# 파일 열기
file = open("memo.txt","w",encoding='utf-8')
stu_list = []
# 파일 쓰기
print("[ 학생성적입력 ]")
print('-'*40)
while True:
    no = input("학번을 입력하세요:  ")
    name = input("학생 이름을 입력하세요:  ")
    kor = input("국어성적 입력:  ")
    if no == '0':
        print("학생성적을 저장합니다.")
        break
    print()
    file.write(stu_list+"\n")

# for i in range(10):
#     file.write(f"안녕하세요. {i+1}\n")

# 파일 닫기
file.close()

print("파일이 저장되었습니다.")

# print("[ 메모장 실행 ]")
# print('-'*40)
# while True:
#     txt = input("글자를 입력하세요:  ")
#     if txt == '0':
#         print("메모장을 저장합니다.")
#         break
#     print(txt)