T=int(input())

for _ in range(T):
    n=int(input())
    dic=dict()
    for _ in range(n):
        name,typ=input().split()
        if typ not in dic:
            dic[typ]=1
        else:
            dic[typ]+=1
    res=1
    for key in dic:
        res*=(dic[key]+1)
    print(res-1)
