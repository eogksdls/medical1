# 파일 열기
f = open("member.txt","r",encoding="utf-8")
c_list = []
# 로그인 ---------------------------------------------
cnt = 0
temp = 0
while True:
    if temp == 1: 
        print("프로그램을 종료합니다.") 
        break  # 프로그램 종료
    print("-"*40)
    print("\t\t[ 로그인 ]")
    print("-"*40)
    print("* 먼저 로그인을 해주세요.")
    print()
    
    c_id = input("ID를 입력하세요.:  ")
    c_pw = input("PW를 입력하세요.(0.종료):  ")
    print('-'*40)
    
    if c_pw == "0":
        print(">> 프로그램을 종료합니다. <<")
        break  # 종료
    
    # 로그인 확인
    # member.txt 파일을 불러와서 아이디와 패스워드 비교
    # for 문으로 비교
    successs_flag = 0 # 로그인 실패
    # 파일 읽기
    
    while True:
        txt = f.readline().strip()
        if txt == "": break
        cc = txt.split(",")
        c_list.append(cc)
    
    for c in c_list:
        if c_id == c[0] and c_pw == c[1]:
            successs_flag = 1  # 로그인 성공 
        
    if successs_flag == 1:   # 로그인 성공
        print(">>로그인 되었습니다.")
        while True:
            print('-'*40)
            print('[ 학생성적 프로그램 ]')
            print("-"*40)
            print("1. 학생성적데이터 읽어오기")
            print("2. 학생성적입력")
            print("3. 학생성적출력")
            print("0. 프로그램 종료")
            print("-"*40)
            choice = int(input("원하는 번호를 입력하세요:  "))
            if choice == 1:
                pass
            elif choice == 0: 
                temp = 1  # 프로그램 종료
                break
            
    else:  # 로그인 실패
        cnt += 1
        print(f"! {cnt}번째 로그인 실패 !")
        print("ID 또는 PASSWORD가 일치하지 않습니다. 다시 로그인해주세요")
    
# 파일 닫기
f.close()