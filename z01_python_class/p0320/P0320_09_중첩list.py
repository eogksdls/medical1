a_list = [
    1,2,3,4,[5,6,7,8,9],[10,11]
]
aa_list = []
for a in a_list:
    if type(a) == list:
        for b in a:
            aa_list.append(b)
            print(b, end=" ")
    else:
        print(a, end=" ")
        aa_list.append(a)
print()
print(aa_list)