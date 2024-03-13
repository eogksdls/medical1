# 가변매개변수

def str_title(num,*txt):
    print('txt 타입: ',type(txt))
    print(txt)
    for i in range(num):
        for t in txt:
            print(t, end=' ')
        print()


str_title(1,"안녕","잘가","안녕하세요","반갑습니다")

# *000 => 튜플 타입
# 튜플은 리스트와 달리 추가,삭제,수정이 안된다.