import operator

# 딕셔너리 정렬
t_dic = {}
t_list = []
t_dic = {'peach':'복숭아','orange':'오렌지'}

t_list = sorted(t_dic.items(),key=operator.itemgetter(0),reverse=True)
print(t_list)
# (peach,복숭아),(orange,오렌지)...

# print(t_dic.keys()) # key 값
# print(t_dic.values()) # value 값
# print(t_dic.items()) # 튜플

# 3개의 숫자를 입력받아 순서대로 출력하시오.
# num = [0,0,0]
# for i in range(3):
#     print(i)
#     num[i] = int(input("{}번째 숫자를 입력하세요.").format(i+1))