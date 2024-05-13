#
import random

# 랜덤함수를 사용하여
# 3자리 아이디를 10개 생성해서 list에 추가
# ID&PW생성-----------------------------


def idpw():
    eng = "abcdefghigklmnopqrstuvwxyz"
    pw = "123456789"

    member = [['aaa','1111']]
    a=[]
    b=[]
    c=[]
    for i in range(10):
        id1 = random.choice(eng)
        id2 = random.choice(eng)
        id3 = random.choice(eng)
        pw1 = random.choice(pw)
        pw2 = random.choice(pw)
        pw3 = random.choice(pw)
        pw4 = random.choice(pw)
        a.append(id1+id2+id3)
        b.append(pw1+pw2+pw3+pw4)
    for i in range(10):
        c.append(a[i])
        c.append(b[i])
        member.append(c)
        c=[]
    print('-'*40)
    return member
