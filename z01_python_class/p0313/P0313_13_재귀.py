# 재귀함수 이용
def count(num):
    if num >= 1:
        print(num,end=' ')
        count(num-1)   # 자기 함수를 다시 가져와 사용함
    else:
        return
# 재귀함수는 비교적 코드가 길어지기 때문에 별로 사용되지 않음

    
count(10)
print()

# for문 이용 -> 앞선 재귀함수에 비해 짧은 코드
num = int(input("숫자를 입력하세요:  "))
for i in range(num,0,-1):
    print(i, end=' ')