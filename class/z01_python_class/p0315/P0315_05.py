
#-----------------------------------------------
c_list = []
new_list = []
# 로그인 ---------------------------------------------
cnt = 0
temp = 0

while True:
    print('-'*40)
    print("[ 회원정보 ]")
    print('-'*40)
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 회원정보수정")
    print("0. 프로그램 종료")
    print('-'*40)
    choice = int(input("원하는 번호를 입력하세요:  "))
    
    if choice == 1:
        print("-"*40)
        print("\t\t[ 회원가입 ]")
        print("-"*40)
        c_id = input("ID 생성:  ")
        c_pw = input("PW 생성(0.종료):  ")
        print('-'*40)
        
        ff = open("member.txt","a",encoding="utf-8")
        ff.write(f"{c_id},{c_pw}\n")  # id,pw 추가하기
        ff.close()
        print()
        print("회원가입을 축하합니다!")
        print()
            
    elif choice == 2:
        while True:
            f = open("member.txt","r",encoding="utf-8")
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
            
            successs_flag = 0 # 로그인 실패
            while True:
                content = f.readline().strip()
                if content == "": break
                cc = content.split(",")
                c_list.append(cc)
            
            for c in c_list:
                if c_id == c[0] and c_pw == c[1]:
                    successs_flag = 1  # 로그인 성공 
                
            if successs_flag == 1:   # 로그인 성공
                print(">> 로그인 되었습니다.")
                print('-'*40)
                print(" [ 학생성적 프로그램 시작 ]")   
            else:  # 로그인 실패
                cnt += 1
                print(f"! {cnt}번째 로그인 실패 !")
                print("ID 또는 PASSWORD가 일치하지 않습니다. 다시 로그인해주세요")
            f.close()
    elif choice == 3:
        # 파일에 있는 모든 정보를 list에 저장
        # 리스트 내 아이디를 찾고, 해당 리스트 삭제 후
        # 다시 생성하는 프로세스
        member = []
        f = open("member.txt","r",encoding=("utf-8"))
        while True:
            txt = f.readline()
            if txt == "": break
            t_list = txt.split(",")
            t_list[0] = t_list[0].strip()
            t_list[1] = t_list[1].strip()
            member.append([t_list[0],t_list[1]])
        f.close()
        
        print("[ 회원정보수정 ]")
        print('-'*40)
        cnt = 0
        search = input("수정하려는 ID를 입력하세요:  ")
        for m in member:
            if search == m[0]:
                break
            cnt += 1
        if cnt == len(member):
            print("아이디가 존재하지 않습니다. 다시 입력해주세요")
        else:
            print("[ 패스워드 수정 ]")
            pw_input = input("수정할 PASSWORD를 입력하세요:  ")
            member[cnt][1] = pw_input
            
            # list의 모든 파일을 저장!
            f = open("member.txt","w",encoding="utf-8")
            for m in member:
                f.write(f"{m[0]},{m[1]}\n")
            f.close()
    
    elif choice == 0:
        print("프로그램을 종료합니다.")
        print('*'*40)
        break