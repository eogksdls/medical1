words = [ {},
    {"airplane":"비행기","apple":"사과","bakery":"빵집",
    "banana":"바나나","bank":"은행","bean":"콩",
    "bicycle":"자전거","boat":"배","bowl":"그릇","bus":"버스"},
    {"add":"더하다","agree":"동의하다","allow":"허락하다",
    "appear":"나타나다","ask":"묻다","become":"~이 되다","begin":"시작하다",
    "believe":"믿다","bring":"가져다 주다","build":"건축하다"},
    {"accumulated":"누적된","additional":"추가적인","adequate":"적당한",
    "administrative":"관리의","affordable":"알맞은","alternative":"대체 가능한",
    "annual":"해마다의","different":"다른","local":"지역의","social":"사회의"}
]
# 0번 자리에 빈칸을 둔 이유는, 1,2,3번으로 맞춰주기 위해서!
w_title = ["","명사","동사","형용사"]

# 함수 선언
# def 함수이름(불러올 데이터):
#     코드
def w_quiz(choice):
    print("{}를 선택하셨습니다.".format(w_title[choice]))
    ch = input("퀴즈가 나갑니다. 준비되셨나요? (1.실행, 0.취소):  ")
    if ch == "1":
        answer = 0
        wrong = 0
        for key in words[choice]:
            kor_in = input("[ {} ]의 뜻을 입력해주세요:  ".format(key))
            if kor_in == words[choice][key]:
                print("정답입니다.")
                answer += 1
            else:
                print("오답입니다. 정답: {}".format(words[choice][key]))
                wrong += 1
        print('-'*55)
        print("맞힌 명사 단어 개수: {}".format(answer))
        print("틀린 명사 단어 개수: {}".format(wrong))
    else:
        print('퀴즈를 취소하셨습니다.')

while True:
    print("\t[ 영단어 맞추기 프로그램 ]")
    print('1. 명사')
    print('2. 동사')
    print('3. 형용사')
    print('0. 종료')
    print('-'*40)
    choice = int(input("원하는 번호를 입력하세요:  "))
    
    if choice == 1:
        w_quiz(choice)
    
    elif choice == 2:
        w_quiz(choice)
        
    elif choice == 3:
        w_quiz(choice)
        
    else:
        print("단어 맞추기 프로그램을 종료합니다.")
        print('*'*55)
        break

# 구조가 반복되면, 함수를 사용하여 오류를 줄이자