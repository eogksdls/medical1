import random

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
choice = 1
cnt = 0
w_list = list(words[choice].keys())
print(w_list)
w_list_ran = random.sample(w_list,5)
for key in w_list_ran:
    kor_in = input("[ {} ]의 뜻을 입력해주세요:  ".format(key))
    if kor_in == words[choice][key]:
        print("정답입니다.")
        cnt += 1
    else:
        print("오답입니다. 정답: {}".format(words[choice][key]))
print('-'*55)
print("맞힌 명사 단어 개수: {}".format(cnt))
print("틀린 명사 단어 개수: {}".format(len(w_list_ran)-cnt))
