def first(win_num):
    for i in range(5):
        win_num.append(i)  # append로 채울 시, 무한히 돌면서 
        #                   win_num에 숫자가 계속 누적되어 추가됨
        #                   초기화 과정 필요
    
win_num = []
while True:
    input("다시 실행할까요?")
    first(win_num)
    print("win_num 데이터 : ",win_num)
    win_num = []  # 데이터가 누적되지 않도록 초기화