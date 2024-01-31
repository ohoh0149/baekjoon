def get_num(a,b,c,d):
    min_num=min((a,b,c,d),(b,c,d,a),(c,d,a,b),(d,a,b,c))

    return min_num


s=set()
for a1 in range(1,10):
    for a2 in range(1,10):
        for a3 in range(1,10):
            for a4 in range(1,10):
                s.add(get_num(a1,a2,a3,a4))

lst=list(s)
lst.sort()
find_lst=tuple(map(int,input().split()))

temp=get_num(*find_lst)
print(lst.index(temp)+1)
