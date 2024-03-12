fruit = { 'peach':'복숭아','orange':'오렌지','apple':'사과',
         'pear':'배','grapes':'포도','mango':'망고','kiwi':'키위'}
# dic = {'key':'value'}
# 복숭아 영어로 입력하시오.
answer = 0
wrong = 0
for f in fruit:
    # f는 key, fruit[f]는 value를 나타낸다.
    eng_in = input('{}를 영어로 입력하세요:  '.format(fruit[f]))
    # 프로그램을 작성하세요.
    if eng_in == f:
        print('[ 정답입니다. ]')
        answer += 1
    else:
        print('[ 오답입니다. 정답은 : {} ]'.format(f))
        wrong += 1
print()
print('>>> 문제체크 <<<')       
print('맞힌 단어 개수: {}개'.format(answer))
print('틀린 단어 개수: {}개'.format(wrong))