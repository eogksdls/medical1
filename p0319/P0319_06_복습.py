stu = [
    ["홍길동",100],
    ["유관순",98],
    ["이순신",95],
    ["김구",50],
    ["강감찬",99],
    ["김유신",90],
    ["홍길순",80],
    ["홍길자",70]
]

# 이름으로 검색, 홍이 들어가는 사람을 모두 검색해서 출력하시오
# 이름으로 검색, 신이 들어가는 사람을 모두 검색해서 출력하시오

# while True:
#     search = input("찾으실 이름을 입력하세요: ")
#     match = [s for s in stu if search in s[0]]
#     print(f"'{search}'(으)로 검색한 이름 :",end=" ")
#     for i in match:
#         print(i[0], end="\t")
#     print()

while True:
    print("[ 학생성적 검색 ]")
    print('-'*50)
    print("1. 이름으로 검색")
    print("2. 점수 검색")
    choice = int(input("원하는 번호를 입력하세요:  "))
    print('-'*50)
    
    if choice == 1:
        print("[ 이름으로 검색]")
        print('-'*50)
        sear_name = input("찾으실 이름을 입력하세요: ")
        search_list = [] # 찾은 사람의 위치 저장
        cnt = 0
        for s in stu:
            if s[0].find(sear_name) != -1:  # 검색어가 포함되어있는지 확인
                # print(search)
                search_list.append(cnt)
            cnt += 1
        # 검색된 사람들 출력
        if len(search_list) == 0:
            print("찾는 사람이 없습니다.")
        else:
            print(f"'{sear_name}'(으)로 검색된 사람 :",end=" ")
            for i in search_list:
                print(stu[i][0],end="\t")
            print()
            print()
            
    elif choice == 2:  # 점수를 입력해서 몇점 이상인 학생 모두 출력
        print("[ 점수로 검색 ]")
        print('-'*50)
        sear_score = int(input("점수를 입력하세요:  "))
        score_list = []
        cnt = 0
        # 점수로 검색
        for s in stu:
            if s[1] >= sear_score:
                score_list.append(cnt)
            cnt += 1
            
        # 검색된 사람들 출력
        if len(score_list) == 0:
            print(f"'{sear_score}'점 이상인 학생이 없습니다.")
            print('-'*50)
            print()
        else:
            print(f"['{sear_score}'점 이상인 학생 ]")
            for i in score_list:
                print(stu[i][0],":",stu[i][1])
            print('-'*50)
            print()
    
    
    
    
    
    
    