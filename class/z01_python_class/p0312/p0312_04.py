# 매개변수에 있는 순서, 매개변수 타입도 매우 중요하다


def str_print(txt,num):  
    for i in range(num):
        print(txt, end='')


txt = input("출력하고 싶은 글자를 입력하세요:  ")
num = int(input("출력하고 싶은 글자 반복횟수를 입력하세요:  "))
str_print(txt,num)


# 안녕하세요.
# 3
# 안녕하세요.가 3번 반복