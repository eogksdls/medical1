while True:
    print("[ 로그인 ]")
    print("-"*30)
    id = input("아이디 : ")
    pw = input("패스워드 : ")
    print("-"*30)
    
    
# 파일에서 아이디와 패스워드 확인 -----------------------------
    chk = 0
    with open("mem.csv","r",encoding="UTF-8") as f:
        while True:
            text = f.readline().strip()
            if text == "": break
            mem = text.split(",")
            if id == mem[1] and pw ==mem[2]:
                print(">> 로그인 성공")
                print('*'*30)
                chk = 1
                break
                
    # id,pw가 없으면 chk=0, 있으면 chk=1
    if chk == 1:
        print("[ 학생성적 프로그램 ]")
        print('-'*30)
        print("1. 학생성적입력")
        print("0. 종료")
        choice = int(input("원하는 번호를 입력하세요:  "))
        if choice == 1:
            print("학생성적입력을 진행합니다.")
        elif choice == 0:
            print("프로그램을 종료합니다.")
            break