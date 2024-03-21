# numbers에 있는 숫자들이 몇 번 나왔는지
# 딕셔너리로 출력하시오.
import operator
numbers = [1,2,4,6,4,3,6,7,1,3,4,3,4,7,7,7,7,1,1,1,7]

counter = {}

for n in numbers:
    if n not in counter:
        counter[n] = 0
    counter[n] += 1
    
print(counter) 
print(sorted(counter.items(), key=operator.itemgetter(0)))

array = [ "D", "A", "C", "A", "C", "F",
         "B", "C", "E", "C", "C", "F", "A", "B", "E", "F", "E"]
a_dic = {}

for s in array:
    if s not in array:
        a_dic[s] = 0
    a_dic[s] += 1

print(a_dic)
print(sorted(a_dic.items(), key=operator.itemgetter(0)))