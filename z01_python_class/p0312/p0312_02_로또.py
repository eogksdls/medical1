import Lottodef as lt

lotto = [0]*45      # 전체 45개 숫자
lucky_lotto = [0]*6   #[0,0,0,0,0,0] # 로또 번호
my_lotto = [0]*6   # 내가 고른 번호
win_num = []   # 당첨된 번호
win_amount = [0,0,1000,10000,1000000,100000000,10000000000]

while True:
    choice = lt.screen()
    if choice == 1:
        lt.num_generate(lotto)
        
    elif choice == 2:
        lt.shuffle(lotto)
        
    elif choice == 3:
        lt.enter(my_lotto)

    elif choice == 4:
        lt.check(lotto,lucky_lotto,my_lotto,win_num,win_amount)
        win_num = []
        break
    else:
        print("해당하는 서비스가 없습니다.")
        break