# 12,1,2월 겨울 3,4,5월 봄 6,7,8월 여름 9,10,11월 가을

while True:
    season = input("월을 입력하세요(ex. 12월, 0. 취소):  ")
    sea = season[0:-1]
    # print(season1)
    if sea.isdigit():
        sea = int(sea)

        if 3<=sea<=5:
            print("봄 입니다.")
        elif 6<=sea<=8:
            print("여름 입니다.")
        elif 9<=sea<=11:
            print("가을 입니다.")
        elif 1<=sea<=2 or sea==12:
            print("겨울 입니다.")
        else:
            print("해당 월은 존재하지 않습니다.")
    elif season == "0" or season=="취소":
        print("프로그램을 종료합니다.")
        break
    else:
        print("다시 입력해주세요.")
